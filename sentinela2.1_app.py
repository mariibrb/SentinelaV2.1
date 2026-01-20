import streamlit as st
import os, io, pandas as pd
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Sentinela 2.1", page_icon="🧡", layout="wide")
aplicar_estilo_sentinela()

# --- GESTÃO DE LIMPEZA ---
if 'v' not in st.session_state:
    st.session_state['v'] = 0

def limpar_campos_upload():
    st.session_state['v'] += 1
    if 'res_final' in st.session_state:
        st.session_state['res_final'] = None
    st.rerun()

# --- CARREGAMENTO DE DADOS ---
@st.cache_data(ttl=600)
def carregar_clientes():
    for p in [".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx", "Clientes Ativos.xlsx"]:
        if os.path.exists(p):
            try:
                df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except: continue
    return pd.DataFrame()

df_cli = carregar_clientes()
versao = st.session_state['v']

# --- SIDEBAR (CONFIGURAÇÕES FIXAS) ---
with st.sidebar:
    logo = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo):
        st.image(logo, use_container_width=True)
    
    st.markdown("---")
    # Keys fixas para garantir que os dados não sumam ao limpar arquivos
    emp_sel = st.selectbox("Passo 1: Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="f_emp")
    
    if emp_sel:
        reg_sel = st.selectbox("Passo 2: Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="f_reg")
        seg_sel = st.selectbox("Passo 3: Segmento", ["", "Comércio", "Indústria", "Equiparado"], key="f_seg")
        ret_sel = st.toggle("Passo 4: Habilitar RET", key="f_ret")
        
        st.markdown("---")
        cod_c = emp_sel.split(" - ")[0].strip()
        emp_dados = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        
        st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{emp_dados['RAZÃO SOCIAL']}<br><b>CNPJ:</b> {emp_dados['CNPJ']}</div>", unsafe_allow_html=True)
        
        if os.path.exists(f"Bases_Tributárias/{cod_c}-Bases_Tributarias.xlsx"):
            st.success("✅ Base Localizada")
        else:
            st.warning("⚠️ Base não localizada")

        st.download_button("📥 Modelo Bases", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True, type="primary", key="f_mod")

# --- CORPO PRINCIPAL ---
c_t, c_r = st.columns([4, 1])
with c_t:
    st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    if st.button("🔄 LIMPAR ARQUIVOS", use_container_width=True, key=f"r_{versao}"):
        limpar_campos_upload()

if emp_sel:
    st.markdown("### 📥 Passo 5: Central de Arquivos")
    c1, c2, c3 = st.columns(3)
    # Keys dinâmicas baseadas na versão para permitir a limpeza sem erro de duplicidade
    with c1: up_xml = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True, key=f"x_{versao}")
    with c2: 
        up_ge = st.file_uploader("📥 Gerencial E", accept_multiple_files=True, key=f"ge_{versao}")
        up_ae = st.file_uploader("📥 Autenticidade E", accept_multiple_files=True, key=f"ae_{versao}")
    with c3:
        up_gs = st.file_uploader("📤 Gerencial S", accept_multiple_files=True, key=f"gs_{versao}")
        up_as = st.file_uploader("📤 Autenticidade S", accept_multiple_files=True, key=f"as_{versao}")

    if st.button("🚀 INICIAR ANÁLISE", use_container_width=True, key=f"run_{versao}"):
        if up_xml and reg_sel and seg_sel:
            with st.spinner("Realizando auditoria fiscal..."):
                try:
                    # Lógica de cruzamento e auditoria mantida íntegra
                    xe, xs = extrair_dados_xml_recursivo(up_xml, str(emp_dados['CNPJ']).strip())
                    buf = io.BytesIO()
                    with pd.ExcelWriter(buf, engine='openpyxl') as writer:
                        gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, up_ae, up_as, up_ge, up_gs)
                    st.session_state['res_final'] = buf.getvalue()
                except Exception as e: st.error(f"Erro: {e}")
        else:
            st.warning("⚠️ Preencha o Regime, o Segmento e suba os XMLs.")

    if st.session_state.get('res_final'):
        st.markdown("<div style='text-align: center;'><h2>✅ AUDITORIA CONCLUÍDA</h2></div>", unsafe_allow_html=True)
        st.download_button("💾 BAIXAR RELATÓRIO", st.session_state['res_final'], f"Sentinela_{cod_c}.xlsx", use_container_width=True, key=f"dl_{versao}")
else:
    st.info("👈 Utilize a barra lateral para configurar a empresa.")
