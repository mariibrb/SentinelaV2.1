import streamlit as st
import os, io, pandas as pd
import requests
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")

# --- INJEÇÃO DA APARÊNCIA PREMIUM ---
aplicar_estilo_sentinela()

# --- FUNÇÃO PARA REINICIAR O APP ---
def reiniciar_aplicacao():
    for key in st.session_state.keys():
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

def verificar_arquivo_github(caminho_relativo):
    token = st.secrets.get("GITHUB_TOKEN")
    repo = st.secrets.get("GITHUB_REPO")
    if not token or not repo: return False
    
    # Criamos uma lista de possibilidades para garantir que o acento não atrapalhe
    possibilidades = [
        caminho_relativo, # Tenta com o nome original
        caminho_relativo.replace("Bases_Tributárias", "Bases_Tributarias"), # Tenta sem acento
        caminho_relativo.replace("Bases_Tributárias", "bases_tributarias")  # Tenta tudo minúsculo
    ]
    
    for path in possibilidades:
        url = f"https://api.github.com/repos/{repo.strip()}/contents/{path}"
        headers = {"Authorization": f"token {token}"}
        try:
            res = requests.get(url, headers=headers, timeout=5)
            if res.status_code == 200:
                return True
        except: continue
    return False

df_clientes = carregar_base_clientes()

# --- CABEÇALHO E BOTÃO REINICIAR ---
col_titulo, col_reset = st.columns([4, 1])

with col_titulo:
    st.markdown("<div class='titulo-principal'>SENTINELA 2.1 | Análise Tributária</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

with col_reset:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 REINICIAR TUDO", use_container_width=True):
        reiniciar_aplicacao()

# --- CORPO PRINCIPAL ---
col_a, col_b = st.columns([2, 1])

with col_a:
    st.markdown("### Passo 1: Seleção da Empresa")
    if not df_clientes.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_clientes.iterrows()]
        selecao = st.selectbox("Escolha a empresa para auditar", [""] + opcoes, label_visibility="collapsed", key="empresa_sel")
    else: 
        st.error("⚠️ Base de clientes não encontrada.")
        selecao = None

if selecao:
    cod_cliente = selecao.split(" - ")[0].strip()
    dados_empresa = df_clientes[df_clientes['CÓD'] == cod_cliente].iloc[0]
    cnpj_auditado = str(dados_empresa['CNPJ']).strip()

    with col_b:
        st.markdown("### Passo 2: Seleção de Regime")
        regime = st.selectbox("Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], label_visibility="collapsed", key="regime_sel")
        is_ret = st.toggle("Habilitar MG (RET)", key="ret_sel")

    st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b> {dados_empresa['RAZÃO SOCIAL']} | <b>CNPJ:</b> {cnpj_auditado}</div>", unsafe_allow_html=True)
    
    c1_stat, c2_stat = st.columns(2)
    # Buscando exatamente o nome da pasta com acento que está no seu GitHub
    path_base = f"Bases_Tributárias/{cod_cliente}-Bases_Tributarias.xlsx"
    
    if verificar_arquivo_github(path_base):
        with c1_stat: st.success("✅ Base de Impostos Localizada")
    else:
        with c1_stat: st.warning("⚠️ Base de Impostos não localizada")
    
    if is_ret:
        path_ret = f"RET/{cod_cliente}-RET_MG.xlsx"
        if verificar_arquivo_github(path_ret):
            with c2_stat: st.success("✅ Base RET Localizada")
        else:
            with c2_stat: st.warning("⚠️ Base RET não localizada")

    st.markdown("### Passo 3: Central de Arquivos")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("**📁 XML (ZIP)**")
        xmls = st.file_uploader("Upload de XMLs ou ZIP", type=['zip', 'xml'], accept_multiple_files=True, key="xml_up")

    with c2:
        st.markdown("**📥 Entradas**")
        ge = st.file_uploader("Gerencial Entradas (TXT/CSV)", type=['csv', 'xlsx', 'txt'], accept_multiple_files=True, key="ge")
        ae = st.file_uploader("Autenticidade Entradas (Excel)", type=['xlsx', 'csv'], accept_multiple_files=True, key="ae")

    with c3:
        st.markdown("**📤 Saídas**")
        gs = st.file_uploader("Gerencial Saídas (TXT/CSV)", type=['csv', 'xlsx', 'txt'], accept_multiple_files=True, key="gs")
        as_f = st.file_uploader("Autenticidade Saídas (Excel)", type=['xlsx', 'csv'], accept_multiple_files=True, key="as")

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("🚀 INICIAR ANÁLISE", key="btn_analise"):
            if xmls and regime:
                with st.spinner("O Sentinela 2.1 está auditando os dados..."):
                    try:
                        df_xe, df_xs = extrair_dados_xml_recursivo(xmls, cnpj_auditado)
                        output = io.BytesIO()
                        with pd.ExcelWriter(output, engine='openpyxl') as writer:
                            gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae, as_f, ge, gs)
                        
                        relat = output.getvalue()
                        st.markdown(f"""
                            <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; border-top: 5px solid #FF6F00; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; margin-top: 20px;">
                                <div style="font-size: 3rem; margin-bottom: 10px;">✅</div>
                                <h2 style="color: #FF6F00; margin: 0; font-weight: 800;">AUDITORIA CONCLUÍDA</h2>
                                <p style="color: #555; font-size: 1.1rem; margin-top: 10px;">
                                    Relatório gerado com sucesso para <b>{dados_empresa['RAZÃO SOCIAL']}</b>.
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.download_button("💾 BAIXAR RELATÓRIO FINAL", relat, f"Sentinela_{cod_cliente}_v2.1.xlsx", use_container_width=True, key="btn_download")
                    except Exception as e:
                        st.error(f"Erro no processamento: {e}")
            else:
                st.warning("⚠️ Verifique os XMLs e o Regime Fiscal.")
