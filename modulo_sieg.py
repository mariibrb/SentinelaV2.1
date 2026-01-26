# modulo_sieg.py
import streamlit as st

def exibir_interface_sieg(cnpj_cliente):
    st.markdown('<div id="modulo-sieg"></div>', unsafe_allow_html=True)
    st.markdown(f"### ⚡ Conexão Direta SIEG API")
    st.write(f"CNPJ em análise: {cnpj_cliente}")
    
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.date_input("Período Inicial", key="sieg_inicio")
        with c2:
            st.date_input("Período Final", key="sieg_fim")
        
        st.multiselect("Documentos para Baixar", ["NF-e", "CT-e", "NFC-e"], default=["NF-e"])
        
        if st.button("🚀 PUXAR XMLS DO SIEG", use_container_width=True):
            st.warning("⚠️ Aguardando integração da API Key para o CNPJ informado.")
