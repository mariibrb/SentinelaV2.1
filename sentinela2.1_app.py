import streamlit as st
import os
import io
import pandas as pd
import zipfile
import re
import sqlite3
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sentinela 2.4.0", page_icon="🧡", layout="wide")

# CSS PARA LOGO NO TOPO E MENU LIMPO
st.markdown("""
    <style>
    .stAppHeader {display: none !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    .block-container {padding-top: 1rem !important;}
    
    /* LOGO COLADA NO TOPO */
    [data-testid="stSidebar"] div.stImage {
        margin-top: -65px !important; 
        margin-bottom: -45px !important; 
        padding: 0px !important;
    }
    
    /* MENU RADIO HORIZONTAL SEM BOLINHAS NOS NOMES */
    div.row-widget.stRadio > div{flex-direction:row; justify-content: center; gap: 20px;}
    div.row-widget.stRadio label {
        background-color: #f0f2f6;
        padding: 8px 25px;
        border-radius: 8px;
        cursor: pointer;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

aplicar_estilo_sentinela()

# --- CARREGAMENTO DE CLIENTES ---
@st.cache_data(ttl=600)
def carregar_clientes():
    p_lista = ["Clientes Ativos.xlsx", ".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx"]
    for p in p_lista:
        if os.path.exists(p):
            try:
                df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except: continue
    return pd.DataFrame()

df_cli = carregar_clientes()
if 'v_ver' not in st.session_state: st.session_state['v_ver'] = 0

# --- SIDEBAR (RESTAURADA E SEM ERROS) ---
with st.sidebar:
    for logo_p in ["logo.png", "streamlit/logo.png", ".streamlit/logo.png"]:
        if os.path.exists(logo_p):
            st.image(logo_p, use_container_width=True)
            break
    st.markdown("---")
    
    if not df_cli.empty:
        emp_sel = st.selectbox("1. Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="f_emp")
    else:
        st.error("Lista de clientes não encontrada.")
        emp_sel = ""

    if emp_sel:
        reg_sel = st.selectbox("2. Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"])
        seg_sel = st.selectbox("3. Segmento", ["", "Comércio", "Indústria", "Equiparado"])
        ret_sel = st.toggle("4. Habilitar MG (RET)")
        
        cod_c = emp_sel.split(" - ")[0].strip()
        
        # MENSAGENS DE STATUS (CORRIGIDO: SEM DELTAGENERATOR)
        st.markdown("---")
        if os.path.exists(f"Bases_Tributarias/{cod_c}-Bases_Tributarias.xlsx"):
            st.success("💎 Modo Elite: Base Localizada")
        else:
            st.warning("🔍 Modo Cegas: Base não localizada")
            
        if ret_sel:
            if os.path.exists(f"RET/{cod_c}-RET_MG.xlsx"):
                st.success("💎 Modo Elite: Base RET Localizada")
            else:
                st.warning("🔍 Modo Cegas: Base RET não localizada")

        # BOTÃO DE MODELOS
        with st.popover("📥 Modelo Bases", use_container_width=True):
            if st.text_input("Senha", type="password", key="p_modelo") == "Senhaforte@123":
                st.download_button("Baixar Modelo", pd.DataFrame().to_csv(), "modelo.xlsx", use_container_width=True)

    st.markdown("---")
    if st.button("🚪 SAIR", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- ÁREA CENTRAL ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.4.0</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

if emp_sel:
    # SELETOR DE MÓDULO (NOMES PUROS)
    modulos = ["GARIMPEIRO", "CONCILIADOR", "AUDITOR", "ESPELHO"]
    modulo_atual = st.radio("Selecione o Estágio:", modulos, horizontal=True, label_visibility="collapsed")
    st.markdown("---")

    # --- SETORES COM IDENTIFICAÇÃO PARA O STYLE.PY ---
    if modulo_atual == "GARIMPEIRO":
        st.markdown('<div id="modulo-xml"></div>', unsafe_allow_html=True)
        st.subheader("Auditoria de Origem (XML)")
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 ZIP XML", accept_multiple_files=True, key=f"x_{st.session_state['v_ver']}")
        with c2: u_ae = st.file_uploader("📥 Autenticidade Entradas", key=f"ae_{st.session_state['v_ver']}")
        with c3: u_as = st.file_uploader("📤 Autenticidade Saídas", key=f"as_{st.session_state['v_ver']}")
        
        if st.button("🚀 INICIAR GARIMPEIRO", use_container_width=True):
            st.info("Iniciando motor...")

    elif modulo_atual == "CONCILIADOR":
        st.markdown('<div id="modulo-amarelo"></div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; padding: 60px; background: rgba(255, 215, 0, 0.1); border: 2px dashed #FFD700; border-radius: 30px;">
                <h1 style="font-size: 80px; margin-bottom: 0px;">🕵️‍♀️</h1>
                <h2 style="color: #B8860B; font-weight: 800;">OPERAÇÃO PENTE FINO</h2>
                <p style="font-size: 20px; color: #555;">Estamos treinando os robôs para o cruzamento <b>XML vs Domínio</b>.</p>
            </div>
        """, unsafe_allow_html=True)

    elif modulo_atual == "AUDITOR":
        st.markdown('<div id="modulo-conformidade"></div>', unsafe_allow_html=True)
        sub_aud = ["💰 PIS/COFINS", "📊 ICMS/IPI"]
        if ret_sel: sub_aud.insert(2, "🏨 RET")
        tabs = st.tabs(sub_aud)
        for i, tab_nome in enumerate(sub_aud):
            with tabs[i]:
                st.markdown(f"#### Auditoria {tab_nome}")
                st.button(f"🚀 Iniciar Cruzamento {tab_nome}", use_container_width=True)

    elif modulo_atual == "ESPELHO":
        st.markdown('<div id="modulo-apuracao"></div>', unsafe_allow_html=True)
        st.subheader("Espelho dos Livros Fiscais")

else:
    st.info("👈 Selecione a empresa na barra lateral para carregar os setores.")
