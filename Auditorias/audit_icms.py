import pandas as pd
import re

def processar_icms(df_xs, writer, cod_cliente, df_xe=None, df_base_emp=None, modo_auditoria="ELITE"):
    """
    AUDITORIA FORENSE SENTINELA - PADRÃO MARIANA (AÇÃO + FUNDAMENTAÇÃO)
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
        
        # Lógica de Alíquota Esperada
        if uf_orig != uf_dest:
            sul_sudeste = ['SP', 'RJ', 'MG', 'PR', 'RS', 'SC']
            alq_esp = 7.0 if (uf_orig in sul_sudeste and uf_dest not in sul_sudeste + ['ES']) else 12.0
            motivo_origem = f"Regra Interestadual {uf_orig}->{uf_dest}"
        else:
            alq_esp = 18.0
            motivo_origem = "Alíquota Interna Padrão"

        # Validação de ST
        cst_esp = "00"
        if cfop in ['5405', '6405', '6404'] or ncm_clean in ncms_com_st:
            cst_esp = "60"; alq_esp = 0.0; motivo_origem = "Substituição Tributária identificada"

        # CÁLCULOS
        vlr_devido = round(bc_xml * (alq_esp / 100), 2)
        complemento = max(0.0, round(vlr_devido - vlr_icms_xml, 2))
        
        diag_alq = "✅ OK" if abs(alq_xml - alq_esp) < 0.01 else "❌ Erro"
        diag_cst = "✅ OK" if cst_xml == cst_esp else "❌ Divergente"
        
        # --- AÇÃO CORRETIVA E FUNDAMENTAÇÃO (PADRÃO 2.0) ---
        acao = "Nenhuma"
        fundamentacao = f"ICMS em conformidade para a operação. Alíquota {alq_esp}% e CST {cst_esp}."
        
        if complemento > 0.01:
            acao = "NF Complementar / Guia de Ajuste"
            fundamentacao = f"Recolhimento insuficiente. Valor devido: R$ {vlr_devido} | Valor em XML: R$ {vlr_icms_xml}. Diferença a recolher: R$ {complemento}."
        elif "❌" in diag_cst:
            acao = "Registrar CC-e"
            fundamentacao = f"CST informado no XML ({cst_xml}) difere do esperado pela legislação ({cst_esp}) para o NCM {ncm_clean}."
        elif "❌" in diag_alq:
            acao = "Registrar CC-e / Revisar Cadastro"
            fundamentacao = f"Alíquota XML ({alq_xml}%) difere da alíquota legal ({alq_esp}%). Motivo: {motivo_origem}."

        return pd.Series([diag_alq, diag_cst, complemento, alq_esp, cst_esp, acao, fundamentacao])

    # Aplicando as colunas conforme o seu padrão
    colunas_novas = [
        'DIAG_ALQUOTA_ICMS', 'DIAG_CST_ICMS', 'ICMS_COMPLEMENTAR_R$', 
        'ALQ_ESPERADA', 'CST_ESPERADO', 'AÇÃO_CORRETIVA_ICMS', 'FUNDAMENTAÇÃO_ICMS'
    ]
    audit_df[colunas_novas] = audit_df.apply(realizar_diagnostico, axis=1)

    # Gravação na aba
    audit_df.to_excel(writer, sheet_name='AUDIT_ICMS', index=False)
    
    # --- FORMATAÇÃO VISUAL ---
    workbook = writer.book
    worksheet = writer.sheets['AUDIT_ICMS']
    f_erro = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    f_ok = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
    f_num = workbook.add_format({'num_format': '#,##0.00'})

    # Ajusta larguras para caber a fundamentação
    worksheet.set_column('A:O', 15)
    worksheet.set_column('P:P', 30) # Ação Corretiva
    worksheet.set_column('Q:Q', 60) # Fundamentação

    # Aplicar cores nos diagnósticos
    for i, col in enumerate(audit_df.columns):
        if "DIAG_" in col:
            worksheet.conditional_format(1, i, len(audit_df), i, {
                'type': 'text', 'criteria': 'containing', 'value': '❌', 'format': f_erro
            })
            worksheet.conditional_format(1, i, len(audit_df), i, {
                'type': 'text', 'criteria': 'containing', 'value': '✅', 'format': f_ok
            })
