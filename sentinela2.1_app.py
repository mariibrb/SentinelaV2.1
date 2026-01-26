import streamlit as st
import os
import io
import pandas as pd
import sqlite3
from style import aplicar_estilo_sentinela

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
    </style>
    """, unsafe_allow_html=True)

aplicar_estilo_sentinela()

# --- CARREGAMENTO DE CLIENTES ---
@st.cache_data(ttl=600)
def carregar_clientes():
    p = "Clientes Ativos.xlsx"
    if os.path.exists(p):
        df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
        df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
        return df
    return pd.DataFrame()

df_cli = carregar_clientes()

if 'modulo_atual' not in st.session_state:
    st.session_state['modulo_atual'] = "GARIMPEIRO"

# --- SIDEBAR OPERACIONAL ---
with st.sidebar:
    # 1. LOGO
    for logo_path in ["logo.png", "streamlit/logo.png", ".streamlit/logo.png"]:
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
            break
    
    st.markdown("---")
    
    if not df_cli.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()]
        emp_sel = st.selectbox("1. Empresa", [""] + opcoes, key="main_emp")
    else:
        st.error("Lista de clientes não carregada.")
        emp_sel = ""

    if emp_sel:
        # 2. FILTROS TRIBUTÁRIOS
        reg_sel = st.selectbox("2. Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"])
        seg_sel = st.selectbox("3. Segmento", ["", "Comércio", "Indústria", "Equiparado"])
        
        st.markdown("---")
        # 3. LÓGICA DO RET (MENSAGEM DE BASE)
        ret_sel = st.toggle("4. Habilitar MG (RET)")
        
        if ret_sel:
            # Aqui simulamos a busca pelo arquivo de base de RET
            cod_c = emp_sel.split(" - ")[0].strip()
            path_ret = f"Bases_RET/{cod_c}-BaseRET.xlsx" # Caminho onde ficam as bases de RET
            
            if os.path.exists(path_ret):
                st.success("💎 Modo Elite: Base RET Localizada")
            else:
                st.warning("🔍 Modo Cegas: Base RET não localizada")

        # 4. STATUS MARIANA
        dados_e = df_cli[df_cli['CÓD'] == emp_sel.split(" - ")[0].strip()].iloc[0]
        st.markdown(f"""
            <div style="background-color: #f8f9fa; border-left: 5px solid #ff4b4b; padding: 12px; border-radius: 8px; margin-top: 10px; font-size: 13px;">
                <b>🚀 Analisando:</b> {dados_e['RAZÃO SOCIAL']}<br>
                <b>CNPJ:</b> {dados_e['CNPJ']}
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        # 5. BOTAO DE MODELOS DE BASES (RESTAURADO)
        with st.popover("📥 Baixar Modelos de Bases", use_container_width=True):
            st.write("Área restrita: Modelos de auditoria")
            senha_mod = st.text_input("Senha de Acesso", type="password", key="p_modelos")
            if senha_mod == "Senhaforte@123":
                st.download_button("Modelo Base Tributária (.xlsx)", pd.DataFrame().to_csv(), "modelo_base_sentinela.xlsx", use_container_width=True)
                st.download_button("Modelo Base RET (.xlsx)", pd.DataFrame().to_csv(), "modelo_ret_sentinela.xlsx", use_container_width=True)
            elif senha_mod != "":
                st.error("Senha incorreta.")

    st.markdown("---")
    if st.button("🚪 SAIR", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- CONTEÚDO CENTRAL ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.4.0</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

if emp_sel:
    # NAVEGAÇÃO LIMPA (SÓ TEXTO)
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
        # Lógica de download
        st.markdown("### 📥 Resultados do Garimpeiro")
        d1, d2, d3 = st.columns(3)
        d1.button("💾 Relatório de Análises", use_container_width=True)
        d2.button("📂 ZIP Separadinho", use_container_width=True)
        d3.button("📦 Download Completo", use_container_width=True)

    elif mod == "CONCILIADOR":
        st.markdown('<div id="modulo-amarelo"></div>', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>🕵️‍♀️</h1><h3 style='text-align: center;'>Operação Pente Fino em Construção...</h3>", unsafe_allow_html=True)

    elif mod == "AUDITOR":
        st.markdown('<div id="modulo-conformidade"></div>', unsafe_allow_html=True)
        st.subheader("Auditoria de Escrituração (Domínio)")
        st.tabs(["💰 PIS/COFINS", "📊 ICMS/IPI", "🏨 RET", "⚖️ OUTROS"])

    elif mod == "ESPELHO":
        st.markdown('<div id="modulo-apuracao"></div>', unsafe_allow_html=True)
        st.subheader("Espelho dos Livros Fiscais")

else:
    st.info("👈 Selecione a empresa na barra lateral para começar.")
