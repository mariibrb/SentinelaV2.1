import pandas as pd
import io
import zipfile
import streamlit as st
import xml.etree.ElementTree as ET
import re
import os

# --- UTILITÁRIOS ORIGINAIS ---
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

def tratar_ncm_texto(ncm):
    if pd.isna(ncm) or ncm == "": return ""
    return re.sub(r'\D', '', str(ncm)).strip()

# --- MOTOR DE PROCESSAMENTO XML (22 COLUNAS) ---
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
            
            linha = {
                "TIPO_SISTEMA": tipo_operacao, "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide), 
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit, "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "CNPJ_DEST": re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', dest)), 
                "IE_DEST": buscar_tag_recursiva('IE', dest), "UF_DEST": buscar_tag_recursiva('UF', dest), 
                "CFOP": buscar_tag_recursiva('CFOP', prod), "NCM": tratar_ncm_texto(buscar_tag_recursiva('NCM', prod)), 
                "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)), "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)), 
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)), "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)), 
                "CST-ICMS": (buscar_tag_recursiva('orig', icms_no) + (buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no))), 
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)), "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(), 
                "VAL-DIFAL": safe_float(buscar_tag_recursiva('vICMSUFDest', imp)) + safe_float(buscar_tag_recursiva('vFCPUFDest', imp)), 
                "VAL-FCP-DEST": safe_float(buscar_tag_recursiva('vFCPUFDest', imp)), "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)), 
                "Status": "A PROCESSAR"
            }
            dados_lista.append(linha)
    except: pass

def extrair_dados_xml_recursivo(files, cnpj_auditado):
    dados = []
    if not files: return pd.DataFrame(), pd.DataFrame()
    for f in files:
        f.seek(0)
        if f.name.endswith('.xml'): processar_conteudo_xml(f.read(), dados, cnpj_auditado)
        elif f.name.endswith('.zip'):
            with zipfile.ZipFile(f) as z:
                for n in z.namelist():
                    if n.lower().endswith('.xml'):
                        with z.open(n) as xml: processar_conteudo_xml(xml.read(), dados, cnpj_auditado)
    df = pd.DataFrame(dados)
    if df.empty: return pd.DataFrame(), pd.DataFrame()
    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

# --- GERAÇÃO DO EXCEL FINAL (DETECTOR DE FUNÇÕES) ---
def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, ge=None, gs=None):
    if not df_xs.empty:
        # MAPEAR STATUS
        st_map = {}
        for f_auth in ([ae] if ae else []) + ([as_f] if as_f else []):
            try:
                f_auth.seek(0)
                df_a = pd.read_excel(f_auth, header=None) if f_auth.name.endswith('.xlsx') else pd.read_csv(f_auth, header=None, sep=None, engine='python')
                df_a[0] = df_a[0].astype(str).str.replace('NFe', '').str.strip()
                st_map.update(df_a.set_index(0)[5].to_dict())
            except: continue
        df_xs['Status'] = df_xs['CHAVE_ACESSO'].map(st_map).fillna('⚠️ N/Encontrada no Garimpo')

        # --- EXECUÇÃO DINÂMICA ---
        modulos = [
            ('Auditorias.audit_icms', [df_xs, writer, cod_cliente, df_xe]),
            ('Auditorias.audit_ipi', [df_xs, writer, cod_cliente]),
            ('Auditorias.audit_pis_cofins', [df_xs, writer, cod_cliente, regime]),
            ('Auditorias.audit_difal', [df_xs, writer])
        ]

        for mod_path, args in modulos:
            try:
                import importlib
                m = importlib.import_module(mod_path)
                # Tenta achar qualquer função que pareça a correta
                funcs = [f for f in dir(m) if f.startswith(('processar', 'audit')) and callable(getattr(m, f))]
                if funcs:
                    getattr(m, funcs[0])(*args)
                else:
                    st.error(f"⚠️ Nenhuma função de auditoria achada em {mod_path}")
            except Exception as e: st.error(f"Erro em {mod_path}: {e}")

        # Finalizações
        try:
            from audit_resumo import gerar_aba_resumo
            gerar_aba_resumo(writer)
            from Apuracoes.apuracao_difal import gerar_resumo_uf
            gerar_resumo_uf(df_xs, writer, df_xe)
            from Gerenciais.audit_gerencial import gerar_abas_gerenciais
            gerar_abas_gerenciais(writer, ge, gs)
        except: pass
