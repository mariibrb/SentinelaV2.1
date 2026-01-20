import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os
from datetime import datetime

# --- IMPORTAÇÃO DOS MÓDULOS ESPECIALISTAS ---
try:
    from audit_resumo import gerar_aba_resumo             
    from Auditorias.audit_icms import processar_icms       
    from Auditorias.audit_ipi import processar_ipi         
    from Auditorias.audit_pis_cofins import processar_pc   
    from Auditorias.audit_difal import processar_difal      # ABA 1: Auditoria (Todas as Notas)
    from Apuracoes.apuracao_difal import gerar_resumo_uf    # ABA 2: Apuração (Saldo por Estado)
    from Gerenciais.audit_gerencial import gerar_abas_gerenciais
except ImportError as e:
    st.error(f"⚠️ Erro de Dependência: {e}")

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
            prod = det.find('prod'); imp = det.find('imposto')
            icms_no = det.find('.//ICMS'); ipi_no = det.find('.//IPI')
            
            # Captura de Tags específicas de DIFAL e FCP (UF Destino)
            v_icms_dest = safe_float(buscar_tag_recursiva('vICMSUFDest', imp))
            v_fcp_dest = safe_float(buscar_tag_recursiva('vFCPUFDest', imp))

            linha = {
                "TIPO_SISTEMA": tipo_operacao, "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide), "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit, "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "CNPJ_DEST": re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', dest)), "UF_DEST": buscar_tag_recursiva('UF', dest), 
                "CFOP": buscar_tag_recursiva('CFOP', prod),
                "NCM": tratar_ncm_texto(buscar_tag_recursiva('NCM', prod)),
                "INDIEDEST": buscar_tag_recursiva('indIEDest', dest), "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)),
                "ORIGEM": buscar_tag_recursiva('orig', icms_no), "CST-ICMS": buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no),
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)), "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)),
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)), "BC-ICMS-ST": safe_float(buscar_tag_recursiva('vBCST', icms_no)),
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)), "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),
                "VAL-FCP": safe_float(buscar_tag_recursiva('vFCP', imp)),
                "VAL-DIFAL": v_icms_dest + v_fcp_dest, 
                "VAL-FCP-DEST": v_fcp_dest
            }
            dados_lista.append(linha)
    except: pass

def extrair_dados_xml_recursivo(files, cnpj_auditado):
    dados = []
    if not files: return pd.DataFrame(), pd.DataFrame()
    def ler_zip(zip_data):
        with zipfile.ZipFile(zip_data) as z:
            for n in z.namelist():
                if n.lower().endswith('.xml'):
                    with z.open(n) as f: processar_conteudo_xml(f.read(), dados, cnpj_auditado)
    for f in files:
        f.seek(0)
        if f.name.endswith('.xml'): processar_conteudo_xml(f.read(), dados, cnpj_auditado)
        elif f.name.endswith('.zip'): ler_zip(f)
    df = pd.DataFrame(dados)
    if df.empty: return pd.DataFrame(), pd.DataFrame()
    
    cols_fix = ['VAL-FCP', 'VAL-FCP-ST', 'VAL-ICMS-ST', 'VAL-DIFAL', 'VAL-FCP-DEST', 'IE_SUBST']
    for col in cols_fix:
        if col not in df.columns: df[col] = 0.0 if col != 'IE_SUBST' else ""
            
    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, ge=None, gs=None, df_base_emp=None, modo_auditoria=None):
    if df_xs.empty and df_xe.empty: return

    # --- HIERARQUIA DE ABAS (ORDEM DE ESCRITA) ---
    try: gerar_aba_resumo(writer)
    except: pass
    
    try: gerar_abas_gerenciais(writer, ge, gs)
    except: pass
    
    try: processar_icms(df_xs, writer, cod_cliente, df_xe)
    except: pass
    
    try: processar_ipi(df_xs, writer, cod_cliente)
    except: pass
    
    try: processar_pc(df_xs, writer, cod_cliente, regime)
    except: pass

    # 1. ABA DE AUDITORIA: "audit_Difal" (Visão detalhada de todas as notas)
    try: processar_difal(df_xs, writer)
    except: pass

    # 2. ABA DE APURAÇÃO: "DIFAL_ST_FECP" (Resumo por UF e Saldo devedor)
    try: gerar_resumo_uf(df_xs, writer, df_xe)
    except: pass
