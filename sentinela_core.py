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

# --- MOTOR DE EXTRAÇÃO XML ---
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
            icms_no = det.find('.//ICMS'); ipi_no = det.find('.//IPI')
            pis_no = det.find('.//PIS'); cof_no = det.find('.//COFINS')
            
            origem = buscar_tag_recursiva('orig', icms_no)
            cst_parcial = buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no)
            cst_full = origem + cst_parcial if cst_parcial else origem

            linha = {
                "TIPO_SISTEMA": tipo_operacao, "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide), 
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit, "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "CNPJ_DEST": re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', dest)), 
                "UF_DEST": buscar_tag_recursiva('UF', dest), 
                "INDIEDEST": buscar_tag_recursiva('indIEDest', dest),
                "CFOP": buscar_tag_recursiva('CFOP', prod), "NCM": buscar_tag_recursiva('NCM', prod), 
                "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)), 
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)), 
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)), 
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)),
                "CST-ICMS": cst_full,
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)),
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),
                "VAL-DIFAL": safe_float(buscar_tag_recursiva('vICMSUFDest', imp)) + safe_float(buscar_tag_recursiva('vFCPUFDest', imp)),
                
                "ALQ-IPI": safe_float(buscar_tag_recursiva('pIPI', ipi_no)),
                "VLR-IPI": safe_float(buscar_tag_recursiva('vIPI', ipi_no)),
                "CST-IPI": buscar_tag_recursiva('CST', ipi_no),
                "CST-PIS": buscar_tag_recursiva('CST', pis_no),
                "VLR-PIS": safe_float(buscar_tag_recursiva('vPIS', pis_no)),
                "CST-COFINS": buscar_tag_recursiva('CST', cof_no),
                "VLR-COFINS": safe_float(buscar_tag_recursiva('vCOFINS', cof_no))
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

# --- GERAÇÃO DAS 06 ABAS (ORDEM: RESUMO COMO A PRIMEIRA ABA) ---
def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, df_base_emp=None, modo=None):
    if df_xs.empty and df_xe.empty: return
    
    try:
        import audit_resumo
        from Auditorias import audit_icms, audit_ipi, audit_pis_cofins, audit_difal
        from Apuracoes import apuracao_difal
    except ImportError as e:
        st.error(f"⚠️ Erro ao carregar módulos especialistas: {e}")
        return

    # --- ABA 1: RESUMO (EXECUTADA PRIMEIRO PARA APARECER NA FRENTE) ---
    try: 
        audit_resumo.gerar_aba_resumo(writer)
    except Exception as e: 
        st.warning(f"Erro ao gerar Aba Resumo: {e}")

    # Abas de Auditoria Especialistas
    if not df_xs.empty:
        audit_icms.processar_icms(df_xs, writer, cod_cliente, df_xe, df_base_emp, modo)
        
        try: audit_ipi.processar_ipi(df_xs, writer, cod_cliente)
        except Exception as e: st.warning(f"IPI: {e}")
        
        try: audit_pis_cofins.processar_pc(df_xs, writer, cod_cliente, regime)
        except Exception as e: st.warning(f"PIS/COFINS: {e}")
        
        try: audit_difal.processar_difal(df_xs, writer)
        except: pass
        
        try: apuracao_difal.gerar_resumo_uf(df_xs, writer, df_xe)
        except: pass

    # Abas de Conferência (Dumps XML) - No final
    for df_temp, nome in [(df_xe, 'ENTRADAS_XML'), (df_xs, 'SAIDAS_XML')]:
        if not df_temp.empty:
            df_temp.to_excel(writer, sheet_name=nome, index=False)
