import streamlit as st
import os, io, pandas as pd
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")
aplicar_estilo_sentinela()

if 'v_ver' not in st.session_state: 
    st.session_state['v_ver'] = 0

def limpar_central():
    st.session_state['v_ver'] += 1
    if 'relat_buf' in st.session_state: 
        st.session_state['relat_buf'] = None
    st.rerun()

@st.cache_data(ttl=600)
def carregar_clientes():
    caminhos = [".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx", "Clientes Ativos.xlsx"]
    for p in caminhos:
        if os.path.exists(p):
            try:
                df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except: continue
    return pd.DataFrame()

def localizar_base_impostos(cod_cliente):
    pastas = ["Bases_Tributárias", "Bases_Tributarias", "bases_tributarias", "Bases"]
    arquivos = [f"{cod_cliente}-Bases_Tributarias.xlsx", f"{cod_cliente}-Bases_Tributárias.xlsx"]
    for pasta in pastas:
        for arquivo in arquivos:
            caminho_teste = os.path.join(pasta, arquivo)
            if os.path.exists(caminho_teste): return caminho_teste
    return None

df_cli = carregar_clientes()
v = st.session_state['v_ver']

# --- SIDEBAR (IDENTIDADE E CONFIGURAÇÃO) ---
with st.sidebar:
    logo_path = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_path): st.image(logo_path, use_container_width=True)
    st.markdown("---")
    emp_sel = st.selectbox("Passo 1: Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="f_emp")
    
    if emp_sel:
        reg_sel = st.selectbox("Passo 2: Escolha o Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="f_reg")
        seg_sel = st.selectbox("Passo 3: Escolha o Segmento", ["", "Comércio", "Indústria", "Equiparado"], key="f_seg")
        ret_sel = st.toggle("Passo 4: Habilitar MG (RET)", key="f_ret")
        st.markdown("---")
        cod_c = emp_sel.split(" - ")[0].strip()
        dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}<br><b>CNPJ:</b> {dados_e['CNPJ']}</div>", unsafe_allow_html=True)
        c_base = localizar_base_impostos(cod_c)
        if c_base: st.success("✅ Base de Impostos Localizada")
        else: st.warning("⚠️ Base não localizada")
        if ret_sel:
            path_ret = f"RET/{cod_c}-RET_MG.xlsx"
            if os.path.exists(path_ret): st.success("✅ Base RET (MG) Localizada")
            else: st.warning("⚠️ Base RET (MG) não localizada")
        st.download_button("📥 Modelo Bases", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True, type="primary", key="f_mod")

# --- CABEÇALHO ---
c_t, c_r = st.columns([4, 1])
with c_t: st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 LIMPAR TUDO", use_container_width=True, key=f"reset_{v}"): limpar_central()

# --- CONTEÚDO PRINCIPAL ---
if emp_sel:
    tab_xml, tab_dominio = st.tabs(["📂 ANÁLISE XML", "📉 CONFORMIDADE DOMÍNIO"])

    with tab_xml:
        st.markdown("### 📥 Passo 5: Central de Arquivos")
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True, key=f"x_{v}")
        with c2: u_ae = st.file_uploader("📥 Autenticidade Entradas", accept_multiple_files=True, key=f"ae_{v}")
        with c3: u_as = st.file_uploader("📤 Autenticidade Saídas", accept_multiple_files=True, key=f"as_{v}")
        
        if st.button("🚀 INICIAR ANÁLISE XML", use_container_width=True, key=f"run_{v}"):
            if u_xml and reg_sel and seg_sel:
                with st.spinner("Auditando..."):
                    try:
                        xe, xs = extrair_dados_xml_recursivo(u_xml, str(dados_e['CNPJ']).strip())
                        buf = io.BytesIO()
                        with pd.ExcelWriter(buf, engine='openpyxl') as writer:
                            gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, u_ae, u_as, None, None)
                        st.session_state['relat_buf'] = buf.getvalue()
                    except Exception as e: st.error(f"Erro: {e}")
            else: st.warning("⚠️ Verifique a Sidebar e os arquivos.")
        if st.session_state.get('relat_buf'):
            st.download_button("💾 BAIXAR RELATÓRIO", st.session_state['relat_buf'], f"Sentinela_{cod_c}.xlsx", use_container_width=True, key=f"dl_{v}")

    with tab_dominio:
        st.markdown("### 📉 Módulos de Conformidade")
        sub_icms, sub_difal, sub_ret, sub_pis = st.tabs(["ICMS/IPI", "Difal/ST/FECP", "RET", "Pis/Cofins"])
        
        # Mensagem padrão para sub-módulos em desenvolvimento
        msg_construcao = "⚙️ **Módulo em Construção** | Este recurso está sendo preparado para integração com o Domínio Sistemas."

        with sub_icms:
            st.markdown("#### 📊 Auditoria ICMS/IPI")
            st.info(msg_construcao)
            
        with sub_difal:
            st.markdown("#### ⚖️ Auditoria Difal / ST / FECP")
            st.info(msg_construcao)
            
        with sub_ret:
            st.markdown("#### 🏨 Auditoria RET (Regime Especial)")
            st.info(msg_construcao)
            
        with sub_pis:
            st.markdown("#### 💰 Auditoria PIS/Cofins")
            st.info(msg_construcao)
else:
    st.info("👈 Selecione a empresa na barra lateral.")
