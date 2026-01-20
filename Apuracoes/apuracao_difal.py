import pandas as pd

UFS_BRASIL = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

def preencher_dados_difal(df_saida, df_entrada, writer, worksheet):
    df_total = pd.concat([df_saida, df_entrada], ignore_index=True)
    
    def preparar_tabela(tipo):
        base = pd.DataFrame({'UF_DEST': UFS_BRASIL})
        df_temp = df_total.copy()
        df_temp['PREFIXO'] = df_temp['CFOP'].astype(str).str.strip().str[0]
        if tipo == 'saida':
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['5', '6', '7'])]
            col_uf_final = 'UF_DEST'
        else:
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['1', '2', '3'])]
            df_filtro['UF_AGRUPAR'] = df_filtro.apply(lambda x: x['UF_DEST'] if x['UF_EMIT'] == 'SP' else x['UF_EMIT'], axis=1)
            col_uf_final = 'UF_AGRUPAR'

        agrupado = df_filtro.groupby([col_uf_final]).agg({
            'VAL-ICMS-ST': 'sum', 'VAL-DIFAL': 'sum', 'VAL-FCP-DEST': 'sum', 'VAL-FCP-ST': 'sum'
        }).reset_index().rename(columns={col_uf_final: 'UF_DEST'})
        
        agrupado['DIFAL_PURO'] = agrupado['VAL-DIFAL'] - agrupado['VAL-FCP-DEST']
        final = pd.merge(base, agrupado, on='UF_DEST', how='left').fillna(0)
        ie_map = df_filtro[df_filtro['IE_SUBST'] != ""].groupby(col_uf_final)['IE_SUBST'].first().to_dict()
        final['IE_SUBST'] = final['UF_DEST'].map(ie_map).fillna("").astype(str)
        return final

    res_s = preparar_tabela('saida'); res_e = preparar_tabela('entrada')
    res_saldo = pd.DataFrame({'UF': UFS_BRASIL})
    res_saldo['IE_SUBST'] = res_s['IE_SUBST']
    for c_xml, c_fin in [('VAL-ICMS-ST', 'ST LÍQUIDO'), ('DIFAL_PURO', 'DIFAL LÍQUIDO'), ('VAL-FCP-DEST', 'FCP LÍQUIDO'), ('VAL-FCP-ST', 'FCP-ST LÍQUIDO')]:
        res_saldo[c_fin] = res_s[c_xml] - res_e[c_xml]

    # --- ESCRITA E FORMATAÇÃO (Usando a worksheet recebida do Core) ---
    workbook = writer.book
    worksheet.hide_gridlines(2)
    f_title = workbook.add_format({'bold': True, 'align': 'center', 'font_color': '#FF6F00', 'border': 1})
    f_head = workbook.add_format({'bold': True, 'border': 1, 'bg_color': '#E0E0E0', 'align': 'center'})
    f_num = workbook.add_format({'num_format': '#,##0.00', 'border': 1})
    f_orange_num = workbook.add_format({'bg_color': '#FFDAB9', 'border': 1, 'num_format': '#,##0.00'})
    f_total = workbook.add_format({'bold': True, 'bg_color': '#F2F2F2', 'border': 1, 'num_format': '#,##0.00'})

    heads = ['UF', 'IEST (SUBST)', 'ST TOTAL', 'DIFAL TOTAL', 'FCP TOTAL', 'FCP-ST TOTAL']
    for df_t, start_c, title in [(res_s, 0, "1. SAÍDAS"), (res_e, 7, "2. ENTRADAS"), (res_saldo, 14, "3. SALDO")]:
        worksheet.merge_range(0, start_c, 0, start_c + 5, title, f_title)
        for i, h in enumerate(heads): worksheet.write(2, start_c + i, h, f_head)
        for r_idx, row in enumerate(df_t.values):
            uf = str(row[0]).strip()
            tem_ie = res_s.loc[res_s['UF_DEST'] == uf, 'IE_SUBST'].values[0] != ""
            for c_idx, val in enumerate(row):
                fmt = f_orange_num if tem_ie and isinstance(val, (int, float)) else f_num if isinstance(val, (int, float)) else workbook.add_format({'border': 1})
                worksheet.write(r_idx + 3, start_c + c_idx, val, fmt)
