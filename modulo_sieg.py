import streamlit as st
import requests
import base64
import zipfile
import io
import pandas as pd
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

def exibir_interface_sieg(cnpj_cliente):
    st.markdown("### ⚡ Integração Executiva SIEG")
    
    if not cnpj_cliente:
        st.warning("⚠️ Selecione uma empresa na barra lateral.")
        return

    with st.container(border=True):
        st.write(f"Conectado ao CNPJ: **{cnpj_cliente}**")
        c1, c2 = st.columns(2)
        with c1:
            data_ini = st.date_input("Início do Período", format="DD/MM/YYYY")
        with c2:
            data_fim = st.date_input("Fim do Período", format="DD/MM/YYYY")
        
        if st.button("🚀 SINCRONIZAR DADOS AGORA", use_container_width=True):
            puxar_dados_executivo(cnpj_cliente, data_ini, data_fim)

def puxar_dados_executivo(cnpj_selecionado, inicio, fim):
    api_key = st.secrets.get("SIEG_API_KEY")
    cnpj_busca = "".join(filter(str.isdigit, cnpj_selecionado))
    
    # Rota 1: A mais moderna para Hub (v3)
    # Rota 2: A clássica para download em lote
    # Rota 3: A de consulta AWS
    urls = [
        "https://api.sieg.com/hub/v3/nfe/xml",
        "https://api.sieg.com/api/Cofre/DownloadLote",
        "https://api.sieg.com/aws/nfe/consultar"
    ]

    headers = {
        "Content-Type": "application/json",
        "apikey": api_key,
        "Accept": "application/json"
    }

    payload = {
        "Cnpj": cnpj_busca,
        "DataInicio": inicio.strftime('%Y-%m-%d'),
        "DataFim": fim.strftime('%Y-%m-%d'),
        "TipoDocumento": "nfe",
        "IsEmissor": True # Busca as emitidas, como você faz no site
    }

    sucesso = False
    with st.spinner("⏳ Estabelecendo conexão segura com o Cofre..."):
        for url in urls:
            try:
                response = requests.post(url, json=payload, headers=headers, timeout=15)
                if response.status_code == 200:
                    dados = response.json()
                    # A API pode retornar 'xmls' (lista) ou 'Arquivo' (zip b64)
                    xmls_list = dados.get("xmls") or dados.get("Xmls")
                    arquivo_zip = dados.get("Arquivo") or dados.get("arquivo")

                    zip_buffer = io.BytesIO()
                    
                    if xmls_list:
                        with zipfile.ZipFile(zip_buffer, "w") as z:
                            for i, b in enumerate(xmls_list):
                                z.writestr(f"nota_{i}.xml", base64.b64decode(b))
                        sucesso = True
                    elif arquivo_zip:
                        zip_buffer = io.BytesIO(base64.b64decode(arquivo_zip))
                        sucesso = True
                    
                    if sucesso:
                        st.session_state['sieg_xmls_baixados'] = zip_buffer
                        st.success(f"✅ Conexão estável! Dados capturados da rota: {url.split('/')[-2]}")
                        st.rerun()
                        break
            except:
                continue

    if not sucesso:
        st.error("❌ O servidor da SIEG recusou a conexão automática.")
        st.info("💡 Como você é ADMIN, verifique no portal se a sua chave tem a permissão 'API HuB' ativa. Algumas contas Admin precisam habilitar isso manualmente por empresa.")

def processar_sieg_para_excel(cnpj_cliente):
    # Chama o motor que já existe no seu sentinela_core
    try:
        zip_memoria = st.session_state['sieg_xmls_baixados']
        zip_memoria.seek(0)
        xe, xs = extrair_dados_xml_recursivo([zip_memoria], cnpj_cliente)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            gerar_excel_final(xe, xs, cnpj_cliente, writer, "RELATORIO", False, None, None, None, "SIEG")
        st.balloons()
        st.download_button("💾 BAIXAR AUDITORIA COMPLETA", output.getvalue(), f"Auditoria_{cnpj_cliente}.xlsx", use_container_width=True)
    except Exception as e:
        st.error(f"Erro no motor: {e}")

if st.session_state.get('sieg_xmls_baixados'):
    st.markdown("---")
    if st.button("📊 GERAR RELATÓRIO EXECUTIVO", type="primary", use_container_width=True):
        processar_sieg_para_excel("CLIENTE")
