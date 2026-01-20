import pandas as pd

UFS_BRASIL = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

def gerar_resumo_uf(df_saida, writer, df_entrada=None):
    if df_entrada is None: df_entrada = pd.DataFrame()
    
    # Consolidação íntegra para cálculo de saldo
    df_total = pd.concat([df_saida, df_entrada], ignore_index=True)
    
    # Filtro de segurança: apenas notas autorizadas
    if 'Situação Nota' in df_total.columns:
        df_total = df_total[df_total['Situação Nota'].astype(str).str.upper().str.contains('AUTORIZAD', na=False)]

    def preparar_tabela(tipo):
        base = pd.DataFrame({'UF_DEST': UFS_BRASIL})
        df_temp = df_total.copy()
        
        # Garante que não haverá duplicidade na criação de colunas de apoio
        if 'PREFIXO_AUX' not in df_temp.columns:
            df_temp['PREFIXO_AUX'] = df_temp['CFOP'].astype(str).str.strip().str[0]
        
        if tipo == 'saida':
            df_filtro = df_temp[df_temp['PREFIXO_AUX'].isin(['5', '6', '7'])]
            col_uf_final = 'UF_DEST'
        else:
            df_filtro = df_temp[df_temp['PREFIXO_AUX'].isin(['1', '2', '3'])]
            # Lógica de Devolução Própria
            df_filtro['UF_AGRUPAR'] = df_filtro.apply(
                lambda x: x['UF_DEST'] if x['UF_EMIT'] == 'SP' else x['UF_EMIT'], axis=1
            )
            col_uf_final = 'UF_AGRUPAR'

        if df_filtro.empty:
            for c in ['VAL-ICMS-ST', 'DIFAL_PURO', 'VAL-FCP-DEST', 'VAL-FCP-ST']: base[c] = 0.0
            base['IE_SUBST'] = ""
            return base

        # Agrupamento explícito para evitar conflitos de nomes de colunas como 'NCM'
        agrupado = df_filtro.groupby([col_uf_final]).agg({
            'VAL-ICMS-ST': 'sum', 
            'VAL-DIFAL': 'sum',      
            'VAL-FCP-DEST': 'sum',   
            'VAL-FCP-ST': 'sum'
        }).reset_index().rename(columns={col_uf_final: 'UF_DEST'})
        
        # Isola o DIFAL do FCP conforme regra fiscal
        agrupado['DIFAL_PURO'] = agrupado['VAL-DIFAL'] - agrupado['VAL-FCP-DEST']
        
        final = pd.merge(base, agrupado, on='UF_DEST', how='left').fillna(0)
        
        # Mapeamento de IE para destaque laranja
        ie_map = df_filtro[df_filtro['IE_SUBST'] != ""].groupby(col_uf_final)['IE_SUBST'].first().to_dict()
        final['IE_SUBST'] = final['UF_DEST'].map(ie_map).fillna("").astype(str)
        
        return final[['UF_DEST', 'IE_SUBST', 'VAL-ICMS-ST', 'DIFAL_PURO', 'VAL-FCP-DEST', 'VAL-FCP-ST']]

    res_s = preparar_tabela('saida')
    res_e = preparar_tabela('entrada')

    # Tabela de Saldo Líquido
    res_saldo = pd.DataFrame({'UF': UFS_BRASIL})
    res_saldo['IE_SUBST'] = res_s['IE_SUBST']
    
    colunas_imposto = [
        ('VAL-ICMS-ST', 'ST LÍQUIDO'), 
        ('DIFAL_PURO', 'DIFAL LÍQUIDO'), 
        ('VAL-FCP-DEST', 'FCP LÍQUIDO'), 
        ('VAL-FCP-ST', 'FCP-ST LÍQUIDO')
    ]

    for c_xml, c_fin in colunas_imposto:
        valores_saldo = []
        for i in range(len(res_s)):
            tem_ie = str(res_s.iloc[i]['IE_SUBST']).strip() != ""
            v_s = res_s.iloc[i][c_xml]
            v_e = res_e.iloc[i][c_xml]
            # Só abate se houver Inscrição Estadual de Substituto
            valores_saldo.append(v_s - v_e if tem_ie else v_s)
        res_saldo[c_fin] = valores_saldo

    # --- EXCEL (NOME DA ABA ATUALIZADO PARA DESTRAVAR) ---
    workbook = writer.book
    nome_aba = 'RESUMO_DIFAL_ST'
    
    # Recupera a aba criada pelo Core ou cria uma nova se necessário
    if nome_aba in writer.sheets:
        worksheet = writer.sheets[nome_aba]
    else:
        worksheet = workbook.add_worksheet(nome_aba)
        writer.sheets[nome_aba] = worksheet

    worksheet.hide_gridlines(2)
    
    # Estilização Visual Laranja
    f_title = workbook.add_format({'bold': True, 'align': 'center', 'font_color': '#FF6F00', 'border': 1})
    f_head = workbook.add_format({'bold': True, 'border': 1, 'bg_color': '#E0E0E0', 'align': 'center'})
    f_num = workbook.add_format({'num_format': '#,##0.00', 'border': 1})
    f_border = workbook.add_format({'border': 1})
    f_orange_num = workbook.add_format({'bg_color': '#FFDAB9', 'border': 1, 'num_format': '#,##0.00'})
    f_orange_fill = workbook.add_format({'bg_color': '#FFDAB9', 'border': 1})
    f_total = workbook.add_format({'bold': True, 'bg_color': '#F2F2F2', 'border': 1, 'num_format': '#,##0.00'})

    heads = ['UF', 'IEST (SUBST)', 'ST TOTAL', 'DIFAL TOTAL', 'FCP TOTAL', 'FCP-ST TOTAL']

    for df_t, start_c, title in [(res_s, 0, "1. SAÍDAS"), (res_e, 7, "2. ENTRADAS"), (res_saldo, 14, "3. SALDO")]:
        worksheet.merge_range(0, start_c, 0, start_c + 5, title, f_title)
        for i, h in enumerate(heads): worksheet.write(2, start_c + i, h, f_head)
        
        for r_idx, row in enumerate(df_t.values):
            uf = str(row[0]).strip()
            tem_ie = str(res_s.loc[res_s['UF_DEST'] == uf, 'IE_SUBST'].values[0]).strip() != ""
            
            for c_idx, val in enumerate(row):
                fmt = f_orange_num if tem_ie and isinstance(val, (int, float)) else f_orange_fill if tem_ie else f_num if isinstance(val, (int, float)) else f_border
                if c_idx == 1:
                    worksheet.write_string(r_idx + 3, start_c + c_idx, str(val), fmt)
                else:
                    worksheet.write(r_idx + 3, start_c + c_idx, val, fmt)
        
        # Linha de Totais Finais
        row_tot = 3 + len(UFS_BRASIL)
        worksheet.write(row_tot, start_c, "TOTAL GERAL", f_total)
        worksheet.write(row_tot, start_c + 1, "", f_total)
        for i in range(2, 6):
            c_idx = start_c + i
            col_let = chr(65 + c_idx) if c_idx < 26 else f"A{chr(65 + c_idx - 26)}"
            worksheet.write(row_tot, c_idx, f'=SUM({col_let}4:{col_let}{row_tot})', f_total)
