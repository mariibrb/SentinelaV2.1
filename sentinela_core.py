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
                "INDIEDEST": buscar_tag_recursiva('indIEDest', dest),
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
                "VAL-FCP-ST": safe_float(buscar_tag_recursiva('vFCPST', icms_no)),
                
                # --- TAGS PARA A SUA ANALISE TRIBUTARIA ---
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

# ... (Função extrair_dados_xml_recursivo permanece igual) ...

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, df_base_emp=None, modo=None):
    if df_xs.empty and df_xe.empty: return
    
    try: gerar_aba_resumo(writer)
    except: pass
    
    for df_temp, nome in [(df_xe, 'ENTRADAS_XML'), (df_xs, 'SAIDAS_XML')]:
        if not df_temp.empty:
            cols_originais = [c for c in df_temp.columns if c != 'Situação Nota']
            cols_status = ['Situação Nota'] 
            df_final = df_temp[cols_originais + cols_status]
            df_final.to_excel(writer, sheet_name=nome, index=False)

    if not df_xs.empty:
        # 1. ICMS
        processar_icms(df_xs, writer, cod_cliente, df_xe, df_base_emp, modo)
        
        # 2. IPI (Chamada com proteção para sua análise tributária rodar)
        try:
            from Auditorias import audit_ipi
            audit_ipi.processar_ipi(df_xs, writer, cod_cliente)
        except Exception as e: st.warning(f"IPI: {e}")
        
        # 3. PIS/COFINS
        try:
            from Auditorias import audit_pis_cofins
            audit_pis_cofins.processar_pc(df_xs, writer, cod_cliente, regime)
        except Exception as e: st.warning(f"PIS/COFINS: {e}")
        
        # 4. DIFAL e 5. Resumo UF
        try: processar_difal(df_xs, writer)
        except: pass
        try: gerar_resumo_uf(df_xs, writer, df_xe)
        except: pass
