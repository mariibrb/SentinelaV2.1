import streamlit as st
import os
import io
import pandas as pd
import zipfile
import re
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from hashlib import sha256
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÕES DO SISTEMA ---
st.set_page_config(page_title="Sentinela 2.4.0", page_icon="🧡", layout="wide")
st.markdown("<style>.stAppHeader {display: none !important;} header {visibility: hidden !important;} footer {visibility: hidden !important;}</style>", unsafe_allow_html=True)
aplicar_estilo_sentinela()

if 'user_data' not in st.session_state: st.session_state['user_data'] = {"nome": "Mariana"} # Bypass login para teste
if 'modulo_atual' not in st.session_state: st.session_state['modulo_atual'] = "GARIMPEIRO"

# --- SIDEBAR (RESTAURADA E COMPLETA) ---
@st.cache_data(ttl=600)
def carregar_clientes():
    p = "Clientes Ativos.xlsx"
    return pd.read_excel(p) if os.path.exists(p) else pd.DataFrame()

df_cli = carregar_clientes()

with st.sidebar:
    # 1. LOGO (Busca em múltiplos caminhos)
    for logo_path in ["logo.png", "streamlit/logo.png", ".streamlit/logo.png"]:
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
            break
    
    st.markdown("---")
    st.write(f"👤 Olá, **{st.session_state['user_data']['nome']}**")
    
    # 2. CAMPOS ESSENCIAIS DE FILTRO
    emp_sel = st.selectbox("1. Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="main_emp")
    
    if emp_sel:
        reg_sel = st.selectbox("2. Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="main_reg")
        seg_sel = st.selectbox("3. Segmento", ["", "Comércio", "Indústria", "Equiparado"], key="main_seg")
        ret_sel = st.toggle("4. Habilitar MG (RET)", key="main_ret")
        
        cod_c = emp_sel.split(" - ")[0].strip()
        dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        
        # Container de Status Mariana
        st.markdown(f"""
            <div style="background-color: #f8f9fa; border-left: 5px solid #ff4b4b; padding: 15px; border-radius: 8px; margin: 15px 0;">
                <b>🔍 Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}<br>
                <b>CNPJ:</b> {dados_e['CNPJ']}
            </div>
        """, unsafe_allow_html=True)
        
        # 3. DOWNLOAD DE MODELOS (RESTORED)
        with st.popover("📥 Baixar Modelos Base", use_container_width=True):
            st.write("Acesso restrito para modelos GitHub")
            if st.text_input("Senha", type="password", key="p_model") == "Senhaforte@123":
                st.download_button("Planilha Modelo (.xlsx)", pd.DataFrame().to_csv(), "modelo_base.xlsx", use_container_width=True)

    st.markdown("---")
    if st.button("🚪 SAIR DO SISTEMA", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- ÁREA CENTRAL (NAVEGAÇÃO LIMPA) ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.4.0</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

if emp_sel:
    # BOTÕES SOMENTE TEXTO (SEM BOLINHA, CORAÇÃO OU FLOR)
    c1, c2, c3, c4 = st.columns(4)
    
    if c1.button("GARIMPEIRO", use_container_width=True, type="primary" if st.session_state['modulo_atual'] == "GARIMPEIRO" else "secondary"):
        st.session_state['modulo_atual'] = "GARIMPEIRO"; st.rerun()

    if c2.button("CONCILIADOR", use_container_width=True, type="primary" if st.session_state['modulo_atual'] == "CONCILIADOR" else "secondary"):
        st.session_state['modulo_atual'] = "CONCILIADOR"; st.rerun()

    if c3.button("AUDITOR", use_container_width=True, type="primary" if st.session_state['modulo_atual'] == "AUDITOR" else "secondary"):
        st.session_state['modulo_atual'] = "AUDITOR"; st.rerun()

    if c4.button("ESPELHO", use_container_width=True, type="primary" if st.session_state['modulo_atual'] == "ESPELHO" else "secondary"):
        st.session_state['modulo_atual'] = "ESPELHO"; st.rerun()

    mod = st.session_state['modulo_atual']
    st.markdown("---")

    # --- SETORES ---
    if mod == "GARIMPEIRO":
        st.markdown('<div id="modulo-xml"></div>', unsafe_allow_html=True)
        st.subheader("Auditoria de Origem (XML)")
        # ... lógica do azul ...

    elif mod == "CONCILIADOR":
        st.markdown('<div id="modulo-amarelo"></div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; padding: 60px; background: rgba(255, 215, 0, 0.1); border: 2px dashed #FFD700; border-radius: 30px;">
                <h1 style="font-size: 80px; margin-bottom: 0px;">🕵️‍♀️</h1>
                <h2 style="color: #B8860B; font-weight: 800;">OPERAÇÃO PENTE FINO</h2>
                <p style="font-size: 20px; color: #555;">
                    <b>Calma, Mariana!</b> Ninguém vai trocar NCM ou comer descrição de produto por aqui.<br>
                    Estamos treinando os robôs para o cruzamento <b>XML vs Domínio</b>.
                </p>
            </div>
        """, unsafe_allow_html=True)

    elif mod == "AUDITOR":
        st.markdown('<div id="modulo-conformidade"></div>', unsafe_allow_html=True)
        st.subheader("Auditoria de Escrituração (Domínio)")
        t_p, t_i, t_r = st.tabs(["💰 PIS/COFINS", "📊 ICMS/IPI", "🏨 RET"])
        # ... lógica do rosa ...

    elif mod == "ESPELHO":
        st.markdown('<div id="modulo-apuracao"></div>', unsafe_allow_html=True)
        st.subheader("Veredito Final (Livros Fiscais)")
        # ... lógica do verde ...
else:
    st.info("👈 Selecione uma empresa na barra lateral para carregar os setores.")
