import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os
from datetime import datetime

# --- IMPORTAÇÃO DOS MÓDULOS ESPECIALISTAS (6 ABAS) ---
try:
    from audit_resumo import gerar_aba_resumo             # Aba: RESUMO
    from Auditorias.audit_icms import processar_icms       # Aba: ICMS_AUDIT
    from Auditorias.audit_ipi import processar_ipi         # Aba: IPI_AUDIT
    from Auditorias.audit_pis_cofins import processar_pc   # Aba: PIS_COFINS_AUDIT
    from Auditorias.audit_difal import processar_difal     # Aba: DIFAL_AUDIT
    from Apuracoes.apuracao_difal import gerar_resumo_uf   # Aba: DIFAL_ST_FECP
except ImportError as e:
    st.error(f"⚠️ Erro de Dependência no Core: {e}")

# --- UTILITÁRIOS DE TRATAMENTO ---
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

# --- MOTOR DE PROCESSAMENTO XML ---
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
        ind_ie_dest = buscar_tag_recursiva('indIEDest', dest)

        for det in root.findall('.//det'):
            prod = det.find('prod'); imp = det.find('imposto')
            icms_no = det.find('.//ICMS'); ipi_no = det.find('.//IPI')
            pis_no = det.find('.//PIS'); cof_no = det.find('.//COFINS')
            
            v_icms_uf_dest = safe_float(buscar_tag_recursiva('vICMSUFDest', imp))
            v_fcp_uf_dest = safe_float(buscar_tag_recursiva('vFCPUFDest', imp))

            linha = {
                "TIPO_SISTEMA": tipo_operacao, "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide),
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit, "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "UF_DEST": buscar_tag_recursiva('UF', dest), "CFOP": buscar_tag_recursiva('CFOP', prod),
                "NCM": tratar_ncm_texto(buscar_tag_recursiva('NCM', prod)),
                "INDIEDEST": ind_ie_dest,
                "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)),
                "CST-ICMS": buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no),
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)),
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)),
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)),
                "CST-IPI": buscar_tag_recursiva('CST', ipi_no),
                "ALQ-IPI": safe_float(buscar_tag_recursiva('pIPI', ipi_no)),
                "VLR-IPI": safe_float(buscar_tag_recursiva('vIPI', ipi_no)),
                "CST-PIS": buscar_tag_recursiva('CST', pis_no),
                "VLR-PIS": safe_float(buscar_tag_recursiva('vPIS', pis_no)),
                "CST-COFINS": buscar_tag_recursiva('CST', cof_no),
                "VLR-COFINS": safe_float(buscar_tag_recursiva('vCOFINS', cof_no)),
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)),
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),
                "VAL-DIFAL": v_icms_uf_dest + v_fcp_uf_dest, "VAL-FCP-DEST": v_fcp_uf_dest
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
    
    df_e = df[df['TIPO_SISTEMA'] == "ENTRADA"].copy()
    df_s = df[df['TIPO_SISTEMA'] == "SAIDA"].copy()
    return df_e, df_s

# --- GERADOR DE EXCEL FINAL (ORQUESTRADOR) ---
def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, df_base_emp=None, modo_auditoria=None):
    workbook = writer.book

    # 1. RESUMO
    try: gerar_aba_resumo(writer)
    except: pass

    if not df_xs.empty:
        # Mapeamento de Situação via Relatórios Domínio
        st_map = {}
        for f_auth in ([ae] if ae else []) + ([as_f] if as_f else []):
            try:
                f_auth.seek(0)
                df_a = pd.read_excel(f_auth, header=None) if f_auth.name.endswith('.xlsx') else pd.read_csv(f_auth, header=None, sep=None, engine='python')
                df_a[0] = df_a[0].astype(str).str.replace('NFe', '').str.strip()
                st_map.update(df_a.set_index(0)[5].to_dict())
            except: continue
        
        df_xs['Situação Nota'] = df_xs['CHAVE_ACESSO'].map(st_map).fillna('⚠️ N/Encontrada')

        # HIERARQUIA DE EXECUÇÃO DAS 5 ABAS TÉCNICAS
        abas_especialistas = [
            ('ICMS_AUDIT', processar_icms, [df_xs, writer, cod_cliente, df_xe]),
            ('IPI_AUDIT', processar_ipi, [df_xs, writer, cod_cliente]),
            ('PIS_COFINS_AUDIT', processar_pc, [df_xs, writer, cod_cliente, regime]),
            ('DIFAL_AUDIT', processar_difal, [df_xs, writer]),
            ('DIFAL_ST_FECP', gerar_resumo_uf, [df_xs, writer, df_xe])
        ]

        for nome_aba, funcao, args in abas_especialistas:
            try:
                # O Core garante a existência da aba no Writer
                if nome_aba not in writer.sheets:
                    workbook.add_worksheet(nome_aba)
                    writer.sheets[nome_aba] = workbook.get_worksheet_by_name(nome_aba)
                
                # Chama o especialista (que agora tem o comando .to_excel interno)
                funcao(*args)
            except Exception as e:
                st.error(f"⚠️ Erro ao processar aba {nome_aba}: {e}")
