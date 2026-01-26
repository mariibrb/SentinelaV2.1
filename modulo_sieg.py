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
        
        # Agora o padrão é buscar o que o cliente EMITIU
        origem = st.radio("Origem das Notas", ["Emitidas (Saídas)", "Recebidas (Entradas)"], horizontal=True)
        doc_tipo = st.selectbox("Documento", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 BUSCAR NO COFRE", use_container_width=True):
            is_emissor = (origem == "Emitidas (Saídas)")
            puxar_xmls_da_api(cnpj_cliente, data_ini, data_fim, doc_tipo, is_emissor)

def puxar_xmls_da_api(cnpj, inicio, fim, tipo, emitidas):
    url = "https://api.sieg.com/hub/v2/nfe/xml"
    api_key = st.secrets.get("SIEG_API_KEY")
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))

    # O segredo está aqui: indicamos se o CNPJ é o EMISSOR ou o DESTINATÁRIO
    payload = {
        "Cnpj": cnpj_limpo,
        "DataInicio": inicio.strftime('%Y%m%d'),
        "DataFim": fim.strftime('%Y%m%d'),
        "TipoDocumento": tipo,
        "IsEmissor": emitidas # Se True, busca o que ele emitiu. Se False, o que recebeu.
    }
    
    headers = {"Content-Type": "application/json", "apikey": api_key}

    with st.spinner("⏳ Acessando Cofre e filtrando Emitidas..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                dados = response.json()
                xmls_b64 = dados.get("xmls") or dados.get("Xmls") or []
                
                if not xmls_b64:
                    st.info(f"ℹ️ Nenhuma nota encontrada como {'Emitente' if emitidas else 'Destinatário'}.")
                    return

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, b in enumerate(xmls_b64):
                        z.writestr(f"sieg_{i}.xml", base64.b64decode(b))
                
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.success(f"✅ {len(xmls_b64)} notas emitidas localizadas!")
                st.rerun()
            else:
                st.error(f"Erro {response.status_code}: Verifique se o CNPJ está ativo no Cofre SIEG.")
        except Exception as e:
            st.error(f"Erro de conexão: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "SIEG Cloud", False, None, None, None, "SIEG")
        st.balloons()
        st.download_button("💾 BAIXAR EXCEL AUDITADO", output.getvalue(), f"Auditoria_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro no motor: {e}")
