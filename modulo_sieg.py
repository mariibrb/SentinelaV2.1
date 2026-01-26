import streamlit as st

def exibir_interface_sieg(cnpj_cliente):
    # O ID abaixo serve para o CSS saber que estamos na zona azul escura
    st.markdown('<div id="modulo-sieg"></div>', unsafe_allow_html=True)
    
    st.markdown("### ⚡ Conexão Direta Cofre HUB - SIEG")
    
    with st.container(border=True):
        st.write(f"Você está consultando dados para o CNPJ: **{cnpj_cliente}**")
        
        c1, c2 = st.columns(2)
        with c1:
            st.date_input("Início do Período", key="s_inicio")
        with c2:
            st.date_input("Fim do Período", key="s_fim")
        
        st.multiselect("Documentos Disponíveis no Cofre", 
                       ["NF-e", "CT-e", "NFC-e", "NFSe"], 
                       default=["NF-e"])
        
        if st.button("🚀 PUXAR DADOS DO COFRE HUB", use_container_width=True):
            st.info("Conectando à API da SIEG... Aguarde as credenciais de teste.")
