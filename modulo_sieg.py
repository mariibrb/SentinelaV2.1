import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    st.markdown("### ⚡ Download em Lote via API SIEG")
    
    if not cnpj_cliente:
        st.warning("⚠️ Selecione uma empresa na barra lateral.")
        return

    with st.container(border=True):
        st.write(f"Empresa: **{cnpj_cliente}**")
        c1, c2 = st.columns(2)
        with c1:
            data_ini = st.date_input("Data Inicial", format="DD/MM/YYYY")
        with c2:
            data_fim = st.date_input("Data Final", format="DD/MM/YYYY")
        
        # Conforme a documentação, definimos o tipo de documento
        doc_tipo = st.selectbox("Documento", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 BAIXAR PACOTE XML", use_container_width=True):
            executar_download_lote(cnpj_cliente, data_ini, data_fim, doc_tipo)

def executar_download_lote(cnpj, inicio, fim, tipo):
    api_key = st.secrets.get("SIEG_API_KEY")
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))
    
    # ENDPOINT OFICIAL DA DOCUMENTAÇÃO:
    url = "https://api.sieg.com/api/Cofre/DownloadLote"

    # ESTRUTURA EXATA DO JSON PEDIDA NO MANUAL:
    payload = {
        "Cnpj": cnpj_limpo,
        "DataInicio": inicio.strftime('%Y-%m-%d'),
        "DataFim": fim.strftime('%Y-%m-%d'),
        "TipoDocumento": tipo
    }
    
    # A documentação pede a apikey no Header
    headers = {
        "Content-Type": "application/json",
        "apikey": api_key
    }

    with st.spinner("⏳ Solicitando pacote de XMLs à SIEG..."):
        try:
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                # O retorno da API de Download em Lote é um JSON com o campo "Arquivo" em Base64
                dados = response.json()
                arquivo_b64 = dados.get("Arquivo") or dados.get("arquivo")
                
                if not arquivo_b64:
                    st.warning("ℹ️ A SIEG não encontrou arquivos para este período.")
                    return

                # O arquivo já vem como um ZIP em Base64
                zip_data = base64.b64decode(arquivo_b64)
                st.session_state['sieg_xmls_baixados'] = io.BytesIO(zip_data)
                
                st.success("✅ Pacote de XMLs baixado com sucesso!")
                st.rerun()
            elif response.status_code == 404:
                st.error("❌ Erro 404: O endereço de Download em Lote não foi encontrado no seu plano.")
            else:
                st.error(f"Erro {response.status_code}: {response.text}")
                
        except Exception as e:
            st.error(f"Erro de conexão: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        
        # O motor Garimpeiro que já temos no core processa o ZIP
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "Auditoria", False, None, None, None, "SIEG_API")
        
        st.balloons()
        st.download_button("💾 BAIXAR RELATÓRIO EXCEL", output.getvalue(), f"Sentinela_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro no processamento: {e}")

if st.session_state.get('sieg_xmls_baixados'):
    st.markdown("---")
    if st.button("📊 GERAR AUDITORIA COMPLETA", type="primary", use_container_width=True):
        processar_sieg_para_excel("CLIENTE")
