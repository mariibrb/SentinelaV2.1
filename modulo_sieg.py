import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    st.markdown("### ⚡ Conexão API V2 - Sistema Externo SIEG")
    
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
        
        doc_tipo = st.selectbox("Tipo Documento", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 SINCRONIZAR VIA API V2", use_container_width=True):
            executar_chamada_v2(cnpj_cliente, data_ini, data_fim, doc_tipo)

def executar_chamada_v2(cnpj, inicio, fim, tipo):
    # Conforme sua nova documentação, a URL base para o HUB V2
    url = "https://api.sieg.com/hub/v2/nfe/xml"
    api_key = st.secrets.get("SIEG_API_KEY")
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))
    
    # Payload ajustado para a V2
    payload = {
        "Cnpj": cnpj_limpo,
        "DataInicio": inicio.strftime('%Y-%m-%d'),
        "DataFim": fim.strftime('%Y-%m-%d'),
        "TipoDocumento": tipo,
        "IsEmissor": True # Busca as emitidas, conforme sua necessidade
    }
    
    headers = {
        "Content-Type": "application/json",
        "apikey": api_key
    }

    with st.spinner("⏳ Consultando Sistema Externo SIEG..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                dados = response.json()
                # A V2 retorna uma lista de XMLs em base64 no campo 'xmls'
                xmls_list = dados.get("xmls") or dados.get("Xmls") or []
                
                if not xmls_list:
                    st.info("ℹ️ Nenhuma nota encontrada para este filtro.")
                    return

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, b in enumerate(xmls_list):
                        z.writestr(f"nota_{i}.xml", base64.b64decode(b))
                
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.success(f"✅ {len(xmls_list)} Notas Sincronizadas!")
                st.rerun()
            
            elif response.status_code == 404:
                st.error("❌ Erro 404: Endpoint ou Empresa não localizada.")
                st.info("💡 Como você é Admin, verifique se o CNPJ está habilitado em 'Sistemas Externos' no portal SIEG.")
            else:
                st.error(f"Erro {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Erro técnico: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "Auditoria", False, None, None, None, "SIEG_V2")
        
        st.balloons()
        st.download_button("💾 BAIXAR RELATÓRIO COMPLETO", output.getvalue(), f"Auditoria_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro no motor: {e}")

if st.session_state.get('sieg_xmls_baixados'):
    st.markdown("---")
    if st.button("📊 GERAR AUDITORIA EXECUTIVA", type="primary", use_container_width=True):
        processar_sieg_para_excel("CLIENTE")
