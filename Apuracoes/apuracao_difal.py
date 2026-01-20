import pandas as pd

# Lista oficial de UFs para o mapa de apuração
UFS_BRASIL = [
    'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 
    'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'
]

def gerar_resumo_uf(df_saida, writer, df_entrada=None):
    """
    Gera a aba DIFAL_ST_FECP íntegra.
    Lê a IE do Substituto, pinta de laranja e abate entradas nas saídas para saldo.
    """
    if df_entrada is None: 
        df_entrada = pd.DataFrame()
    
    # Consolidação para processamento
    df_total = pd.concat([df_saida, df_entrada], ignore_index=True)

    def preparar_tabela(tipo):
        base = pd.DataFrame({'UF_DEST': UFS_BRASIL})
        df_temp = df_total.copy()
        
        # Garante CFOP string para extrair prefixo (1, 2, 3 entradas / 5, 6, 7 saídas)
        df_temp['PREFIXO'] = df_temp['CFOP'].astype(str).str.strip().str[0]
        
        if tipo == 'saida':
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['5', '6', '7'])]
            col_uf = 'UF_DEST'
        else:
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['1', '2', '3'])]
            # Lógica de agrupamento: Compras de SP usam UF_DEST, Terceiros usam UF_EMIT
            df_filtro['UF_AGRUPAR'] = df_filtro.apply(
                lambda x: x['UF_DEST'] if x['UF_EMIT'] == 'SP' else x['UF_EMIT'], axis=1
            )
            col_uf = 'UF_AGRUPAR'

        # Agregador tributário
        agrupado = df_filtro.groupby([col_uf]).agg({
            'VAL-ICMS-ST': 'sum', 
            'VAL-DIFAL': 'sum', 
            'VAL-FCP-DEST': 'sum', 
            'VAL-FCP-ST': 'sum'
        }).reset_index().rename(columns={col_uf: 'UF_DEST'})
        
        # CAPTURA DA IE_SUBST: Vital para pintura e abatimento
        ie_map = df_filtro[df_filtro['IE_SUBST'] != ""].groupby(col_uf)['IE_SUBST'].first().to_dict()
        
        final = pd.merge(base, agrupado, on='UF_DEST', how='left').fillna(0)
        final['IE_SUBST'] = final['UF_DEST'].map(ie_map).fillna("")
        return final

    # Tabelas de apoio
    res_s = preparar_tabela('saida')
    res_e = preparar_tabela('entrada')

    # --- CÁLCULO DO SALDO FINAL (ABATIMENTO) ---
    res_saldo = pd.DataFrame({'UF': UFS_BRASIL})
    res_saldo['IE_SUBST'] = res_s['IE_SUBST']
    
    colunas_cruzamento = [
        ('VAL-ICMS-ST', 'ST LIQ'), 
        ('VAL-DIFAL', 'DIFAL LIQ'), 
        ('VAL-FCP-DEST', 'FCP LIQ'), 
        ('VAL-FCP-ST', 'FCPST LIQ')
    ]

    for col_xml, col_final in colunas_cruzamento:
        valores_calc = []
        for i in range(len(res_s)):
            tem_ie = str(res_s.iloc[i]['IE_SUBST']).strip() != ""
            v_saida = res_s.iloc[i][col_xml]
            v_entrada = res_e.iloc[i][col_xml]
            
            # REGRA FISCAL: Abate entrada se houver Inscrição Estadual (IEST)
            if tem_ie:
                valores_calc.append(v_saida - v_entrada)
            else:
                valores_calc.append(v_saida)
        res_saldo[col_final] = valores_calc

    # --- FORMATAÇÃO EXCEL COM TÍTULOS E CORES ---
    workbook = writer.book
    worksheet = workbook.add_worksheet('DIFAL_ST_FECP')
    
    # Formatos Estilizados
    f_orange = workbook.add_format({'bg_color': '#FFDAB9', 'border': 1, 'num_format': '#,##0.00'})
    f_num = workbook.add_format({'border': 1, 'num_format': '#,##0.00'})
    f_head = workbook.add_format({'bold': True, 'bg_color': '#FF8C00', 'font_color': 'white', 'border': 1, 'align': 'center'})
    f_title = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center', 'bg_color': '#E0E0E0', 'border': 1})
    f_uf = workbook.add_format({'bold': True, 'border': 1, 'align': 'center'})

    # TÍTULOS DAS SEÇÕES
    worksheet.merge_range('A1:G1', '📤 SAÍDAS (RESUMO POR UF)', f_title)
    worksheet.merge_range('H1:N1', '📥 ENTRADAS (ABATIMENTOS)', f_title)
    worksheet.merge_range('O1:U1', '⚖️ SALDO FINAL A RECOLHER', f_title)

    # Escreve os Dados
    # Início na linha 2 (index 1) por causa do título mergeado
    for df_t, start_col in [(res_s, 0), (res_e, 7), (res_saldo, 14)]:
        # Cabeçalhos das colunas
        for c_idx, col_name in enumerate(df_t.columns):
            worksheet.write(1, start_col + c_idx, col_name, f_head)
            
            # Dados das linhas
            for r_idx, value in enumerate(df_t[col_name]):
                uf_linha = df_t.iloc[r_idx][df_t.columns[0]]
                # Busca se essa UF específica tem IE cadastrada nas Saídas
                ie_atual = res_s.loc[res_s['UF_DEST'] == uf_linha, 'IE_SUBST'].values[0]
                tem_ie_linha = str(ie_atual).strip() != ""
                
                if col_name in ['UF_DEST', 'UF', 'IE_SUBST']:
                    worksheet.write(r_idx + 2, start_col + c_idx, value, f_uf)
                else:
                    fmt = f_orange if tem_ie_linha else f_num
                    worksheet.write(r_idx + 2, start_col + c_idx, value, fmt)

    worksheet.set_column(0, 21, 13)
