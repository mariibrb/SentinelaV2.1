import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    st.markdown("### ⚡ Conexão Administrativa SIEG")
    
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
        
        # Filtro de busca
        opcao = st.radio("Tipo de busca", ["Emitidas", "Recebidas"], horizontal=True)
        tipo_doc = st.selectbox("Documento", ["nfe", "cte", "nfse"], index=0)
        
        if st.button("🚀 PUXAR XMLS DIRETAMENTE", use_container_width=True):
            puxar_dados_admin(cnpj_cliente, data_ini, data_fim, tipo_doc, opcao)

def puxar_dados_admin(cnpj, inicio, fim, tipo, opcao):
    # Rota mestre para quem tem permissão total
    url = "https://api.sieg.com/hub/v2/nfe/xml"
    api_key = st.secrets.get("SIEG_API_KEY")
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))
    
    # Payload formatado para busca total no cofre
    payload = {
        "Cnpj": cnpj_limpo,
        "DataInicio": inicio.strftime('%Y%m%d'),
        "DataFim": fim.strftime('%Y%m%d'),
        "TipoDocumento": tipo,
        "IsEmissor": True if opcao == "Emitidas" else False,
        "RecuperarXmls": True # Este comando força a busca em todo o cofre
    }
    
    headers = {
        "Content-Type": "application/json", 
        "apikey": api_key
    }

    with st.spinner("⏳ Sincronizando com o Cofre Administrativo..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            # Se der 404, tentamos a última rota possível (AWS Cloud)
            if response.status_code == 404:
                url = "https://api.sieg.com/aws/nfe/consultar"
                payload["DataInicio"] = inicio.strftime('%Y-%m-%d')
                payload["DataFim"] = fim.strftime('%Y-%m-%d')
                response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                dados = response.json()
                xmls_list = dados.get("xmls") or dados.get("Xmls") or []
                
                if not xmls_list:
                    st.info(f"ℹ️ Conectado com sucesso, mas não há notas {'emitidas' if opcao == 'Emitidas' else 'recebidas'} neste período.")
                    return

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, xml_b64 in enumerate(xmls_list):
                        try:
                            z.writestr(f"sieg_{i}.xml", base64.b64decode(xml_b64))
                        except: continue
                
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.success(f"✅ {len(xmls_list)} notas localizadas!")
                st.rerun()
            else:
                st.error(f"Erro {response.status_code}: A SIEG não autorizou a requisição. Verifique se a Chave API está correta no Secrets.")
        except Exception as e:
            st.error(f"Erro técnico: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "Auditoria SIEG", False, None, None, None, "SIEG_API")
        st.balloons()
        st.download_button("💾 BAIXAR RELATÓRIO FINAL", output.getvalue(), f"Auditoria_SIEG_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro no motor: {e}")

if st.session_state.get('sieg_xmls_baixados'):
    st.markdown("---")
    if st.button("📊 GERAR RELATÓRIO AGORA", type="primary", use_container_width=True):
        # Como o cnpj_cliente vem da interface, precisamos garantir que ele exista aqui
        # Se estiver usando dentro do app principal, a variável já existe
        processar_sieg_para_excel(st.session_state.get('cnpj_atual_sieg', ''))
