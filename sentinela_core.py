import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os
from datetime import datetime

try:
    from audit_resumo import gerar_aba_resumo
    from Auditorias.audit_icms import processar_icms
    from Auditorias.audit_ipi import processar_ipi
    from Auditorias.audit_pis_cofins import processar_pc
    from Apuracoes.apuracao_difal import gerar_resumo_uf
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
            icms_no = det.find('.//ICMS')
            v_icms_uf_dest = safe_float(buscar_tag_recursiva('vICMSUFDest', imp))
            v_fcp_uf_dest = safe_float(buscar_tag_recursiva('vFCPUFDest', imp))

            linha = {
                "TIPO_SISTEMA": tipo_operacao, "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide),
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit, "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "UF_DEST": buscar_tag_recursiva('UF', dest), "CFOP": buscar_tag_recursiva('CFOP', prod),
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)),
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),
                "VAL-DIFAL": v_icms_uf_dest + v_fcp_uf_dest, "VAL-FCP-DEST": v_fcp_uf_dest,
                "VAL-FCP": safe_float(buscar_tag_recursiva('vFCP', imp))
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
    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None):
    try: gerar_aba_resumo(writer)
    except: pass
    
    if not df_xs.empty:
        processar_icms(df_xs, writer, cod_cliente, df_xe)
        processar_ipi(df_xs, writer, cod_cliente)
        processar_pc(df_xs, writer, cod_cliente, regime)
        
        workbook = writer.book
        nome_guia = 'DIFAL_ST_FECP'
        worksheet = workbook.add_worksheet(nome_guia)
        writer.sheets[nome_guia] = worksheet
        
        try:
            gerar_resumo_uf(df_xs, writer, df_xe)
        except Exception as e:
            st.error(f"Erro no preenchimento da aba de Saldo: {e}")
