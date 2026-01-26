import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    st.markdown("### ⚡ Conexão Administrativa Especial")
    
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
        
        doc_tipo = st.selectbox("Documento", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 EXECUTAR SINCRONIZAÇÃO", use_container_width=True):
            executar_sincronizacao_admin(cnpj_cliente, data_ini, data_fim, doc_tipo)

def executar_sincronizacao_admin(cnpj, inicio, fim, tipo):
    api_key = st.secrets.get("SIEG_API_KEY")
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))
    
    # URL 3: Rota de download para administradores de contabilidade
    url = f"https://api.sieg.com/hub/v2/download/xml"

    payload = {
        "Cnpj": cnpj_limpo,
        "DataInicio": inicio.strftime('%Y%m%d'),
        "DataFim": fim.strftime('%Y%m%d'),
        "TipoDocumento": tipo
    }
    
    headers = {
        "Content-Type": "application/json", 
        "apikey": api_key
    }

    with st.spinner("⏳ Vasculhando servidores SIEG..."):
        try:
            # Forçamos o método POST para a rota de download
            response = requests.post(url, json=payload, headers=headers)
            
            # Se der 404, tentamos a última rota de contingência (V1)
            if response.status_code == 404:
                url_v1 = "https://api.sieg.com/hub/v1/download/xml"
                response = requests.post(url_v1, json=payload, headers=headers)

            if response.status_code == 200:
                dados = response.json()
                xmls_list = dados.get("xmls") or dados.get("Xmls") or []
                
                if not xmls_list:
                    st.info("ℹ️ Conexão estabelecida, mas nenhum XML encontrado.")
                    return

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, xml_b64 in enumerate(xmls_list):
                        z.writestr(f"sieg_{i}.xml", base64.b64decode(xml_b64))
                
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.success(f"✅ {len(xmls_list)} notas localizadas!")
                st.rerun()
            else:
                # Mostra o erro real para a gente entender o que a SIEG quer
                st.error(f"Erro {response.status_code}")
                st.write("Resposta do Servidor:", response.text)
                
        except Exception as e:
            st.error(f"Erro de conexão: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "Audit", False, None, None, None, "SIEG")
        st.download_button("💾 BAIXAR EXCEL", output.getvalue(), f"Auditoria_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro: {e}")

if st.session_state.get('sieg_xmls_baixados'):
    st.markdown("---")
    if st.button("📊 GERAR RELATÓRIO AGORA", type="primary", use_container_width=True):
         # Aqui pegamos o CNPJ do cliente que está selecionado na barra lateral do app mestre
         # Como o app mestre passa cnpj_limpo para exibir_interface_sieg,
         # vamos usar uma gambiarra temporária para o botão funcionar:
         processar_sieg_para_excel("CLIENTE")
