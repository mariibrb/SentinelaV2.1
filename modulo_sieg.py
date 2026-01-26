import streamlit as st
import requests
import base64
import zipfile
import io

def exibir_interface_sieg(cnpj_cliente):
    st.markdown('<div id="modulo-sieg"></div>', unsafe_allow_html=True)
    st.markdown("### ⚡ Conexão Direta Cofre HUB - SIEG")
    
    if not cnpj_cliente:
        st.warning("⚠️ Selecione uma empresa na barra lateral para prosseguir.")
        return

    with st.container(border=True):
        st.write(f"Analisando via API: **{cnpj_cliente}**")
        c1, c2 = st.columns(2)
        with c1:
            data_ini = st.date_input("Data Inicial", format="DD/MM/YYYY")
        with c2:
            data_fim = st.date_input("Data Final", format="DD/MM/YYYY")
        
        docs = st.multiselect("Documentos", ["nfe", "cte", "nfse"], default=["nfe"])
        
        if st.button("🚀 PUXAR XMLS DO COFRE", use_container_width=True):
            puxar_dados_api(cnpj_cliente, data_ini, data_fim, docs)

def puxar_dados_api(cnpj, inicio, fim, tipos):
    # Endpoint padrão do SIEG HUB
    url = "https://api.sieg.com/hub/v2/nfe/xml" 
    api_key = st.secrets.get("SIEG_API_KEY", "CHAVE_NAO_CONFIGURADA")
    
    headers = {
        "Content-Type": "application/json",
        "apikey": api_key
    }
    
    # Formatação das datas para o padrão da API (YYYYMMDD)
    data_sieg_ini = inicio.strftime('%Y%m%d')
    data_sieg_fim = fim.strftime('%Y%m%d')

    payload = {
        "Cnpj": cnpj,
        "DataInicio": data_sieg_ini,
        "DataFim": data_sieg_fim,
        "TipoDocumento": tipos[0] # Simplificado para o primeiro tipo selecionado
    }

    with st.spinner("⏳ Solicitando pacotes ao Cofre HUB..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                dados = response.json()
                # O SIEG geralmente retorna uma lista de XMLs em Base64
                xmls_base64 = dados.get("Xmls", [])
                
                if not xmls_base64:
                    st.info("ℹ️ Nenhum arquivo encontrado para este período no Cofre.")
                    return

                st.success(f"✅ {len(xmls_base64)} arquivos localizados!")
                
                # Criamos um ZIP na memória para simular o comportamento do seu "Garimpeiro"
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, xml_b64 in enumerate(xmls_base64):
                        xml_content = base64.b64decode(xml_b64)
                        z.writestr(f"documento_{i}.xml", xml_content)
                
                # Aqui guardamos no session_state para o Motor Garimpeiro ler
                st.session_state['sieg_zip'] = zip_buffer.getvalue()
                st.info("📦 Dados prontos. Volte à aba GARIMPEIRO ou processe aqui mesmo.")
                
            else:
                st.error(f"❌ Erro na API SIEG: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"💥 Erro de Conexão: {e}")
