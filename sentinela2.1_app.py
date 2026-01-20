import streamlit as st
import os, io, pandas as pd
import requests
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")

# --- INJEÇÃO DA APARÊNCIA PREMIUM ---
aplicar_estilo_sentinela()

# --- FUNÇÃO PARA REINICIAR APENAS ARQUIVOS E RESULTADOS ---
def limpar_central_arquivos():
    # Chaves específicas da Central de Arquivos para evitar conflito com a Sidebar
    chaves_para_limpar = ["xml_up", "ge", "ae", "gs", "as", "btn_analise_final", "btn_download_final"]
    for key in chaves_para_limpar:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# --- FUNÇÕES DE SUPORTE ---
@st.cache_data(ttl=600)
def carregar_base_clientes():
    caminhos = [
        ".streamlit/Clientes Ativos.xlsx",
        "streamlit/Clientes Ativos.xlsx",
        "Clientes Ativos.xlsx"
    ]
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
    possibilidades = [
        f"Bases_Tributárias/{cod_cliente}-Bases_Tributarias.xlsx",
        f"Bases_Tributarias/{cod_cliente}-Bases_Tributarias.xlsx",
        f"bases_tributarias/{cod_cliente}-Bases_Tributarias.xlsx"
    ]
    for p in possibilidades:
        if os.path.exists(p):
            return p
    return None

df_clientes = carregar_base_clientes()

# --- SIDEBAR (PAINEL DE CONTROLE - DADOS PRESERVADOS) ---
with st.sidebar:
    logo_path = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🏢 Passo 1: Empresa")
    if not df_clientes.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_clientes.iterrows()]
        selecao = st.selectbox("Escolha a empresa", [""] + opcoes, key="sidebar_empresa_sel")
    else: 
        st.error("⚠️ Base de clientes não encontrada.")
        selecao = None

    if selecao:
        st.markdown("### ⚖️ Passo 2: Regime")
        regime = st.selectbox("Escolha o Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="sidebar_regime_sel")
        
        st.markdown("### 🏗️ Passo 3: Segmento")
        tipo_ipi = st.selectbox("Escolha o Segmento", ["", "Comércio (Não gera IPI)", "Indústria", "Equiparado à Indústria"], index=0, key="sidebar_segmento_sel")
        
        st.markdown("### 🛡️ Passo 4: RET")
        is_ret = st.toggle("Habilitar MG (RET)", value=False, key="sidebar_ret_toggle")
        
        # --- BLOCO DE STATUS ---
        st.markdown("---")
        st.markdown("### 📊 Status da Conexão")
        
        cod_cliente = selecao.split(" - ")[0].strip()
        dados_empresa = df_clientes[df_clientes['CÓD'] == cod_cliente].iloc[0]
        cnpj_auditado = str(dados_empresa['CNPJ']).strip()
        
        st.markdown(f"""
            <div class='status-container' style='margin-top:0px;'>
                📍 <b>Analisando:</b><br>{dados_empresa['RAZÃO SOCIAL']}<br>
                <b>CNPJ:</b> {cnpj_auditado}
            </div>
        """, unsafe_allow_html=True)
        
        caminho_base = localizar_base_dados(cod_cliente)
        if caminho_base:
            st.success("✅ Base de Impostos Localizada")
        else:
            st.warning("⚠️ Base de Impostos não localizada")
            
        if is_ret:
            path_ret = f"RET/{cod_cliente}-RET_MG.xlsx"
            if os.path.exists(path_ret):
                st.success("✅ Base RET Localizada")
            else:
                st.warning("⚠️ Base RET não localizada")
        
        st.markdown("---")
        def criar_gabarito():
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                pd.DataFrame(columns=["NCM", "CST_ESPERADA", "ALQ_INTER", "CST_PC_ESPERADA", "CST_IPI_ESPERADA", "ALQ_IPI_ESPERADA"]).to_excel(writer, sheet_name='GABARITO', index=False)
            return output.getvalue()
        
        st.download_button("📥 Modelo Bases", criar_gabarito(), "modelo_gabarito.xlsx", use_container_width=True, type="primary", key="sidebar_download_modelo")

# --- CABEÇALHO ---
col_titulo, col_reset = st.columns([4, 1])
with col_titulo:
    st.markdown("<div class='titulo-principal'>SENTINELA 2.1 | Análise Tributária</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with col_reset:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 REINICIAR ARQUIVOS", use_container_width=True, key="main_reset_btn"):
        limpar_central_arquivos()

# --- CORPO PRINCIPAL ---
if selecao:
    st.markdown("### 📥 Passo 5: Central de Arquivos")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**📁 XML (ZIP)**")
        xmls = st.file_uploader("Upload de XMLs", type=['zip', 'xml'], accept_multiple_files=True, key="xml_up")
    with c2:
        st.markdown("**📥 Entradas**")
        ge = st.file_uploader("Gerencial Entradas", type=['csv', 'xlsx', 'txt'], accept_multiple_files=True, key="ge")
        ae = st.file_uploader("Autenticidade Entradas", type=['xlsx', 'csv'], accept_multiple_files=True, key="ae")
    with c3:
        st.markdown("**📤 Saídas**")
        gs = st.file_uploader("Gerencial Saídas", type=['csv', 'xlsx', 'txt'], accept_multiple_files=True, key="gs")
        as_f = st.file_uploader("Autenticidade Saídas", type=['xlsx', 'csv'], accept_multiple_files=True, key="as")

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("🚀 INICIAR ANÁLISE", key="btn_analise_final"):
            if xmls and regime and tipo_ipi:
                with st.spinner("O Sentinela está auditando os dados..."):
                    try:
                        df_xe, df_xs = extrair_dados_xml_recursivo(xmls, cnpj_auditado)
                        output = io.BytesIO()
                        with pd.ExcelWriter(output, engine='openpyxl') as writer:
                            gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae, as_f, ge, gs)
                        relat = output.getvalue()
                        st.markdown(f"<div style='background-color: #ffffff; border-radius: 15px; padding: 25px; border-top: 5px solid #FF6F00; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; margin-top: 20px;'><h2 style='color: #FF6F00;'>AUDITORIA CONCLUÍDA</h2></div>", unsafe_allow_html=True)
                        st.download_button("💾 BAIXAR RELATÓRIO FINAL", relat, f"Sentinela_{cod_cliente}_v2.1.xlsx", use_container_width=True, key="btn_download_final")
                    except Exception as e:
                        st.error(f"Erro: {e}")
            else:
                st.warning("⚠️ Selecione o Regime Fiscal, o Segmento e carregue os XMLs.")
else:
    st.info("👈 Utilize a barra lateral para configurar a empresa e as regras fiscais.")
