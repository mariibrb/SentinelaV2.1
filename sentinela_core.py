import pandas as pd
import io
import zipfile
import streamlit as st
import xml.etree.ElementTree as ET
import re
import os

# --- FUNÇÕES DE APOIO ---
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

# --- EXTRAÇÃO DOS DADOS DO XML ---
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
            ipi_no = det.find('.//IPI'); pis_no = det.find('.//PIS'); cof_no = det.find('.//COFINS')

            linha = {
                "TIPO_SISTEMA": tipo_operacao, "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide), 
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit, "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "CNPJ_DEST": re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', dest)), 
                "IE_DEST": buscar_tag_recursiva('IE', dest), "UF_DEST": buscar_tag_recursiva('UF', dest), 
                "CFOP": buscar_tag_recursiva('CFOP', prod), "NCM": buscar_tag_recursiva('NCM', prod), 
                "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)), 
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)), 
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)), 
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)),
                "CST-ICMS": (buscar_tag_recursiva('orig', icms_no) + (buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no))),
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)),
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),
                "VAL-DIFAL": safe_float(buscar_tag_recursiva('vICMSUFDest', imp)) + safe_float(buscar_tag_recursiva('vFCPUFDest', imp)),
                "VAL-FCP-DEST": safe_float(buscar_tag_recursiva('vFCPUFDest', imp)),
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),
                
                # Tags de Auditoria Estáticas (PIS/COFINS/IPI)
                "ALQ-IPI": safe_float(buscar_tag_recursiva('pIPI', ipi_no)),
                "VLR-IPI": safe_float(buscar_tag_recursiva('vIPI', ipi_no)),
                "CST-IPI": buscar_tag_recursiva('CST', ipi_no),
                "ALQ-PIS": safe_float(buscar_tag_recursiva('pPIS', pis_no)),
                "VLR-PIS": safe_float(buscar_tag_recursiva('vPIS', pis_no)),
                "CST-PIS": buscar_tag_recursiva('CST', pis_no),
                "ALQ-COFINS": safe_float(buscar_tag_recursiva('pCOFINS', cof_no)),
                "VLR-COFINS": safe_float(buscar_tag_recursiva('vCOFINS', cof_no)),
                "CST-COFINS": buscar_tag_recursiva('CST', cof_no)
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
    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

# --- GERAÇÃO DO ARQUIVO FINAL ---
def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, df_base_emp=None, modo=None):
    # LAZY IMPORTS - CORRIGIDO
    try:
        from audit_resumo import gerar_aba_resumo             
        from Auditorias.audit_icms import processar_icms       
        from Auditorias.audit_ipi import processar_ipi         
        from Auditorias.audit_pis_cofins import processar_pc   
        from Auditorias.audit_difal import processar_difal      
        from Apuracoes.apuracao_difal import gerar_resumo_uf
    except ImportError as e:
        st.error(f"⚠️ Erro ao carregar módulos: {e}")
        return

    # Função para ler os arquivos de Autenticidade (Excel) e comparar Coluna A com B
    def preparar_referencia(arquivos_upload):
        if not arquivos_upload: return None
        dfs = []
        for f in arquivos_upload:
            try:
                f.seek(0)
                d = pd.read_excel(f)
                # Coluna A (index 0) é a Chave | Coluna F (index 5) é o Status
                ref = d.iloc[:, [0, 5]].copy()
                ref.columns = ['CHAVE_ACESSO', 'Status_Excel']
                ref['CHAVE_ACESSO'] = ref['CHAVE_ACESSO'].astype(str).str.replace('NFe', '').str.strip()
                dfs.append(ref)
            except: continue
        return pd.concat(dfs).drop_duplicates('CHAVE_ACESSO') if dfs else None

    # Merge Entradas
    ref_ent = preparar_referencia(ae)
    if ref_ent is not None:
        df_xe = pd.merge(df_xe, ref_ent, on='CHAVE_ACESSO', how='left')
        df_xe['Status'] = df_xe['Status_Excel'].fillna("SEM REFERÊNCIA")
    else:
        df_xe['Status'] = "⚠️ ANEXO ENTRADAS NÃO CARREGADO"

    # Merge Saídas
    ref_sai = preparar_referencia(as_f)
    if ref_sai is not None:
        df_xs = pd.merge(df_xs, ref_sai, on='CHAVE_ACESSO', how='left')
        df_xs['Status'] = df_xs['Status_Excel'].fillna("SEM REFERÊNCIA")
    else:
        df_xs['Status'] = "⚠️ ANEXO SAÍDAS NÃO CARREGADO"

    try: gerar_aba_resumo(writer)
    except: pass
    
    cols_xml = ["TIPO_SISTEMA", "CHAVE_ACESSO", "NUM_NF", "DATA_EMISSAO", "CNPJ_EMIT", "UF_EMIT", "CNPJ_DEST", "IE_DEST", "UF_DEST", "CFOP", "NCM", "VPROD", "BC-ICMS", "ALQ-ICMS", "VLR-ICMS", "CST-ICMS", "VAL-ICMS-ST", "IE_SUBST", "VAL-DIFAL", "VAL-FCP-DEST", "VAL-FCP-ST", "Status"]

    for df_temp, nome in [(df_xe, 'ENTRADAS_XML'), (df_xs, 'SAIDAS_XML')]:
        if not df_temp.empty:
            df_dump = df_temp[[c for c in df_temp.columns if c in cols_xml]].copy()
            df_dump[cols_xml].to_excel(writer, sheet_name=nome, index=False)

    if not df_xs.empty:
        processar_icms(df_xs, writer, cod_cliente, df_xe, df_base_emp, modo)
        try: processar_ipi(df_xs, writer, cod_cliente)
        except: pass
        try: processar_pc(df_xs, writer, cod_cliente, regime) # AGORA DEFINIDO CORRETAMENTE
        except: pass
        try: processar_difal(df_xs, writer)
        except: pass
        try: gerar_resumo_uf(df_xs, writer, df_xe)
        except: pass
