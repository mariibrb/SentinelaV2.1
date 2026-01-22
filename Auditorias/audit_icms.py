import pandas as pd
import os
import streamlit as st
import re

def processar_icms(df_xs, writer, cod_cliente, df_xe=None, df_base_emp=None, modo_auditoria="CEGAS"):
    """
    RESTAURAÇÃO DA AUDITORIA FORENSE SENTINELA (NÍVEL 2.0)
    Analisa Alíquotas, CSTs, Benefícios, Complementos e Cartas de Correção.
    """
    if df_xs.empty:
        return

    # Criamos uma cópia profunda para não afetar o XML original
    audit_df = df_xs.copy()

    # --- 1. CARREGAMENTO DO GABARITO ELITE ---
    base_gabarito = pd.DataFrame()
    if modo_auditoria == "ELITE" and df_base_emp is not None:
        base_gabarito = df_base_emp.copy()
        base_gabarito.columns = [str(c).strip().upper() for c in base_gabarito.columns]
        # Chave de match por NCM limpo
        col_ncm = [c for c in base_gabarito.columns if 'NCM' in c]
        if col_ncm:
            base_gabarito['NCM_KEY'] = base_gabarito[col_ncm[0]].astype(str).str.replace(r'\D', '', regex=True)

    # --- 2. MAPEAMENTO DE HISTÓRICO DE ENTRADAS (INTELIGÊNCIA DE ST) ---
    ncms_com_st = []
    if df_xe is not None and not df_xe.empty:
        # Se o produto entrou com ST ou CST 60, ele deve sair como ST/60
        mask_st = (df_xe['VAL-ICMS-ST'] > 0) | (df_xe['CST-ICMS'].astype(str).isin(['10', '60', '70']))
        ncms_com_st = df_xe[mask_st]['NCM'].astype(str).str.replace(r'\D', '', regex=True).unique().tolist()

    # --- 3. FUNÇÃO DE AUDITORIA LINHA A LINHA (O CÉREBRO) ---
    def realizar_diagnostico(r):
        # Dados do XML
        ncm = str(r.get('NCM', '')).replace('.0', '')
        ncm_clean = re.sub(r'\D', '', ncm)
        cfop = str(r.get('CFOP', ''))
        origem_prod = str(r.get('CST-ICMS', '0'))[0] # Pega o primeiro dígito (Origem)
        cst_xml = str(r.get('CST-ICMS', '00'))[-2:] # Pega os dois últimos (Tributação)
        alq_xml = float(r.get('ALQ-ICMS', 0.0))
        bc_xml = float(r.get('BC-ICMS', 0.0))
        vlr_icms_xml = float(r.get('VLR-ICMS', 0.0))
        uf_orig = str(r.get('UF_EMIT', '')).upper()
        uf_dest = str(r.get('UF_DEST', '')).upper()
        tem_cce = "SIM" if str(r.get('Status', '')).upper() == "CARTA_CORRECAO" else "NÃO"

        # Valores Esperados (Gabarito)
        alq_esp = None
        cst_esp = "00"
        motivo = "Regra Geral"

        # A. Validação Interestadual (4% para importados)
        if uf_orig != uf_dest:
            if origem_prod in ['1', '2', '3', '8']: # Códigos de Importados
                alq_esp = 4.0
                motivo = "Resolução SF 13/12 (Importados)"
            else:
                sul_sudeste = ['SP', 'RJ', 'MG', 'PR', 'RS', 'SC']
                alq_esp = 7.0 if (uf_orig in sul_sudeste and uf_dest not in sul_sudeste + ['ES']) else 12.0
                motivo = f"Interrestadual {uf_orig} -> {uf_dest}"

        # B. Validação via Base de Dados (Elite)
        if not base_gabarito.empty and ncm_clean in base_gabarito['NCM_KEY'].values:
            g = base_gabarito[base_gabarito['NCM_KEY'] == ncm_clean].iloc[0]
            col_alq = [c for c in base_gabarito.columns if 'ALIQ' in c and ('INTERNA' in c or 'Geral' in c)]
            if col_alq and (alq_esp is None or uf_orig == uf_dest):
                alq_esp = float(g[col_alq[0]])
                motivo = "Localizado na Base Tributária"

        # C. Validação de Substituição Tributária (ST)
        if cfop in ['5405', '6405', '6404'] or ncm_clean in ncms_com_st:
            cst_esp = "60"
            alq_esp = 0.0
            motivo = "Produto com ST Retido anteriormente"

        # Garantia de alíquota padrão se tudo falhar
        if alq_esp is None: alq_esp = 18.0

        # --- DIAGNÓSTICOS ---
        # 1. Alíquota
        dif_alq = round(alq_xml - alq_esp, 2)
        diag_alq = "✅ OK" if abs(dif_alq) < 0.01 else f"❌ ERRO ({alq_xml}% vs {alq_esp}%)"

        # 2. CST
        diag_cst = "✅ OK" if cst_xml == cst_esp else f"❌ DIVERGENTE ({cst_xml} vs {cst_esp})"

        # 3. Cálculo de ICMS Complementar (Prejuízo)
        vlr_devido = round(bc_xml * (alq_esp / 100), 2)
        complemento = max(0.0, round(vlr_devido - vlr_icms_xml, 2))

        # 4. Status de Risco Fiscal
        if complemento > 0 or "❌" in diag_alq:
            status_risco = "🚨 ALTO RISCO"
        elif tem_cce == "SIM":
            status_risco = "⚠️ ATENÇÃO (CC-e)"
        else:
            status_risco = "✔️ CONFORME"

        return pd.Series([
            diag_alq, 
            diag_cst, 
            status_risco, 
            complemento, 
            alq_esp, 
            cst_esp, 
            motivo, 
            tem_cce
        ])

    # Aplicando o Cérebro
    colunas_analise = [
        'DIAGNOSTICO_ALQUOTA', 'DIAGNOSTICO_CST', 'VEREDITO_FINAL', 
        'ICMS_COMPLEMENTAR_R$', 'ALQ_ESPERADA_%', 'CST_ESPERADA', 
        'FUNDAMENTAÇÃO_REGRA', 'POSSUI_CCe'
    ]
    
    audit_df[colunas_analise] = audit_df.apply(realizar_diagnostico, axis=1)

    # --- 4. ESCRITA NO EXCEL COM FORMATAÇÃO DE LUXO ---
    audit_df.to_excel(writer, sheet_name='AUDIT_ICMS', index=False)
    
    workbook = writer.book
    worksheet = writer.sheets['AUDIT_ICMS']
    
    # Estilos
    f_erro = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006', 'bold': True, 'border': 1})
    f_ok = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100', 'bold': True, 'border': 1})
    f_aviso = workbook.add_format({'bg_color': '#FFEB9C', 'font_color': '#9C6500', 'border': 1})
    f_money = workbook.add_format({'num_format': 'R$ #,##0.00', 'border': 1})

    # Aplicar cores nas colunas de diagnóstico
    for row_num in range(1, len(audit_df) + 1):
        # Cor no Veredito
        veredito = audit_df.iloc[row_num-1]['VEREDITO_FINAL']
        fmt = f_ok if "CONFORME" in veredito else (f_erro if "RISCO" in veredito else f_aviso)
        worksheet.write(row_num, audit_df.columns.get_loc('VEREDITO_FINAL'), veredito, fmt)
        
        # Formatar coluna de dinheiro
        val_comp = audit_df.iloc[row_num-1]['ICMS_COMPLEMENTAR_R$']
        worksheet.write(row_num, audit_df.columns.get_loc('ICMS_COMPLEMENTAR_R$'), val_comp, f_money)

    # Ajustes finais de visual
    worksheet.set_column('A:Z', 18)
    worksheet.freeze_panes(1, 4)
