import streamlit as st
import os
import io
import pandas as pd
import zipfile
import re
import sqlite3
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(page_title="Sentinela 2.4.0", page_icon="🧡", layout="wide")

# CSS PARA AJUSTAR O ESPAÇO DA LOGO E LIMPAR O TOPO
st.markdown("""
    <style>
    .stAppHeader {display: none !important;}
    header {visibility: hidden !important;}
    .block-container {padding-top: 1rem !important;}
    
    /* AJUSTE DO ESPAÇO DA LOGO NO SIDEBAR */
    [data-testid="stSidebar"] div.stImage {
        margin-top: -65px !important; 
        margin-bottom: -40px !important; 
        padding: 0px !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.5rem !important; 
        padding-top: 0rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

aplicar_estilo_sentinela()

# --- CARREGAMENTO DE CLIENTES (RESTAURADO) ---
@st.cache_data(ttl=600)
def carregar_clientes():
    # Procura o arquivo em caminhos comuns
    caminhos = ["Clientes Ativos.xlsx", ".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx"]
    for p in caminhos:
        if os.path.exists(p):
            try:
                df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except: continue
    return pd.DataFrame()

df_cli = carregar_clientes()

# Session State para navegação
if 'modulo_atual' not in st.session_state:
    st.session_state['modulo_atual'] = "GARIMPEIRO"

# --- SIDEBAR OPERACIONAL ---
with st.sidebar:
    # Busca e exibe a Logo
    for logo_path in ["logo.png", "streamlit/logo.png", ".streamlit/logo.png"]:
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
            break
    
    st.markdown("---")
    
    # Lista de Empresas Restaurada
    if not df_cli.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()]
        emp_sel = st.selectbox("1. Empresa", [""] + opcoes, key="main_emp")
    else:
        st.error("Arquivo 'Clientes Ativos.xlsx' não encontrado.")
        emp_sel = ""

    if emp_sel:
        # Campos Essenciais
        reg_sel = st.selectbox("2. Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"])
        seg_sel = st.selectbox("3. Segmento", ["", "Comércio", "Indústria", "Equiparado"])
        ret_sel = st.toggle("4. Habilitar MG (RET)")
        
        # Caixa de Status Mariana
        cod_c = emp_sel.split(" - ")[0].strip()
        dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        st.markdown(f"""
            <div style="background-color: #f8f9fa; border-left: 5px solid #ff4b4b; padding: 12px; border-radius: 8px; margin-top: 10px; font-size: 13px;">
                <b>🔍 Analisando:</b> {dados_e['RAZÃO SOCIAL']}<br>
                <b>CNPJ:</b> {dados_e['CNPJ']}
            </div>
        """, unsafe_allow_html=True)
        
        # Download de Modelos
        with st.popover("📥 Baixar Modelos Base", use_container_width=True):
            if st.text_input("Senha", type="password", key="p_side") == "Senhaforte@123":
                st.download_button("Modelo Padrão (.xlsx)", pd.DataFrame().to_csv(), "modelo.xlsx")

    st.markdown("---")
    if st.button("🚪 SAIR", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- CONTEÚDO CENTRAL ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.4.0</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

if emp_sel:
    # BOTÕES SOMENTE TEXTO (Limpos conforme pedido)
    c1, c2, c3, c4 = st.columns(4)
    
    setores = ["GARIMPEIRO", "CONCILIADOR", "AUDITOR", "ESPELHO"]
    cols = [c1, c2, c3, c4]
    
    for i, setor in enumerate(setores):
        if cols[i].button(setor, use_container_width=True, 
                          type="primary" if st.session_state['modulo_atual'] == setor else "secondary"):
            st.session_state['modulo_atual'] = setor
            st.rerun()

    mod = st.session_state['modulo_atual']
    st.markdown("---")

    if mod == "GARIMPEIRO":
        st.markdown('<div id="modulo-xml"></div>', unsafe_allow_html=True)
        st.subheader("Auditoria de Origem (XML)")
        # Área de Uploads
        ca, cb = st.columns(2)
        u_xml = ca.file_uploader("ZIP de XMLs", accept_multiple_files=True)
        u_sieg = cb.file_uploader("Autenticidade SIEG")
        
        if st.button("🚀 INICIAR GARIMPEIRO", use_container_width=True):
            st.toast("Processando...")

    elif mod == "CONCILIADOR":
        st.markdown('<div id="modulo-amarelo"></div>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center;'>🕵️‍♀️ OPERAÇÃO PENTE FINO</h2>", unsafe_allow_html=True)
        st.info("Módulo em construção: XML vs Domínio.")

    elif mod == "AUDITOR":
        st.markdown('<div id="modulo-conformidade"></div>', unsafe_allow_html=True)
        st.subheader("Auditoria de Escrituração (Domínio)")
        st.tabs(["💰 PIS/COFINS", "📊 ICMS/IPI", "🏨 RET"])

    elif mod == "ESPELHO":
        st.markdown('<div id="modulo-apuracao"></div>', unsafe_allow_html=True)
        st.subheader("Espelho dos Livros Fiscais")
        st.info("Aguardando auditoria...")

else:
    st.info("👈 Selecione a empresa na barra lateral para começar.")
