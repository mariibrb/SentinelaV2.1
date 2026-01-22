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

# --- MOTOR DE PROCESSAMENTO XML (ORDEM EXATA DAS 22 COLUNAS) ---
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
            prod = det.find('prod'); imp = det.find('imposto')
            icms_no = det.find('.//ICMS')
            
            v_icms_uf_dest = safe_float(buscar_tag_recursiva('vICMSUFDest', imp))
            v_fcp_uf_dest = safe_float(buscar_tag_recursiva('vFCPUFDest', imp))

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
                "NCM": tratar_ncm_texto(buscar_tag_recursiva('NCM', prod)), # 11
                "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)), # 12
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)), # 13
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)), # 14
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)), # 15
                "CST-ICMS": (buscar_tag_recursiva('orig', icms_no) + (buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no))), # 16
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)), # 17
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),      # 18
                "VAL-DIFAL": v_icms_uf_dest + v_fcp_uf_dest,    # 19
                "VAL-FCP-DEST": v_fcp_uf_dest,                  # 20
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),    # 21
                "Status": "AGUARDANDO"                          # 22
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

# --- GERAÇÃO DO EXCEL FINAL (AUDITORIA MESMO SEM IMPOSTO NO XML) ---
def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, ge=None, gs=None):
    # Importação interna para blindar contra erros de ciclo
    try:
        from audit_resumo import gerar_aba_resumo
        from Auditorias.audit_icms import processar_icms
        from Auditorias.audit_ipi import processar_ipi
        from Auditorias.audit_pis_cofins import processar_pc
        from Auditorias.audit_difal import processar_difal
        from Apuracoes.apuracao_difal import gerar_resumo_uf
        from Gerenciais.audit_gerencial import gerar_abas_gerenciais
    except ImportError as e:
        st.error(f"⚠️ Erro ao carregar módulos especialistas: {e}")
        return

    try: gerar_aba_resumo(writer)
    except: pass
    
    if not df_xs.empty:
        # CRUZAMENTO COM GARIMPO
        st_map = {}
        for f_auth in ([ae] if ae else []) + ([as_f] if as_f else []):
            try:
                f_auth.seek(0)
                df_a = pd.read_excel(f_auth, header=None) if f_auth.name.endswith('.xlsx') else pd.read_csv(f_auth, header=None, sep=None, engine='python')
                df_a[0] = df_a[0].astype(str).str.replace('NFe', '').str.strip()
                st_map.update(df_a.set_index(0)[5].to_dict())
            except: continue

        df_xs['Status'] = df_xs['CHAVE_ACESSO'].map(st_map).fillna('⚠️ N/Encontrada no Garimpo')
        
        # Chamada das Auditorias - O motor de IPI vai analisar a OMISSÃO se o XML estiver zerado
        processar_icms(df_xs, writer, cod_cliente, df_xe)
        processar_ipi(df_xs, writer, cod_cliente)
        processar_pc(df_xs, writer, cod_cliente, regime)
        processar_difal(df_xs, writer)
        try: gerar_resumo_uf(df_xs, writer, df_xe)
        except: pass
        try: gerar_abas_gerenciais(writer, ge, gs)
        except: pass
