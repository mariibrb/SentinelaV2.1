import pandas as pd

def processar_icms(df_xs, writer, cod_cliente, df_xe=None, df_base_emp=None, modo_auditoria="CEGAS"):
    """
    AUDITORIA INTEGRAL DE ICMS (MODO ELITE):
    Contém todos os diagnósticos de conferência entre XML e Base Tributária.
    """
    if df_xs.empty:
        return

    audit_df = df_xs.copy()
    
    # Tratamento de NCM para Cruzamento
    audit_df['NCM'] = audit_df['NCM'].astype(str).str.replace(r'\D', '', regex=True).str.strip()

    # --- MODO ELITE: RECUPERAÇÃO DAS REGRAS DA BASE ---
    if modo_auditoria == "ELITE" and df_base_emp is not None:
        df_base_emp['NCM'] = df_base_emp['NCM'].astype(str).str.replace(r'\D', '', regex=True).str.strip()
        
        # Merge com a Base de Dados (Alíquotas e Exceções)
        audit_df = pd.merge(
            audit_df, 
            df_base_emp[['NCM', 'ALQ_INTERNA', 'ALQ_EXTERNA', 'REDUCAO_BC', 'EXCECAO_NCM']], 
            on='NCM', 
            how='left'
        )
    else:
        audit_df['ALQ_INTERNA'] = 0.0
        audit_df['ALQ_EXTERNA'] = 0.0
        audit_df['REDUCAO_BC'] = 0.0
        audit_df['EXCECAO_NCM'] = "MODO CEGAS"

    # --- COLUNAS DE DIAGNÓSTICO (O CORAÇÃO DA AUDITORIA) ---
    
    # 1. Definição da Alíquota de Referência (Baseada no fluxo UF_EMIT -> UF_DEST)
    audit_df['ALQ_REF_BASE'] = audit_df.apply(
        lambda x: x['ALQ_INTERNA'] if x['UF_EMIT'] == x['UF_DEST'] else x['ALQ_EXTERNA'], 
        axis=1
    )

    # 2. Diagnóstico de Base de Cálculo (Verifica se houve redução indevida)
    audit_df['BC_ESPERADA'] = audit_df.apply(
        lambda x: round(x['VPROD'] * (1 - (x['REDUCAO_BC'] / 100)), 2) if x['REDUCAO_BC'] > 0 else x['VPROD'],
        axis=1
    )
    audit_df['DIF_BC'] = round(audit_df['BC-ICMS'] - audit_df['BC_ESPERADA'], 2)

    # 3. Diagnóstico de Alíquota (XML vs Base do Cliente)
    audit_df['DIF_ALQ'] = round(audit_df['ALQ-ICMS'] - audit_df['ALQ_REF_BASE'], 2)

    # 4. Diagnóstico de Valor de Imposto (Cálculo Matemático)
    audit_df['VLR_ICMS_CALC'] = audit_df.apply(
        lambda x: round(x['BC-ICMS'] * (x['ALQ_REF_BASE'] / 100), 2) if x['ALQ_REF_BASE'] > 0 else 0.0,
        axis=1
    )
    audit_df['DIF_VLR_ICMS'] = round(audit_df['VLR-ICMS'] - audit_df['VLR_ICMS_CALC'], 2)

    # 5. Status Final por Critério
    def definir_status(row):
        if abs(row['DIF_VLR_ICMS']) > 0.01: return "🚨 ERRO VALOR"
        if abs(row['DIF_ALQ']) > 0.01: return "⚠️ ALQ DIVERGENTE"
        if abs(row['DIF_BC']) > 0.10: return "📉 BC DIVERGENTE"
        return "✔️ OK"

    audit_df['DIAGNOSTICO_FINAL'] = audit_df.apply(definir_status, axis=1)

    # --- ESCRITA NO EXCEL COM FORMATAÇÃO ---
    workbook = writer.book
    worksheet = workbook.add_worksheet('AUDIT_ICMS')
    
    # Formatos
    f_header = workbook.add_format({'bold': True, 'bg_color': '#FF8C00', 'font_color': 'white', 'border': 1, 'align': 'center'})
    f_erro = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006', 'border': 1})
    f_aviso = workbook.add_format({'bg_color': '#FFEB9C', 'font_color': '#9C6500', 'border': 1})
    f_ok = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100', 'border': 1})
    f_num = workbook.add_format({'num_format': '#,##0.00', 'border': 1})
    f_text = workbook.add_format({'border': 1})

    # Cabeçalhos
    for col_num, value in enumerate(audit_df.columns.values):
        worksheet.write(0, col_num, value, f_header)

    # Escrita das linhas com lógica de cores nos diagnósticos
    for row_num, row_data in enumerate(audit_df.values):
        diag = audit_df.iloc[row_num]['DIAGNOSTICO_FINAL']
        
        for col_num, cell_value in enumerate(row_data):
            col_name = audit_df.columns[col_num]
            
            # Formatação condicional na coluna de Status e Diferenças
            if "DIAGNOSTICO" in col_name:
                fmt = f_ok if "OK" in diag else (f_erro if "ERRO" in diag else f_aviso)
                worksheet.write(row_num + 1, col_num, cell_value, fmt)
            elif isinstance(cell_value, (int, float)):
                worksheet.write(row_num + 1, col_num, cell_value, f_num)
            else:
                worksheet.write(row_num + 1, col_num, str(cell_value) if not pd.isna(cell_value) else "", f_text)

    worksheet.set_column(0, len(audit_df.columns) - 1, 15)
    worksheet.freeze_panes(1, 4)
