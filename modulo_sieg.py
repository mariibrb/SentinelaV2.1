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
        st.write(f"Empresa: **{cnpj_cliente}**")
        c1, c2 = st.columns(2)
        with c1:
            data_ini = st.date_input("Início", format="DD/MM/YYYY")
        with c2:
            data_fim = st.date_input("Fim", format="DD/MM/YYYY")
        
        doc_tipo = st.selectbox("Documento", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 BUSCAR NO COFRE", use_container_width=True):
            puxar_xmls_da_api(cnpj_cliente, data_ini, data_fim, doc_tipo)

    if st.session_state.get('sieg_xmls_baixados'):
        st.markdown("---")
        if st.button("📊 GERAR RELATÓRIO AGORA", type="primary", use_container_width=True):
            processar_sieg_para_excel(cnpj_cliente)

def puxar_xmls_da_api(cnpj, inicio, fim, tipo):
    # Esta é a URL que as chaves novas do portal SIEG HuB mais utilizam
    url = "https://api.sieg.com/hub/v2/nfe/xml"
    api_key = st.secrets.get("SIEG_API_KEY")
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))

    payload = {
        "Cnpj": cnpj_limpo,
        "DataInicio": inicio.strftime('%Y%m%d'),
        "DataFim": fim.strftime('%Y%m%d'),
        "TipoDocumento": tipo
    }
    headers = {"Content-Type": "application/json", "apikey": api_key}

    with st.spinner("⏳ Acessando SIEG..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            # Se der 404, tentamos a rota alternativa de consulta
            if response.status_code == 404:
                url_alt = "https://api.sieg.com/aws/nfe/consultar"
                response = requests.post(url_alt, json=payload, headers=headers)

            if response.status_code == 200:
                dados = response.json()
                xmls_b64 = dados.get("xmls") or dados.get("Xmls") or []
                
                if not xmls_b64:
                    st.info("ℹ️ Nenhuma nota encontrada neste período.")
                    return

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, b in enumerate(xmls_b64):
                        z.writestr(f"sieg_{i}.xml", base64.b64decode(b))
                
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.rerun()
            else:
                st.error(f"Erro {response.status_code}: A SIEG não encontrou os dados. Verifique se há notas nesse mês.")
        except Exception as e:
            st.error(f"Erro de conexão: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "SIEG", False, None, None, None, "SIEG")
        st.balloons()
        st.download_button("💾 BAIXAR EXCEL", output.getvalue(), f"Auditoria_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro no motor: {e}")
