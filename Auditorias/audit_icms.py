import pandas as pd
import re

def processar_icms(df_xs, writer, cod_cliente, df_xe=None, df_base_emp=None, modo_auditoria="ELITE"):
    """
    AUDITORIA FORENSE SENTINELA - COM COLUNA DE AÇÃO CORRETIVA
    """
    if df_xs.empty:
        return

    audit_df = df_xs.copy()

    # --- 1. GABARITO E HISTÓRICO ---
    ncms_com_st = []
    if df_xe is not None and not df_xe.empty:
        mask_st = (df_xe['VAL-ICMS-ST'] > 0) | (df_xe['CST-ICMS'].astype(str).isin(['10', '60', '70']))
        ncms_com_st = df_xe[mask_st]['NCM'].astype(str).str.replace(r'\D', '', regex=True).unique().tolist()

    def realizar_diagnostico(r):
        ncm_clean = re.sub(r'\D', '', str(r.get('NCM', '')))
        cfop = str(r.get('CFOP', ''))
        cst_xml = str(r.get('CST-ICMS', '00'))[-2:]
        alq_xml = float(r.get('ALQ-ICMS', 0.0))
        bc_xml = float(r.get('BC-ICMS', 0.0))
        vlr_icms_xml = float(r.get('VLR-ICMS', 0.0))
        uf_orig = str(r.get('UF_EMIT', '')).upper()
        uf_dest = str(r.get('UF_DEST', '')).upper()
        
        # Lógica de Alíquota Esperada (Interestadual vs Interna)
        if uf_orig != uf_dest:
            sul_sudeste = ['SP', 'RJ', 'MG', 'PR', 'RS', 'SC']
            alq_esp = 7.0 if (uf_orig in sul_sudeste and uf_dest not in sul_sudeste + ['ES']) else 12.0
            motivo = f"Interestadual {uf_orig}->{uf_dest}"
        else:
            alq_esp = 18.0
            motivo = "Alíquota Interna Padrão"

        # Validação de ST
        cst_esp = "00"
        if cfop in ['5405', '6405', '6404'] or ncm_clean in ncms_com_st:
            cst_esp = "60"; alq_esp = 0.0; motivo = "ST identificado"

        # CÁLCULOS FORENSES
        vlr_devido = round(bc_xml * (alq_esp / 100), 2)
        complemento = max(0.0, round(vlr_devido - vlr_icms_xml, 2))
        
        diag_alq = "✅ OK" if abs(alq_xml - alq_esp) < 0.01 else f"❌ ERRO"
        diag_cst = "✅ OK" if cst_xml == cst_esp else f"❌ DIV."
        
        status_risco = "🚨 ALTO RISCO" if complemento > 0 else "✔️ CONFORME"

        # --- LÓGICA DA AÇÃO CORRETIVA ---
        acao = []
        if "❌" in diag_alq:
            acao.append(f"Revisar Alíquota para {alq_esp}%")
        if "❌" in diag_cst:
            acao.append(f"Alterar CST para {cst_esp}")
        if complemento > 0:
            acao.append(f"Recolher ICMS Complementar de R$ {complemento}")
        
        acao_corretiva = " | ".join(acao) if acao else "Nenhuma ação necessária"

        return pd.Series([diag_alq, diag_cst, status_risco, complemento, alq_esp, cst_esp, motivo, acao_corretiva])

    # Aplicando as colunas
    colunas_novas = [
        'DIAGNOSTICO_ALQUOTA', 'DIAGNOSTICO_CST', 'VEREDITO_FISCAL', 
        'ICMS_COMPLEMENTAR_R$', 'ALQ_ESPERADA_%', 'CST_ESPERADA', 'REGRA_APLICADA', 'AÇÃO_CORRETIVA'
    ]
    audit_df[colunas_novas] = audit_df.apply(realizar_diagnostico, axis=1)

    # Gravação na aba
    audit_df.to_excel(writer, sheet_name='AUDIT_ICMS', index=False)
    
    # Formatação Visual
    workbook = writer.book
    worksheet = writer.sheets['AUDIT_ICMS']
    f_erro = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006', 'bold': True})
    f_ok = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
    f_acao = workbook.add_format({'bg_color': '#D9EAD3', 'font_color': '#274E13', 'italic': True})
    
    # Aplicar formatação nas colunas de diagnóstico e veredito
    for i, col in enumerate(audit_df.columns):
        if "DIAGNOSTICO" in col or "VEREDITO" in col:
            worksheet.conditional_format(1, i, len(audit_df), i, {
                'type': 'text', 'criteria': 'containing', 'value': '❌', 'format': f_erro
            })
            worksheet.conditional_format(1, i, len(audit_df), i, {
                'type': 'text', 'criteria': 'containing', 'value': '🚨', 'format': f_erro
            })
            worksheet.conditional_format(1, i, len(audit_df), i, {
                'type': 'text', 'criteria': 'containing', 'value': '✅', 'format': f_ok
            })
        # Destaque para a coluna de Ação Corretiva
        if col == "AÇÃO_CORRETIVA":
             worksheet.set_column(i, i, 40, f_acao)

    worksheet.freeze_panes(1, 4)
