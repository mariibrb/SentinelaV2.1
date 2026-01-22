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

def safe_float(v):
    if v is None or pd.isna(v): return 0.0
    txt = str(v).strip().upper()
    if txt in ['NT', '', 'N/A', 'ISENTO', 'NULL', 'ZERO', '-', ' ']: return 0.0
    try:
        txt = txt.replace('R$', '').replace(' ', '').replace('%', '').strip()
        if ',' in txt and '.' in txt: txt = txt.replace('.', '').replace(',', '.')
        elif ',' in txt: txt = txt.replace(',', '.')
        return round(float(txt), 4)
    except: return 0.0

def buscar_tag_recursiva(tag_alvo, no):
    if no is None: return ""
    for elemento in no.iter():
        tag_nome = elemento.tag.split('}')[-1]
        if tag_nome == tag_alvo: return elemento.text if elemento.text else ""
    return ""

def processar_conteudo_xml(content, dados_lista, cnpj_empresa_auditada):
    try:
        xml_str = content.decode('utf-8', errors='replace')
        xml_str = re.sub(r'\sxmlns(:\w+)?="[^"]+"', '', xml_str) 
        root = ET.fromstring(xml_str)
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
            ipi_no = det.find('.//IPI'); pis_no = det.find('.//PIS'); cof_no = det.find('.//COFINS')
            
            origem = buscar_tag_recursiva('orig', icms_no)
            cst_parcial = buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no)
            cst_full = origem + cst_parcial if cst_parcial else origem

            linha = {
                "TIPO_SISTEMA": tipo_operacao,                 # 1
                "CHAVE_ACESSO": str(chave).strip(),            # 2
                "NUM_NF": buscar_tag_recursiva('nNF', ide),     # 3
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide), # 4
                "CNPJ_EMIT": cnpj_emit,                        # 5
                "UF_EMIT": buscar_tag_recursiva('UF', emit),   # 6
                "CNPJ_DEST": re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', dest)), # 7
                "IE_DEST": buscar_tag_recursiva('IE', dest),   # 8
                "UF_DEST": buscar_tag_recursiva('UF', dest),   # 9
                "CFOP": buscar_tag_recursiva('CFOP', prod),    # 10
                "NCM": buscar_tag_recursiva('NCM', prod),      # 11
                "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)), # 12
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)), # 13
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)), # 14
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)), # 15
                "CST-ICMS": cst_full,                          # 16
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)), # 17
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),      # 18
                "VAL-DIFAL": safe_float(buscar_tag_recursiva('vICMSUFDest', imp)) + safe_float(buscar_tag_recursiva('vFCPUFDest', imp)), # 19
                "VAL-FCP-DEST": safe_float(buscar_tag_recursiva('vFCPUFDest', imp)), # 20
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),    # 21
                "Status": "A PROCESSAR"                         # 22
            }
            
            # Tags de Apoio (Invisíveis no dump, mas essenciais para as auditorias)
            linha["ALQ-IPI"] = safe_float(buscar_tag_recursiva('pIPI', ipi_no))
            linha["VLR-IPI"] = safe_float(buscar_tag_recursiva('vIPI', ipi_no))
            linha["CST-IPI"] = buscar_tag_recursiva('CST', ipi_no)
            linha["VLR-PIS"] = safe_float(buscar_tag_recursiva('vPIS', pis_no))
            linha["VLR-COFINS"] = safe_float(buscar_tag_recursiva('vCOFINS', cof_no))
            
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

    # LÓGICA DE CRUZAMENTO COM PLANILHA DE AUTENTICIDADE
    if 'relatorio' in st.session_state and st.session_state['relatorio']:
        df_rel = pd.DataFrame(st.session_state['relatorio'])
        df_rel = df_rel.rename(columns={'Chave': 'CHAVE_ACESSO', 'Status': 'Status_Real'})
        df = pd.merge(df, df_rel[['CHAVE_ACESSO', 'Status_Real']], on='CHAVE_ACESSO', how='left')
        df['Status'] = df['Status_Real'].fillna("SEM REFERÊNCIA (FAZER GARIMPO)")
        df.drop(columns=['Status_Real'], inplace=True)
    else:
        df['Status'] = "⚠️ PLANILHA DE AUTENTICIDADE NÃO CARREGADA"

    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, ge=None, gs=None, df_base_emp=None, modo_auditoria=None):
    if df_xs.empty and df_xe.empty: return
    
    # 1. ABA RESUMO
    try: gerar_aba_resumo(writer)
    except: pass
    
    # 2. ABAS DE DADOS XML (22 Colunas)
    ordem_xml = [
        "TIPO_SISTEMA", "CHAVE_ACESSO", "NUM_NF", "DATA_EMISSAO", "CNPJ_EMIT", "UF_EMIT",
        "CNPJ_DEST", "IE_DEST", "UF_DEST", "CFOP", "NCM", "VPROD", "BC-ICMS", "ALQ-ICMS",
        "VLR-ICMS", "CST-ICMS", "VAL-ICMS-ST", "IE_SUBST", "VAL-DIFAL", "VAL-FCP-DEST",
        "VAL-FCP-ST", "Status"
    ]

    for df_temp, nome in [(df_xe, 'ENTRADAS_XML'), (df_xs, 'SAIDAS_XML')]:
        if not df_temp.empty:
            df_final = df_temp[ordem_xml].copy()
            df_final.to_excel(writer, sheet_name=nome, index=False)

    # 3. CHAMADA DAS AUDITORIAS (Sem travar o código)
    if not df_xs.empty:
        # ICMS
        try: processar_icms(df_xs, writer, cod_cliente, df_xe, df_base_emp, modo_auditoria)
        except Exception as e: st.error(f"Erro na aba ICMS: {e}")
        
        # IPI
        try: processar_ipi(df_xs, writer, cod_cliente)
        except Exception as e: st.error(f"Erro na aba IPI: {e}")
        
        # PIS/COFINS
        try: processar_pc(df_xs, writer, cod_cliente, regime)
        except Exception as e: st.error(f"Erro na aba PIS/COFINS: {e}")
        
        # DIFAL
        try: processar_difal(df_xs, writer)
        except Exception as e: st.error(f"Erro na aba DIFAL: {e}")
        
        # RESUMO UF (APURAÇÃO)
        try: gerar_resumo_uf(df_xs, writer, df_xe)
        except Exception as e: st.error(f"Erro na aba Resumo UF: {e}")
        
        # GERENCIAIS
        try: gerar_abas_gerenciais(writer, ae, as_f, ge, gs)
        except Exception as e: st.error(f"Erro nas abas Gerenciais: {e}")
