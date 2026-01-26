import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    st.markdown('<div id="modulo-sieg"></div>', unsafe_allow_html=True)
    st.markdown("### ⚡ Busca Global Cofre HUB - SIEG")
    
    if not cnpj_cliente:
        st.warning("⚠️ Selecione uma empresa na barra lateral.")
        return

    with st.container(border=True):
        st.write(f"🔍 Buscando notas para o CNPJ: **{cnpj_cliente}**")
        
        c1, c2 = st.columns(2)
        with c1:
            data_ini = st.date_input("Início", format="DD/MM/YYYY")
        with c2:
            data_fim = st.date_input("Fim", format="DD/MM/YYYY")
        
        # Simulando a sua busca manual: busca o CNPJ em todas as pastas
        tipo_doc = st.selectbox("Tipo", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 EXECUTAR BUSCA NO COFRE", use_container_width=True):
            executar_busca_global(cnpj_cliente, data_ini, data_fim, tipo_doc)

def executar_busca_global(cnpj_selecionado, inicio, fim, tipo):
    # Rota de consulta por filtro (é a que simula "digitar o cnpj" na busca)
    url = "https://api.sieg.com/aws/nfe/consultar"
    api_key = st.secrets.get("SIEG_API_KEY")
    
    # Limpamos o CNPJ (apenas números)
    cnpj_busca = "".join(filter(str.isdigit, cnpj_selecionado))

    # Montamos o pedido exatamente como a busca do site
    payload = {
        "Cnpj": cnpj_busca,
        "DataInicio": inicio.strftime('%Y-%m-%d'),
        "DataFim": fim.strftime('%Y-%m-%d'),
        "TipoDocumento": tipo,
        "MetodoBusca": "Cnpj" # AQUI está o segredo: ele busca o CNPJ em todo o cofre
    }
    
    headers = {
        "Content-Type": "application/json", 
        "apikey": api_key
    }

    with st.spinner(f"⏳ Vasculhando pastas do Cofre por {cnpj_busca}..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            # Se a busca global der 404, tentamos a rota de XML direto
            if response.status_code == 404:
                url_xml = "https://api.sieg.com/hub/v2/nfe/xml"
                response = requests.post(url_xml, json=payload, headers=headers)

            if response.status_code == 200:
                dados = response.json()
                xmls_b64 = dados.get("xmls") or dados.get("Xmls") or []
                
                if not xmls_b64:
                    st.warning("ℹ️ O CNPJ foi aceito, mas não há arquivos nesse período.")
                    return

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, b in enumerate(xmls_b64):
                        z.writestr(f"sieg_{i}.xml", base64.b64decode(b))
                
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.success(f"✅ Sucesso! {len(xmls_b64)} notas encontradas.")
                st.rerun()
            else:
                st.error(f"❌ Erro {response.status_code}: A SIEG não autorizou a busca global.")
                st.info("Isso pode significar que o CNPJ do cliente precisa ser 'vinculado' ao seu Token.")
        except Exception as e:
            st.error(f"💥 Erro técnico: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    # (Mantém a mesma lógica de processamento anterior)
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "SIEG", False, None, None, None, "SIEG")
        st.download_button("💾 BAIXAR EXCEL", output.getvalue(), f"Auditoria_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro: {e}")
