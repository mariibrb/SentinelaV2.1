import streamlit as st
import os
import io
import pandas as pd
import sqlite3
from style import aplicar_estilo_sentinela

# --- CONFIGURAÇÕES DE PÁGINA E CSS ---
st.set_page_config(page_title="Sentinela 2.4.0", page_icon="🧡", layout="wide")

st.markdown("""
    <style>
    .stAppHeader {display: none !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    .block-container {padding-top: 1rem !important;}
    
    /* AJUSTE DO ESPAÇO DA LOGO NO SIDEBAR */
    [data-testid="stSidebar"] div.stImage {
        margin-top: -65px !important; 
        margin-bottom: -45px !important; 
        padding: 0px !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.4rem !important; 
        padding-top: 0rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

aplicar_estilo_sentinela()

# --- CARREGAMENTO DE CLIENTES ---
@st.cache_data(ttl=600)
def carregar_clientes():
    p = "Clientes Ativos.xlsx"
    if os.path.exists(p):
        try:
            df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
            df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
            return df
        except:
            return pd.DataFrame()
    return pd.DataFrame()

df_cli = carregar_clientes()

if 'modulo_atual' not in st.session_state:
    st.session_state['modulo_atual'] = "GARIMPEIRO"

# --- SIDEBAR (LOGICAMENTE ESTRUTURADA) ---
with st.sidebar:
    # 1. LOGO
    for p in ["logo.png", "streamlit/logo.png"]:
        if os.path.exists(p):
            st.image(p, use_container_width=True)
            break
    
    st.markdown("---")
    
    # 2. SELEÇÃO DE EMPRESA
    if not df_cli.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()]
        emp_sel = st.selectbox("1. Empresa", [""] + opcoes, key="main_emp")
    else:
        st.error("Lista de clientes não encontrada.")
        emp_sel = ""

    if emp_sel:
        # 3. FILTROS TRIBUTÁRIOS
        reg_sel = st.selectbox("2. Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"])
        seg_sel = st.selectbox("3. Segmento", ["", "Comércio", "Indústria", "Equiparado"])
        
        st.markdown("---")
        
        # 4. LÓGICA DO RET (MENSAGEM DE BASE)
        ret_sel = st.toggle("4. Habilitar MG (RET)")
        
        if ret_sel:
            cod_c = emp_sel.split(" - ")[0].strip()
            # Verifica se existe a base de RET para a empresa
            path_ret = f"Bases_Tributarias/RET/{cod_c}-BaseRET.xlsx"
            
            if os.path.exists(path_ret):
                st.success("💎 Modo Elite: Base RET Localizada")
            else:
                st.warning("🔍 Modo Cegas: Base RET não localizada")

        # 5. STATUS DA ANÁLISE
        st.markdown(f"""
            <div style="background-color: #f8f9fa; border-left: 5px solid #ff4b4b; padding: 12px; border-radius: 8px; margin-top: 10px; font-size: 13px;">
                <b>🚀 Analisando:</b> {emp_sel.split(' - ')[1]}<br>
                <b>Analista:</b> Mariana
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # 6. BOTÃO DE MODELOS DE BASES (POPOVER COM SENHA)
        with st.popover("📥 Baixar Modelos de Bases", use_container_width=True):
            st.write("Área do Consultor: Modelos GitHub")
            senha_mod = st.text_input("Senha de Acesso", type="password", key="p_modelos")
            if senha_mod == "Senhaforte@123":
                st.download_button("Modelo Base Tributária", pd.DataFrame().to_csv(), "modelo_fiscal.xlsx", use_container_width=True)
                if ret_sel:
                    st.download_button("Modelo Base RET", pd.DataFrame().to_csv(), "modelo_ret.xlsx", use_container_width=True)
            elif senha_mod != "":
                st.error("Senha incorreta.")

    st.markdown("---")
    if st.button("🚪 SAIR", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- ÁREA CENTRAL (NAVEGAÇÃO LIMPA - SEM BOLINHAS) ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.4.0</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

if emp_sel:
    # BOTÕES SOMENTE TEXTO (AZUL, AMARELO, ROSA, VERDE)
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
        st.markdown("### 📥 Downloads")
        d1, d2, d3 = st.columns(3)
        d1.button("💾 Relatório de Análises", use_container_width=True)
        d2.button("📂 ZIP Separadinho", use_container_width=True)
        d3.button("📦 Download Completo", use_container_width=True)

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
        st.tabs(["💰 PIS/COFINS", "📊 ICMS/IPI", "🏨 RET", "⚖️ OUTROS"])

    elif mod == "ESPELHO":
        st.markdown('<div id="modulo-apuracao"></div>', unsafe_allow_html=True)
        st.subheader("Espelho dos Livros Fiscais (Veredito Final)")

else:
    st.info("👈 Selecione a empresa na barra lateral para começar.")
