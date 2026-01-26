import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    # ID para o CSS aplicar o Azul Escuro (Style.py)
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
        
        # O SIEG HuB trabalha melhor com esses tipos minúsculos
        doc_tipo = st.selectbox("Tipo de Documento", ["nfe", "cte", "nfse", "nfce"], index=0)
        
        if st.button("🚀 PUXAR DADOS DO COFRE", use_container_width=True):
            puxar_xmls_da_api(cnpj_cliente, data_ini, data_fim, doc_tipo)

    # SE OS DADOS FORAM BAIXADOS, MOSTRA O PROCESSAMENTO FINAL
    if st.session_state.get('sieg_xmls_baixados'):
        st.markdown("---")
        st.success(f"📦 Arquivos em memória prontos para auditoria.")
        
        if st.button("📊 GERAR RELATÓRIO AUDITADO", type="primary", use_container_width=True):
            processar_sieg_para_excel(cnpj_cliente)

def puxar_xmls_da_api(cnpj, inicio, fim, tipo):
    # Testaremos a URL de consulta de pacotes que é a mais robusta
    url = "https://api.sieg.com/aws/nfe/consultar" 
    api_key = st.secrets.get("SIEG_API_KEY")
    
    if not api_key:
        st.error("❌ API Key não configurada nos Secrets do Streamlit!")
        return

    # Limpa o CNPJ para deixar apenas números
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))

    # Payload formatado conforme a documentação técnica da SIEG para o HuB
    payload = {
        "Cnpj": cnpj_limpo,
        "DataInicio": inicio.strftime('%Y-%m-%d'),
        "DataFim": fim.strftime('%Y-%m-%d'),
        "TipoDocumento": tipo
    }
    
    headers = {
        "Content-Type": "application/json", 
        "apikey": api_key
    }

    with st.spinner("⏳ Conectando ao cofre da SIEG..."):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            # Se a primeira URL der 404, tentamos a URL de download direto
            if response.status_code == 404:
                url_alt = "https://api.sieg.com/hub/v2/nfe/xml"
                response = requests.post(url_alt, json=payload, headers=headers)

            if response.status_code == 200:
                dados = response.json()
                # O SIEG pode retornar 'xmls' ou 'Xmls'
                xmls_b64 = dados.get("xmls") or dados.get("Xmls") or []
                
                if not xmls_b64:
                    st.info("ℹ️ Nenhum arquivo encontrado para este período no Cofre.")
                    return

                # Criamos o ZIP em memória (virtual)
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as z:
                    for i, b in enumerate(xmls_b64):
                        try:
                            z.writestr(f"sieg_{i}.xml", base64.b64decode(b))
                        except:
                            continue
                
                # Guarda o ZIP na memória da sessão
                st.session_state['sieg_xmls_baixados'] = zip_buffer
                st.rerun()
            else:
                st.error(f"❌ Erro API: {response.status_code} - Verifique se a Chave API tem permissão para o HuB.")
        except Exception as e:
            st.error(f"💥 Falha técnica na conexão: {e}")

def processar_sieg_para_excel(cnpj_cliente):
    with st.spinner("🚀 Motor Sentinela processando dados da nuvem..."):
        try:
            # Recupera os dados baixados da memória
            zip_memoria = st.session_state['sieg_xmls_baixados']
            zip_memoria.seek(0)
            
            # Executa o motor de extração (xe = entradas, xs = saídas)
            xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
            
            # Prepara o buffer para o Excel
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                # Chama a função mestre de geração de relatório do sentinela_core
                gerar_excel_final(xe, xs, cnpj_cliente, writer, "Regime SIEG", False, None, None, None, "SIEG_CLOUD")
            
            st.session_state['sieg_relatorio_final'] = output.getvalue()
            st.balloons()
            st.download_button(
                label="💾 BAIXAR RELATÓRIO AUDITADO (SIEG)", 
                data=output.getvalue(), 
                file_name=f"Auditoria_SIEG_{cnpj_cliente}.xlsx", 
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Erro no processamento do motor: {e}")
