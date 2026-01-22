import pandas as pd
import io
import zipfile
import streamlit as st
import xml.etree.ElementTree as ET
import re
import os

# --- IMPORTAÇÃO DOS MÓDULOS ESPECIALISTAS ---
try:
    from audit_resumo import gerar_aba_resumo             
    from Auditorias.audit_icms import processar_icms       
    from Auditorias.audit_ipi import processar_ipi         
    from Auditorias.audit_pis_cofins import processar_pc   
    from Auditorias.audit_difal import processar_difal      
    from Apuracoes.apuracao_difal import gerar_resumo_uf    
    from Gerenciais.audit_gerencial import gerar_abas_gerenciais
except ImportError as e:
    st.error(f"⚠️ Erro de Dependência no Core: {e}")

# ... (Funções safe_float e buscar_tag_recursiva permanecem iguais) ...

def processar_conteudo_xml(content, dados_lista, cnpj_empresa_auditada):
    try:
        xml_str = content.decode('utf-8', errors='replace')
        xml_str_limpa = re.sub(r'\sxmlns(:\w+)?="[^"]+"', '', xml_str) 
        root = ET.fromstring(xml_str_limpa)
        inf = root.find('.//infNFe')
        if inf is None: return 
        
        ide = root.find('.//ide'); emit = root.find('.//emit'); dest = root.find('.//dest')
        cnpj_emit = re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', emit))
        cnpj_alvo = re.sub(r'\D', '', str(cnpj_empresa_auditada))
        tipo_nf = buscar_tag_recursiva('tpNF', ide)
        tipo_operacao = "SAIDA" if (cnpj_emit == cnpj_alvo and tipo_nf == '1') else "ENTRADA"
        chave = inf.attrib.get('Id', '')[3:]

        for det in root.findall('.//det'):
            prod = det.find('prod'); imp = det.find('imposto'); icms_no = det.find('.//ICMS')
            v_prod = safe_float(buscar_tag_recursiva('vProd', prod))
            ncm = buscar_tag_recursiva('NCM', prod)
            
            origem = buscar_tag_recursiva('orig', icms_no)
            cst_parcial = buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no)
            cst_full = origem + cst_parcial if cst_parcial else origem

            linha = {
                "TIPO_SISTEMA": tipo_operacao, "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide), 
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit, "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "CNPJ_DEST": re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', dest)), 
                "IE_DEST": buscar_tag_recursiva('IE', dest),
                "UF_DEST": buscar_tag_recursiva('UF', dest), 
                "CFOP": buscar_tag_recursiva('CFOP', prod),
                "NCM": ncm, "VPROD": v_prod, 
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)), 
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)), 
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)),
                "CST-ICMS": cst_full,
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)),
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),
                "VAL-DIFAL": safe_float(buscar_tag_recursiva('vICMSUFDest', imp)) + safe_float(buscar_tag_recursiva('vFCPUFDest', imp)),
                "VAL-FCP-DEST": safe_float(buscar_tag_recursiva('vFCPUFDest', imp)),
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no))
            }
            dados_lista.append(linha)
    except: pass

def extrair_dados_xml_recursivo(files, cnpj_auditado):
    dados = []
    for f in files:
        f.seek(0)
        if zipfile.is_zipfile(f):
            with zipfile.ZipFile(f) as z:
                for n in z.namelist():
                    if n.lower().endswith('.xml'):
                        with z.open(n) as xml: processar_conteudo_xml(xml.read(), dados, cnpj_auditado)
    
    df = pd.DataFrame(dados)
    if df.empty: return pd.DataFrame(), pd.DataFrame()

    # --- LÓGICA DE CRUZAMENTO COM PLANILHA DE AUTENTICIDADE ---
    if 'relatorio' in st.session_state and st.session_state['relatorio']:
        df_rel = pd.DataFrame(st.session_state['relatorio'])
        # Ajusta nomes de colunas do relatório de autenticidade para o merge
        df_rel = df_rel.rename(columns={'Chave': 'CHAVE_ACESSO', 'Status': 'Situação Nota'})
        df = pd.merge(df, df_rel[['CHAVE_ACESSO', 'Situação Nota']], on='CHAVE_ACESSO', how='left')
        # Se a chave não existir no relatório, avisa que falta referência
        df['Situação Nota'] = df['Situação Nota'].fillna("SEM REFERÊNCIA (FAZER GARIMPO)")
    else:
        # Se nem subiram a planilha, avisa em todas as linhas
        df['Situação Nota'] = "⚠️ PLANILHA DE AUTENTICIDADE NÃO CARREGADA"

    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, df_base_emp=None, modo=None):
    if df_xs.empty and df_xe.empty: return
    
    try: gerar_aba_resumo(writer)
    except: pass
    
    # Reorganização de colunas (Status sempre depois dos dados da nota)
    for df_temp, nome in [(df_xe, 'ENTRADAS_XML'), (df_xs, 'SAIDAS_XML')]:
        if not df_temp.empty:
            cols_originais = [c for c in df_temp.columns if c != 'Situação Nota']
            cols_status = ['Situação Nota'] 
            df_final = df_temp[cols_originais + cols_status]
            df_final.to_excel(writer, sheet_name=nome, index=False)

    if not df_xs.empty:
        processar_icms(df_xs, writer, cod_cliente, df_xe, df_base_emp, modo)
    
    try: processar_ipi(df_xs, writer, cod_cliente)
    except: pass
    try: processar_pc(df_xs, writer, cod_cliente, regime)
    except: pass
    try: processar_difal(df_xs, writer)
    except: pass
    try: gerar_resumo_uf(df_xs, writer, df_xe)
    except: pass
