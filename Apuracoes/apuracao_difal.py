import pandas as pd

# Lista oficial para garantir que todos os estados apareçam no mapa, mesmo sem movimento
UFS_BRASIL = [
    'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 
    'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'
]

def gerar_resumo_uf(df_saida, writer, df_entrada=None):
    """
    APURAÇÃO INTEGRAL DIFAL/ST/FECP:
    Realiza o cruzamento de notas de entrada e saída, respeitando a hierarquia fiscal.
    Abate o valor das entradas no saldo devedor apenas onde houver Inscrição Estadual (IEST).
    """
    if df_entrada is None: 
        df_entrada = pd.DataFrame()
    
    # Consolidação para garantir que tratamos CFOPs de devolução e transferências
    df_total = pd.concat([df_saida, df_entrada], ignore_index=True)

    def preparar_tabela_detalhada(tipo):
        base = pd.DataFrame({'UF_DEST': UFS_BRASIL})
        df_temp = df_total.copy()
        
        # Tratamento de CFOP para identificar fluxo físico vs fluxo fiscal
        df_temp['PREFIXO'] = df_temp['CFOP'].astype(str).str.strip().str[0]
        
        if tipo == 'saida':
            # Filtra operações de saída (5, 6, 7)
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['5', '6', '7'])]
            col_uf = 'UF_DEST'
        else:
            # Filtra operações de entrada (1, 2, 3)
            df_filtro = df_temp[df_temp['PREFIXO'].isin(['1', '2', '3'])]
            # Regra de agregação: Compras de SP (internas) vs Compras de outros estados
            df_filtro['UF_AGRUPAR'] = df_filtro.apply(
                lambda x: x['UF_DEST'] if x['UF_EMIT'] == 'SP' else x['UF_EMIT'], axis=1
            )
            col_uf = 'UF_AGRUPAR'

        # --- A PORRADA DE COLUNAS DE CONFERÊNCIA ---
        agrupado = df_filtro.groupby([col_uf]).agg({
            'VPROD': 'sum',
            'BC-ICMS': 'sum',
            'VAL-ICMS-ST': 'sum', 
            'VAL-DIFAL': 'sum', 
            'VAL-FCP-DEST': 'sum', 
            'VAL-FCP-ST': 'sum'
        }).reset_index().rename(columns={col_uf: 'UF_DEST'})
        
        # Captura da IE do Substituto (IEST) para a Coluna B (Saída) / I (Entrada)
        ie_map = df_filtro[df_filtro['IE_SUBST'] != ""].groupby(col_uf)['IE_SUBST'].first().to_dict()
        
        final = pd.merge(base, agrupado, on='UF_DEST', how='left').fillna(0)
        
        # Insere a IE na segunda coluna (B ou I dependendo do bloco)
        final.insert(1, 'IE_SUBST', final['UF_DEST'].map(ie_map).fillna(""))
        
        # Renomeia colunas para o diagnóstico ficar claro no Excel
        prefix = "S_" if tipo == 'saida' else "E_"
        final.columns = [prefix + col if col not in ['UF_DEST', 'IE_SUBST'] else col for col in final.columns]
        
        return final

    # Gera os blocos de dados
    res_s = preparar_tabela_detalhada('saida')
    res_e = preparar_tabela_detalhada('entrada')

    # --- BLOCO DE SALDO FINAL (APURAÇÃO LÍQUIDA) ---
    res_saldo = pd.DataFrame({'UF': UFS_BRASIL})
    res_saldo['IE_SUBST'] = res_s['IE_SUBST']
    
    # Cruzamento para cálculo de saldo (Saída - Entrada)
    colunas_calculo = [
        ('VAL-ICMS-ST', 'ST LIQ'), 
        ('VAL-DIFAL', 'DIFAL LIQ'), 
        ('VAL-FCP-DEST', 'FCP LIQ'), 
        ('VAL-FCP-ST', 'FCPST LIQ')
    ]

    for col_xml, col_final in colunas_calculo:
        lista_saldos = []
        for i in range(len(res_s)):
            tem_ie = str(res_s.iloc[i]['IE_SUBST']).strip() != ""
            v_saida = res_s.iloc[i]['S_' + col_xml]
            v_entrada = res_e.iloc[i]['E_' + col_xml]
            
            # REGRA MESTRA: Se tem IE na UF, considera apuração e abate. 
            # Se não tem, o valor de saída é o saldo devedor por guia única.
            if tem_ie:
                lista_saldos.append(v_saida - v_entrada)
            else:
                lista_saldos.append(v_saida)
        res_saldo[col_final] = lista_saldos

    # --- FORMATAÇÃO RÍGIDA DO EXCEL (TÍTULOS E CORES) ---
    workbook = writer.book
    worksheet = workbook.add_worksheet('DIFAL_ST_FECP')
    
    # Estilos
    f_title = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center', 'bg_color': '#E0E0E0', 'border': 1})
    f_head = workbook.add_format({'bold': True, 'bg_color': '#FF8C00', 'font_color': 'white', 'border': 1, 'align': 'center'})
    f_orange = workbook.add_format({'bg_color': '#FFDAB9', 'border': 1, 'num_format': '#,##0.00'})
    f_num = workbook.add_format({'border': 1, 'num_format': '#,##0.00'})
    f_uf = workbook.add_format({'bold': True, 'border': 1, 'align': 'center'})

    # TÍTULOS MERGEADOS (A PORRADA DE COLUNAS DIVIDIDA POR BLOCOS)
    # Bloco Saídas: A até G (7 colunas)
    worksheet.merge_range('A1:G1', '📤 SAÍDAS (RESUMO POR UF)', f_title)
    # Bloco Entradas: H até N (7 colunas)
    worksheet.merge_range('H1:N1', '📥 ENTRADAS (ABATIMENTOS)', f_title)
    # Bloco Saldo: O até U (6 colunas)
    worksheet.merge_range('O1:U1', '⚖️ SALDO FINAL A RECOLHER', f_title)

    # Escrita dos Dados
    for df_t, start_col in [(res_s, 0), (res_e, 7), (res_saldo, 14)]:
        # Escreve cabeçalhos na linha 2
        for c_idx, col_name in enumerate(df_t.columns):
            worksheet.write(1, start_col + c_idx, col_name, f_head)
            
            # Escreve dados a partir da linha 3
            for r_idx, value in enumerate(df_t[col_name]):
                uf_linha = df_t.iloc[r_idx][0]
                # Verifica no bloco de saída se aquela UF tem IE para pintar de laranja
                ie_verificacao = str(res_s.loc[res_s['UF_DEST'] == uf_linha, 'IE_SUBST'].values[0]).strip()
                
                if col_name in ['UF_DEST', 'UF', 'IE_SUBST']:
                    worksheet.write(r_idx + 2, start_col + c_idx, value, f_uf)
                else:
                    fmt = f_orange if ie_verificacao != "" else f_num
                    worksheet.write(r_idx + 2, start_col + c_idx, value, fmt)

    worksheet.set_column(0, 25, 14)
    worksheet.freeze_panes(2, 1)
