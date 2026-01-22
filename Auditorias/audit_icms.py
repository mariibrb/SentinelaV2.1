import pandas as pd
import os
import streamlit as st
import re

def processar_icms(df_xs, writer, cod_cliente, df_xe=None, df_base_emp=None, modo_auditoria="CEGAS"):
    """
    RESTAURAÇÃO SENTINELA 2.0:
    Auditoria inteligente que cruza Base Tributária, CFOP, 
    histórico de Entradas (ST) e Regras Interestaduais.
    """
    if df_xs.empty:
        return

    colunas_xml_originais = list(df_xs.columns)
    df_i = df_xs.copy()

    # --- 1. PREPARAÇÃO DO GABARITO (MODO ELITE) ---
    base_gabarito = pd.DataFrame()
    if modo_auditoria == "ELITE" and df_base_emp is not None:
        base_gabarito = df_base_emp.copy()
        base_gabarito.columns = [str(c).strip().upper() for c in base_gabarito.columns]
        col_ncm_gab = [c for c in base_gabarito.columns if 'NCM' in c]
        if col_ncm_gab:
            base_gabarito['NCM_KEY'] = base_gabarito[col_ncm_gab[0]].apply(lambda x: re.sub(r'\D', '', str(x)).strip())

    # --- 2. MAPEAMENTO DE ST NAS ENTRADAS (INTELIGÊNCIA 2.0) ---
    ncms_com_st_na_compra = []
    if df_xe is not None and not df_xe.empty:
        temp_xe = df_xe.copy()
        temp_xe['NCM_LIMP'] = temp_xe['NCM'].apply(lambda x: re.sub(r'\D', '', str(x)).strip())
        # Identifica se comprou com ST ou CST de substituição
        mask_st = (temp_xe['VAL-ICMS-ST'] > 0) | (temp_xe['CST-ICMS'].astype(str).isin(['10', '60', '70']))
        ncms_com_st_na_compra = temp_xe[mask_st]['NCM_LIMP'].unique().tolist()

    def audit_icms_linha(r):
        uf_orig = str(r.get('UF_EMIT', '')).strip().upper()
        uf_dest = str(r.get('UF_DEST', '')).strip().upper()
        cfop = str(r.get('CFOP', '')).strip()
        ncm_xml = re.sub(r'\D', '', str(r.get('NCM', ''))).strip()
        
        cst_xml = str(r.get('CST-ICMS', '00')).zfill(2)
        alq_xml = float(r.get('ALQ-ICMS', 0.0))
        bc_icms_xml = float(r.get('BC-ICMS', 0.0))
        vlr_icms_xml = float(r.get('VLR-ICMS', 0.0))

        alq_esp = None
        cst_esp = None
        fundamentacao = ""

        # PASSO 1: BASE DE DADOS (PRIORIDADE ABSOLUTA)
        if not base_gabarito.empty and 'NCM_KEY' in base_gabarito.columns:
            if ncm_xml in base_gabarito['NCM_KEY'].values:
                g = base_gabarito[base_gabarito['NCM_KEY'] == ncm_xml].iloc[0]
                
                # Busca ALIQ e CST (Interna ou Geral)
                col_alq = [c for c in base_gabarito.columns if 'ALIQ' in c and ('INTERNA' in c or ' IN' in c)]
                col_cst = [c for c in base_gabarito.columns if 'CST' in c and ('INTERNA' in c or ' IN' in c)]
                
                try:
                    if col_alq: alq_esp = float(g[col_alq[0]])
                    if col_cst: cst_esp = str(g[col_cst[0]]).strip().split('.')[0].zfill(2)
                    fundamentacao = f"Puxado da Base de Dados (NCM {ncm_xml})."
                except: pass

        # PASSO 2: REGRAS DE ST (FALHA DE GABARITO OU CFOP)
        if alq_esp is None or alq_esp == 0:
            if cfop in ['5405', '6405', '6404', '5667'] or ncm_xml in ncms_com_st_na_compra:
                cst_esp = "60"
                alq_esp = 0.0
                fundamentacao = "Identificado como ST (CFOP ou Histórico de Compra)."

        # PASSO 3: REGRAS GERAIS E INTERESTADUAIS (O CORAÇÃO DO 2.0)
        if alq_esp is None:
            if uf_orig == uf_dest:
                alq_esp = 18.0 # Padrão Interno
                fundamentacao = "Alíquota Interna Padrão (Base não localizada)."
            else:
                # Lógica Interestadual (7% ou 12%)
                sul_sudeste = ['SP', 'RJ', 'MG', 'PR', 'RS', 'SC']
                if (uf_orig in sul_sudeste and uf_dest not in sul_sudeste + ['ES']):
                    alq_esp = 7.0
                else:
                    alq_esp = 12.0
                fundamentacao = f"Regra Interestadual {uf_orig}->{uf_dest}."
            
            cst_esp = "00" if cst_esp is None else cst_esp

        # --- CÁLCULOS E DIAGNÓSTICOS ---
        # Tratamento para CSTs que não tributam (060, 040, 041)
        if cst_esp in ['60', '40', '41']:
            alq_esp = 0.0

        vlr_icms_devido = round(bc_icms_xml * (alq_esp / 100), 2)
        # Diferença de imposto (Complementar)
        vlr_comp_final = max(0.0, round(vlr_icms_devido - vlr_icms_xml, 2))

        # Diagnósticos Visuais
        diag_alq = "✅ OK" if abs(alq_xml - alq_esp) < 0.01 else f"❌ Erro (XML:{alq_xml}%|Esp:{alq_esp}%)"
        diag_cst = "✅ OK" if cst_xml == cst_esp else f"❌ Divergente (XML:{cst_xml}|Esp:{cst_esp})"
        
        status_base = "✅ Integral"
        if cst_xml in ['60', '10', '70']: status_base = "✅ ST/Retido"
        elif cst_xml == '20' or cst_esp == '20': status_base = "✅ Redução Base (CST 20)"
        
        return pd.Series([cst_esp, alq_esp, diag_cst, diag_alq, status_base, vlr_comp_final, fundamentacao])

    # --- EXECUÇÃO DA ANÁLISE ---
    analises_nomes = ['CST_ESPERADA', 'ALQ_ESPERADA', 'DIAG_CST', 'DIAG_ALQUOTA', 'STATUS_PRODUTO', 'ICMS_A_COMPLEMENTAR', 'MOTIVO_REGRA']
    df_analise = df_i.apply(audit_icms_linha, axis=1)
    df_analise.columns = analises_nomes
    
    # Organização das Colunas para o Excel
    df_final = pd.concat([df_i, df_analise], axis=1)

    # --- ESCRITA FORMATADA ---
    df_final.to_excel(writer, sheet_name='AUDIT_ICMS', index=False)
    
    # Formatação Automática de Colunas
    workbook = writer.book
    worksheet = writer.sheets['AUDIT_ICMS']
    
    f_header = workbook.add_format({'bold': True, 'bg_color': '#4F81BD', 'font_color': 'white', 'border': 1})
    f_erro = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    f_ok = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})

    # Aplica as cores de erro/ok nas colunas de diagnóstico
    for row_num in range(1, len(df_final) + 1):
        # Coluna DIAG_CST (ajustar índice conforme posição)
        val_cst = df_final.iloc[row_num-1]['DIAG_CST']
        worksheet.write(row_num, df_final.columns.get_loc('DIAG_CST'), val_cst, f_ok if "OK" in val_cst else f_erro)
        
        # Coluna DIAG_ALQUOTA
        val_alq = df_final.iloc[row_num-1]['DIAG_ALQUOTA']
        worksheet.write(row_num, df_final.columns.get_loc('DIAG_ALQUOTA'), val_alq, f_ok if "OK" in val_alq else f_erro)

    worksheet.freeze_panes(1, 4) # Congela cabeçalho e primeiras colunas
