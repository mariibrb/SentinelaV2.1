import streamlit as st
import os, io, pandas as pd
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO E ESTILO ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")
aplicar_estilo_sentinela()

# --- LÓGICA DE CONTROLE DE SESSÃO (EVITA keyboard_double) ---
if 'reset_v' not in st.session_state:
    st.session_state['reset_v'] = 0

def limpar_apenas_arquivos():
    st.session_state['reset_v'] += 1
    if 'relatorio_pronto' in st.session_state:
        st.session_state['relatorio_pronto'] = None
    st.rerun()

# --- CARREGAMENTO DE CLIENTES ---
@st.cache_data(ttl=600)
def carregar_clientes_locais():
    caminhos = [".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx", "Clientes Ativos.xlsx"]
    for p in caminhos:
        if os.path.exists(p):
            try:
                df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except: continue
    return pd.DataFrame()

df_cli = carregar_clientes_locais()
v = st.session_state['reset_v']

# --- SIDEBAR (PAINEL DE CONTROLE) ---
with st.sidebar:
    logo_p = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_p):
        st.image(logo_p, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🏢 Passo 1: Empresa")
    if not df_cli.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()]
        selecao = st.selectbox("Escolha a empresa", [""] + opcoes, key="sb_emp")
    else: selecao = None

    if selecao:
        st.markdown("### ⚖️ Passo 2: Regime")
        regime = st.selectbox("Escolha o Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="sb_reg")
        
        st.markdown("### 🏗️ Passo 3: Segmento")
        segmento = st.selectbox("Escolha o Segmento", ["", "Comércio (Não gera IPI)", "Indústria", "Equiparado à Indústria"], index=0, key="sb_seg")
        
        st.markdown("### 🛡️ Passo 4: RET")
        is_ret = st.toggle("Habilitar MG (RET)", key="sb_ret_flag")
        
        # --- BLOCO DE STATUS ---
        st.markdown("---")
        st.markdown("### 📊 Status da Conexão")
        cod_c = selecao.split(" - ")[0].strip()
        emp_d = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        
        st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{emp_d['RAZÃO SOCIAL']}<br><b>CNPJ:</b> {emp_d['CNPJ']}</div>", unsafe_allow_html=True)
        
        if os.path.exists(f"Bases_Tributárias/{cod_c}-Bases_Tributarias.xlsx"):
            st.success("✅ Base de Impostos Localizada")
        else: st.warning("⚠️ Base não localizada")
            
        if is_ret:
            if os.path.exists(f"RET/{cod_c}-RET_MG.xlsx"): st.success("✅ Base RET Localizada")
            else: st.warning("⚠️ Base RET não localizada")
        
        st.markdown("---")
        def gabarito_func():
            out = io.BytesIO()
            with pd.ExcelWriter(out, engine='xlsxwriter') as w:
                pd.DataFrame(columns=["NCM", "CST_ESPERADA", "ALQ_INTER", "CST_PC_ESPERADA", "CST_IPI_ESPERADA", "ALQ_IPI_ESPERADA"]).to_excel(w, index=False)
            return out.getvalue()
        
        st.download_button("📥 Modelo Bases", gabarito_func(), "modelo.xlsx", use_container_width=True, type="primary", key="sb_dl_mod")

# --- CABEÇALHO ---
c_t, c_r = st.columns([4, 1])
with c_t:
    st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 REINICIAR ARQUIVOS", use_container_width=True, key=f"btn_reset_{v}"):
        limpar_apenas_arquivos()

# --- CORPO PRINCIPAL ---
if selecao:
    st.markdown("### 📥 Passo 5: Central de Arquivos")
    c1, c2, c3 = st.columns(3)
    with c1: xmls = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True, key=f"xml_{v}")
    with c2: 
        ge = st.file_uploader("📥 Gerencial Entradas", accept_multiple_files=True, key=f"ge_{v}")
        ae = st.file_uploader("📥 Autenticidade Entradas", accept_multiple_files=True, key=f"ae_{v}")
    with c3:
        gs = st.file_uploader("📤 Gerencial Saídas", accept_multiple_files=True, key=f"gs_{v}")
        as_f = st.file_uploader("📤 Autenticidade Saídas", accept_multiple_files=True, key=f"as_{v}")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 INICIAR ANÁLISE", use_container_width=True, key=f"run_{v}"):
        if xmls and regime and segmento:
            with st.spinner("Realizando auditoria fiscal..."):
                try:
                    df_xe, df_xs = extrair_dados_xml_recursivo(xmls, str(emp_d['CNPJ']).strip())
                    buf = io.BytesIO()
                    with pd.ExcelWriter(buf, engine='openpyxl') as writer:
                        # Hierarquia fiscal e regras de agregação mantidas integralmente
                        gerar_excel_final(df_xe, df_xs, cod_c, writer, regime, is_ret, ae, as_f, ge, gs)
                    st.session_state['relatorio_pronto'] = buf.getvalue()
                except Exception as e: st.error(f"Erro no processamento: {e}")
        else: st.warning("⚠️ Selecione Regime, Segmento e carregue os XMLs.")

    if st.session_state.get('relatorio_pronto'):
        st.markdown("<div style='text-align: center; padding: 20px;'><h2>✅ AUDITORIA CONCLUÍDA</h2></div>", unsafe_allow_html=True)
        st.download_button("💾 BAIXAR RELATÓRIO FINAL", st.session_state['relatorio_pronto'], f"Sentinela_{cod_c}.xlsx", use_container_width=True, key=f"dl_fin_{v}")
else:
    st.info("👈 Utilize a barra lateral para configurar a empresa e as regras fiscais.")
