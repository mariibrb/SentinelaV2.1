import pandas as pd

def processar_icms(df_xs, writer, cod_cliente, df_xe=None, df_base_emp=None, modo_auditoria="CEGAS"):
    if df_xs.empty:
        return

    audit_df = df_xs.copy()
    
    # Tratamento de NCM e Cruzamento (Modo Elite)
    if modo_auditoria == "ELITE" and df_base_emp is not None:
        df_base_emp['NCM'] = df_base_emp['NCM'].astype(str).str.replace(r'\D', '', regex=True).str.strip()
        audit_df['NCM'] = audit_df['NCM'].astype(str).str.replace(r'\D', '', regex=True).str.strip()
        
        audit_df = pd.merge(
            audit_df, 
            df_base_emp[['NCM', 'ALQ_INTERNA', 'ALQ_EXTERNA', 'REDUCAO_BC', 'EXCECAO_NCM']], 
            on='NCM', how='left'
        )
    else:
        audit_df['ALQ_INTERNA'] = 0.0
        audit_df['ALQ_EXTERNA'] = 0.0
        audit_df['REDUCAO_BC'] = 0.0
        audit_df['EXCECAO_NCM'] = ""

    # Parâmetros de Diagnóstico que pensamos juntos
    audit_df['ALQ_REFERENCIA'] = audit_df.apply(
        lambda x: x['ALQ_INTERNA'] if x['UF_EMIT'] == x['UF_DEST'] else x['ALQ_EXTERNA'], axis=1
    )

    audit_df['BC-ICMS-CALC'] = audit_df.apply(
        lambda x: x['VPROD'] * (1 - (x['REDUCAO_BC'] / 100)) if x['REDUCAO_BC'] > 0 else x['VPROD'], axis=1
    )
    
    audit_df['VLR-ICMS-CALC'] = audit_df.apply(
        lambda x: round(x['BC-ICMS-CALC'] * (x['ALQ_REFERENCIA'] / 100), 2) if x['ALQ_REFERENCIA'] > 0 else 0.0, axis=1
    )

    audit_df['DIFERENCA-ICMS'] = round(audit_df['VLR-ICMS'] - audit_df['VLR-ICMS-CALC'], 2)
    audit_df['STATUS_AUDIT'] = audit_df.apply(
        lambda x: "OK" if abs(x['DIFERENCA-ICMS']) <= 0.01 else "DIVERGENTE", axis=1
    )

    # Escrita no Excel
    workbook = writer.book
    worksheet = workbook.add_worksheet('AUDIT_ICMS')
    f_header = workbook.add_format({'bold': True, 'bg_color': '#FF8C00', 'font_color': 'white', 'border': 1})
    f_divergente = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006', 'border': 1})
    f_ok = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100', 'border': 1})
    f_num = workbook.add_format({'num_format': '#,##0.00', 'border': 1})

    for col_num, value in enumerate(audit_df.columns.values):
        worksheet.write(0, col_num, value, f_header)

    for row_num, row_data in enumerate(audit_df.values):
        status = audit_df.iloc[row_num]['STATUS_AUDIT']
        fmt_status = f_divergente if status == "DIVERGENTE" else f_ok
        for col_num, cell_value in enumerate(row_data):
            if audit_df.columns[col_num] == 'STATUS_AUDIT':
                worksheet.write(row_num + 1, col_num, cell_value, fmt_status)
            elif isinstance(cell_value, (int, float)):
                worksheet.write(row_num + 1, col_num, cell_value, f_num)
            else:
                worksheet.write(row_num + 1, col_num, str(cell_value) if not pd.isna(cell_value) else "", None)
