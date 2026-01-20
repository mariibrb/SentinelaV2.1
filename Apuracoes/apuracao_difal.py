import pandas as pd

UFS_BRASIL = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

def gerar_resumo_uf(df_saida, writer, df_entrada=None):
    if df_entrada is None: df_entrada = pd.DataFrame()
    df_total = pd.concat([df_saida, df_entrada], ignore_index=True)

    def preparar_tabela(tipo):
        base = pd.DataFrame({'UF_DEST': UFS_BRASIL})
        df_temp = df_total.copy()
        df_temp['PREFIXO'] = df_temp['CFOP'].astype(str).str.strip().str[0]
        
        if tipo == 'saida':
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['5', '6', '7'])]
            col_uf = 'UF_DEST'
        else:
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['1', '2', '3'])]
            df_filtro['UF_AGRUPAR'] = df_filtro.apply(lambda x: x['UF_DEST'] if x['UF_EMIT'] == 'SP' else x['UF_EMIT'], axis=1)
            col_uf = 'UF_AGRUPAR'

        agrupado = df_filtro.groupby([col_uf]).agg({
            'VAL-ICMS-ST': 'sum', 'VAL-DIFAL': 'sum', 'VAL-FCP-DEST': 'sum', 'VAL-FCP-ST': 'sum'
        }).reset_index().rename(columns={col_uf: 'UF_DEST'})
        
        ie_map = df_filtro[df_filtro['IE_SUBST'] != ""].groupby(col_uf)['IE_SUBST'].first().to_dict()
        final = pd.merge(base, agrupado, on='UF_DEST', how='left').fillna(0)
        final['IE_SUBST'] = final['UF_DEST'].map(ie_map).fillna("")
        return final

    res_s = preparar_tabela('saida'); res_e = preparar_tabela('entrada')
    res_saldo = pd.DataFrame({'UF': UFS_BRASIL}); res_saldo['IE_SUBST'] = res_s['IE_SUBST']
    
    colunas = [('VAL-ICMS-ST', 'ST LIQ'), ('VAL-DIFAL', 'DIFAL LIQ'), ('VAL-FCP-DEST', 'FCP LIQ'), ('VAL-FCP-ST', 'FCPST LIQ')]

    for c_xml, c_fin in colunas:
        saldos = []
        for i in range(len(res_s)):
            tem_ie = str(res_s.iloc[i]['IE_SUBST']).strip() != ""
            v_s = res_s.iloc[i][c_xml]; v_e = res_e.iloc[i][c_xml]
            saldos.append(v_s - v_e if tem_ie else v_s) 
        res_saldo[c_fin] = saldos

    workbook = writer.book
    worksheet = workbook.add_worksheet('DIFAL_ST_FECP')
    f_orange = workbook.add_format({'bg_color': '#FFDAB9', 'border': 1, 'num_format': '#,##0.00'})
    f_num = workbook.add_format({'border': 1, 'num_format': '#,##0.00'})
    f_head = workbook.add_format({'bold': True, 'bg_color': '#E0E0E0', 'border': 1})

    for df_t, start_c in [(res_s, 0), (res_e, 7), (res_saldo, 14)]:
        for c_idx, col in enumerate(df_t.columns):
            worksheet.write(0, start_c + c_idx, col, f_head)
            for r_idx, val in enumerate(df_t[col]):
                uf = df_t.iloc[r_idx]['UF_DEST'] if 'UF_DEST' in df_t.columns else df_t.iloc[r_idx]['UF']
                tem_ie = res_s.loc[res_s['UF_DEST'] == uf, 'IE_SUBST'].values[0] != ""
                fmt = f_orange if tem_ie else f_num
                worksheet.write(r_idx + 1, start_c + c_idx, val, fmt)
