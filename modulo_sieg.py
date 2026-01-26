import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    st.markdown('<div id="modulo-sieg"></div>', unsafe_allow_html=True)
    st.markdown("### ⚡ Conexão Direta Cofre HUB - SIEG")
    
    if not cnpj_cliente:
        st.warning("⚠️ Selecione uma empresa na barra lateral para prosseguir.")
        return

    with st.container(border=True):
        st.write(f"Conectado ao CNPJ: **{cnpj_cliente}**")
        
        c1, c2 = st.columns(2)
        with c1:
            data_ini = st.date_input("Data Inicial", format="DD/MM/YYYY")
        with c2:
            data_fim = st.date_input("Data Final", format="DD/MM/YYYY")
        
        doc_tipo = st.selectbox("Tipo de Documento", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 PUXAR DADOS DO COFRE", use_container_width=True):
            puxar_xmls_da_api(cnpj_cliente, data_ini, data_fim, doc_tipo)

    # SE OS DADOS FORAM BAIXADOS, MOSTRA O PROCESSAMENTO FINAL
    if st.session_state.get('sieg_xmls_baixados'):
        st.markdown("---")
        st.success(f"📦 Arquivos em memória prontos para auditoria.")
        
        if st.button("📊 GERAR RELATÓRIO AUDITADO", type="primary", use_container_width=True):
            processar_sieg_para_excel(cnpj_cliente)

def puxar_xmls_da_api(cnpj, inicio, fim, tipo):
    url = "https://api.sieg.com/hub/v2/nfe/xml"
    api_key = st.secrets.get("SIEG_API_KEY")
    
    if not api_key:
        st.error("❌ API Key não configurada nos Secrets!")
        return

    payload = {
        "Cnpj": "".join(filter(str.isdigit, cnpj)),
        "DataInicio": inicio.strftime('%Y%m%d'),
        "DataFim": fim.strftime('%Y%m%d'),
        "TipoDocumento": tipo
    }
    headers = {"Content-Type": "application/json", "apikey": api_key}

    with st.spinner("⏳ Baixando do Cofre HUB..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                xmls_b64 = response.json().get("Xmls", [])
                if not xmls_b64:
                    st.info("ℹ️ Nenhum arquivo no período.")
                    return

                # Criamos o ZIP em memória
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, b in enumerate(xmls_b64):
                        z.writestr(f"sieg_{i}.xml", base64.b64decode(b))
                
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.rerun()
            else:
                st.error(f"Erro API: {response.status_code}")
        except Exception as e:
            st.error(f"Falha: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    with st.spinner("🚀 Motor Sentinela em ação..."):
        try:
            # Pegamos o ZIP que está guardado na memória
            zip_memoria = st.session_state['sieg_xmls_baixados']
            zip_memoria.seek(0)
            
            # Chamamos o seu motor original
            xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
            
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                # Usamos a sua função de gerar excel
                gerar_excel_final(xe, xs, cnpj_cliente, writer, "Não Informado", False, None, None, None, "SIEG")
            
            st.session_state['sieg_relatorio_final'] = output.getvalue()
            st.balloons()
            st.download_button("💾 BAIXAR RELATÓRIO SIEG", output.getvalue(), f"Auditoria_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
        except Exception as e:
            st.error(f"Erro no processamento: {e}")
