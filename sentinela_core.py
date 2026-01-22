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
            prod = det.find('prod'); imp = det.find('imposto')
            icms_no = det.find('.//ICMS'); ipi_no = det.find('.//IPI')
            pis_no = det.find('.//PIS'); cof_no = det.find('.//COFINS')
            
            origem = buscar_tag_recursiva('orig', icms_no)
            cst_parcial = buscar_tag_recursiva('CST', icms_no) or buscar_tag_recursiva('CSOSN', icms_no)
            cst_full = origem + cst_parcial if cst_parcial else origem

            linha = {
                "TIPO_SISTEMA": tipo_operacao,
                "CHAVE_ACESSO": str(chave).strip(),
                "NUM_NF": buscar_tag_recursiva('nNF', ide),
                "DATA_EMISSAO": buscar_tag_recursiva('dhEmi', ide) or buscar_tag_recursiva('dEmi', ide),
                "CNPJ_EMIT": cnpj_emit,
                "UF_EMIT": buscar_tag_recursiva('UF', emit),
                "CNPJ_DEST": re.sub(r'\D', '', buscar_tag_recursiva('CNPJ', dest)),
                "IE_DEST": buscar_tag_recursiva('IE', dest),
                "UF_DEST": buscar_tag_recursiva('UF', dest),
                "CFOP": buscar_tag_recursiva('CFOP', prod),
                "NCM": buscar_tag_recursiva('NCM', prod),
                "VPROD": safe_float(buscar_tag_recursiva('vProd', prod)),
                "BC-ICMS": safe_float(buscar_tag_recursiva('vBC', icms_no)),
                "ALQ-ICMS": safe_float(buscar_tag_recursiva('pICMS', icms_no)),
                "VLR-ICMS": safe_float(buscar_tag_recursiva('vICMS', icms_no)),
                "CST-ICMS": cst_full,
                "VAL-ICMS-ST": safe_float(buscar_tag_recursiva('vICMSST', icms_no)),
                "IE_SUBST": str(buscar_tag_recursiva('IEST', icms_no)).strip(),
                "VAL-DIFAL": safe_float(buscar_tag_recursiva('vICMSUFDest', imp)) + safe_float(buscar_tag_recursiva('vFCPUFDest', imp)),
                "VAL-FCP-DEST": safe_float(buscar_tag_recursiva('vFCPUFDest', imp)),
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),
                
                # Tags de tributos para os módulos especialistas
                "ALQ-IPI": safe_float(buscar_tag_recursiva('pIPI', ipi_no)),
                "VLR-IPI": safe_float(buscar_tag_recursiva('vIPI', ipi_no)),
                "CST-IPI": buscar_tag_recursiva('CST', ipi_no),
                "ALQ-PIS": safe_float(buscar_tag_recursiva('pPIS', pis_no)),
                "VLR-PIS": safe_float(buscar_tag_recursiva('vPIS', pis_no)),
                "ALQ-COFINS": safe_float(buscar_tag_recursiva('pCOFINS', cof_no)),
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

    # --- CORREÇÃO DA LEITURA DO STATUS (AUTENTICIDADE) ---
    if 'relatorio' in st.session_state and st.session_state['relatorio'] is not None:
        df_rel = pd.DataFrame(st.session_state['relatorio'])
        
        # Tentamos encontrar a coluna de Chave e Status independente do nome exato (Maiúsculo/Minúsculo)
        df_rel.columns = [c.strip().upper() for c in df_rel.columns]
        
        # Mapeia os nomes prováveis que vêm do seu Excel de Garimpo
        mapa_cols = {
            'CHAVE': 'CHAVE_ACESSO',
            'CHAVE DE ACESSO': 'CHAVE_ACESSO',
            'STATUS': 'SITUACAO_GARIMPO',
            'SITUAÇÃO': 'SITUACAO_GARIMPO'
        }
        df_rel = df_rel.rename(columns=mapa_cols)

        if 'CHAVE_ACESSO' in df_rel.columns:
            df = pd.merge(df, df_rel[['CHAVE_ACESSO', 'SITUACAO_GARIMPO']], on='CHAVE_ACESSO', how='left')
            df['Status'] = df['SITUACAO_GARIMPO'].fillna("SEM REFERÊNCIA (FAZER GARIMPO)")
            df.drop(columns=['SITUACAO_GARIMPO'], inplace=True)
        else:
            df['Status'] = "⚠️ COLUNA 'CHAVE' NÃO ENCONTRADA NO ANEXO"
    else:
        df['Status'] = "⚠️ ANEXO DE AUTENTICIDADE NÃO CARREGADO"

    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, ge=None, gs=None, df_base_emp=None, modo_auditoria=None):
    if df_xs.empty and df_xe.empty: return
    
    try: gerar_aba_resumo(writer)
    except: pass
    
    # Ordem de exibição final: Status por ÚLTIMO
    colunas_finais = [
        "TIPO_SISTEMA", "CHAVE_ACESSO", "NUM_NF", "DATA_EMISSAO", "CNPJ_EMIT", "UF_EMIT",
        "CNPJ_DEST", "IE_DEST", "UF_DEST", "CFOP", "NCM", "VPROD", "BC-ICMS", "ALQ-ICMS",
        "VLR-ICMS", "CST-ICMS", "VAL-ICMS-ST", "IE_SUBST", "VAL-DIFAL", "VAL-FCP-DEST",
        "VAL-FCP-ST", "Status"
    ]

    for df_temp, nome in [(df_xe, 'ENTRADAS_XML'), (df_xs, 'SAIDAS_XML')]:
        if not df_temp.empty:
            df_export = df_temp[colunas_finais].copy()
            df_export.to_excel(writer, sheet_name=nome, index=False)

    if not df_xs.empty:
        # Auditorias continuam lendo as tags extras (IPI, PIS, etc) que estão no DF
        processar_icms(df_xs, writer, cod_cliente, df_xe, df_base_emp, modo_auditoria)
        processar_ipi(df_xs, writer, cod_cliente)
        processar_pc(df_xs, writer, cod_cliente, regime)
        processar_difal(df_xs, writer)
        gerar_resumo_uf(df_xs, writer, df_xe)
        gerar_abas_gerenciais(writer, ae, as_f, ge, gs)
