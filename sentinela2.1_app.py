import streamlit as st
import os, io, pandas as pd
import requests
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")

# --- INJEÇÃO DA APARÊNCIA PREMIUM ---
aplicar_estilo_sentinela()

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
    
    # Criamos uma lista de possíveis caminhos para a pasta de bases
    # Tentando com e sem acento, já que o GitHub diferencia
    possibilidades = [
        caminho_relativo,
        caminho_relativo.replace("Bases_Tributárias", "Bases_Tributarias"),
        caminho_relativo.replace("Bases_Tributárias", "bases_tributarias")
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

# --- SIDEBAR ---
with st.sidebar:
    logo_path = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    def criar_gabarito():
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            pd.DataFrame(columns=["NCM", "CST_ESPERADA", "ALQ_INTER", "CST_PC_ESPERADA", "CST_IPI_ESPERADA", "ALQ_IPI_ESPERADA"]).to_excel(writer, sheet_name='GABARITO', index=False)
        return output.getvalue()
    
    st.download_button("📥 Modelo Bases Tributárias", criar_gabarito(), "modelo_gabarito.xlsx", use_container_width=True)

# --- CORPO PRINCIPAL ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.1 | Análise Tributária</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

col_a, col_b = st.columns([2, 1])

with col_a:
    st.markdown("### Passo 1: Seleção da Empresa")
    if not df_clientes.empty:
        opcoes = [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_clientes.iterrows()]
        selecao = st.selectbox("Escolha a empresa para auditar", [""] + opcoes, label_visibility="collapsed")
    else: 
        st.error("⚠️ Base de clientes não encontrada.")
        selecao = None

if selecao:
    cod_cliente = selecao.split(" - ")[0].strip()
    dados_empresa = df_clientes[df_clientes['CÓD'] == cod_cliente].iloc[0]
    cnpj_auditado = str(dados_empresa['CNPJ']).strip()

    with col_b:
        st.markdown("### Passo 2: Seleção de Regime")
        regime = st.selectbox("Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], label_visibility="collapsed")
        is_ret = st.toggle("Habilitar MG (RET)")

    st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b> {dados_empresa['RAZÃO SOCIAL']} | <b>CNPJ:</b> {cnpj_auditado}</div>", unsafe_allow_html=True)
    
    c1_stat, c2_stat = st.columns(2)
    # Procurando o arquivo específico da empresa
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
        if st.button("🚀 INICIAR ANÁLISE"):
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
                        st.download_button("💾 BAIXAR RELATÓRIO FINAL", relat, f"Sentinela_{cod_cliente}_v2.1.xlsx", use_container_width=True)
                    except Exception as e:
                        st.error(f"Erro no processamento: {e}")
            else:
                st.warning("⚠️ Verifique os XMLs e o Regime Fiscal.")
