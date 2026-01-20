import streamlit as st
import os, io, pandas as pd
import requests
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")

# --- INJEÇÃO DA APARÊNCIA PREMIUM ---
aplicar_estilo_sentinela()

# --- LÓGICA DE CONTROLE DE SESSÃO (EVITA DUPLICIDADE) ---
if 'versao_arquivos' not in st.session_state:
    st.session_state['versao_arquivos'] = 0

def limpar_central_arquivos():
    # Aumentar a versão força o Streamlit a recriar os uploaders com IDs novos, limpando-os
    st.session_state['versao_arquivos'] += 1
    # Limpa o resultado da análise anterior
    if 'analise_concluida' in st.session_state:
        st.session_state['analise_concluida'] = None
    st.rerun()

# --- FUNÇÕES DE SUPORTE ---
@st.cache_data(ttl=600)
def carregar_base_clientes():
    caminhos = [".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx", "Clientes Ativos.xlsx"]
    for caminho in caminhos:
        if os.path.exists(caminho):
            try:
                df = pd.read_excel(caminho)
                df = df.dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except: continue
    return pd.DataFrame()

def localizar_base_dados(cod_cliente):
    possibilidades = [f"Bases_Tributárias/{cod_cliente}-Bases_Tributarias.xlsx", f"Bases_Tributarias/{cod_cliente}-Bases_Tributarias.xlsx"]
    for p in possibilidades:
        if os.path.exists(p): return p
    return None

df_clientes = carregar_base_clientes()

# --- SIDEBAR (DADOS PRESERVADOS COM KEYS FIXAS) ---
with st.sidebar:
    logo_path = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🏢 Passo 1: Empresa")
    if not df_clientes.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_clientes.iterrows()]
        selecao = st.selectbox("Escolha a empresa", [""] + opcoes, key="fixa_empresa")
    else: 
        st.error("⚠️ Base de clientes não encontrada.")
        selecao = None

    if selecao:
        st.markdown("### ⚖️ Passo 2: Regime")
        regime = st.selectbox("Escolha o Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="fixa_regime")
        
        st.markdown("### 🏗️ Passo 3: Segmento")
        tipo_ipi = st.selectbox("Escolha o Segmento", ["", "Comércio (Não gera IPI)", "Indústria", "Equiparado à Indústria"], key="fixa_segmento")
        
        st.markdown("### 🛡️ Passo 4: RET")
        is_ret = st.toggle("Habilitar MG (RET)", key="fixa_ret")
        
        st.markdown("---")
        st.markdown("### 📊 Status da Conexão")
        cod_cliente = selecao.split(" - ")[0].strip()
        dados_empresa = df_clientes[df_clientes['CÓD'] == cod_cliente].iloc[0]
        st.markdown(f"<div class='status-container' style='margin-top:0px;'>📍 <b>Analisando:</b><br>{dados_empresa['RAZÃO SOCIAL']}<br><b>CNPJ:</b> {dados_empresa['CNPJ']}</div>", unsafe_allow_html=True)
        
        if localizar_base_dados(cod_cliente): st.success("✅ Base Localizada")
        else: st.warning("⚠️ Base não localizada")
        
        if is_ret:
            if os.path.exists(f"RET/{cod_cliente}-RET_MG.xlsx"): st.success("✅ Base RET Localizada")
            else: st.warning("⚠️ Base RET não localizada")
        
        st.markdown("---")
        def criar_gabarito():
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                pd.DataFrame(columns=["NCM", "CST_ESPERADA", "ALQ_INTER", "CST_PC_ESPERADA", "CST_IPI_ESPERADA", "ALQ_IPI_ESPERADA"]).to_excel(writer, sheet_name='GABARITO', index=False)
            return output.getvalue()
        
        st.download_button("📥 Modelo Bases", criar_gabarito(), "modelo_gabarito.xlsx", use_container_width=True, type="primary", key="fixa_btn_mdl")

# --- CABEÇALHO ---
col_t, col_r = st.columns([4, 1])
with col_t:
    st.markdown("<div class='titulo-principal'>SENTINELA 2.1 | Análise Tributária</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with col_r:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 REINICIAR ARQUIVOS", use_container_width=True, key="fixa_btn_reset"):
        limpar_central_arquivos()

# --- CORPO PRINCIPAL (KEYS DINÂMICAS PARA EVITAR keyboard_double) ---
v = st.session_state['versao_arquivos']

if selecao:
    st.markdown("### 📥 Passo 5: Central de Arquivos")
    c1, c2, c3 = st.columns(3)
    with c1:
        xmls = st.file_uploader("📁 XML (ZIP)", type=['zip', 'xml'], accept_multiple_files=True, key=f"xml_up_{v}")
    with c2:
        ge = st.file_uploader("📥 Gerencial Entradas", type=['csv', 'xlsx', 'txt'], accept_multiple_files=True, key=f"ge_{v}")
        ae = st.file_uploader("📥 Autenticidade Entradas", type=['xlsx', 'csv'], accept_multiple_files=True, key=f"ae_{v}")
    with c3:
        gs = st.file_uploader("📤 Gerencial Saídas", type=['csv', 'xlsx', 'txt'], accept_multiple_files=True, key=f"gs_{v}")
        as_f = st.file_uploader("📤 Autenticidade Saídas", type=['xlsx', 'csv'], accept_multiple_files=True, key=f"as_{v}")

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("🚀 INICIAR ANÁLISE", key=f"btn_run_{v}"):
            if xmls and regime and tipo_ipi:
                with st.spinner("Analisando..."):
                    try:
                        df_xe, df_xs = extrair_dados_xml_recursivo(xmls, str(dados_empresa['CNPJ']).strip())
                        output = io.BytesIO()
                        with pd.ExcelWriter(output, engine='openpyxl') as writer:
                            gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae, as_f, ge, gs)
                        st.session_state['analise_concluida'] = output.getvalue()
                    except Exception as e: st.error(f"Erro: {e}")
            else: st.warning("⚠️ Preencha todos os campos antes de iniciar.")

    if st.session_state.get('analise_concluida'):
        st.markdown(f"<div style='background-color: #ffffff; border-radius: 15px; padding: 25px; border-top: 5px solid #FF6F00; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; margin-top: 20px;'><h2 style='color: #FF6F00;'>AUDITORIA CONCLUÍDA</h2></div>", unsafe_allow_html=True)
        st.download_button("💾 BAIXAR RELATÓRIO FINAL", st.session_state['analise_concluida'], f"Sentinela_{cod_cliente}_v2.1.xlsx", use_container_width=True, key=f"btn_dl_{v}")
else:
    st.info("👈 Utilize a barra lateral para configurar a empresa e as regras fiscais.")
