import streamlit as st
import os, io, pandas as pd, zipfile, re, random
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final
from Apuracoes.apuracao_difal import gerar_resumo_uf 

# --- MOTOR GARIMPEIRO (Lógica Íntegra Original) ---
def identify_xml_info(content_bytes, client_cnpj, file_name):
    client_cnpj_clean = "".join(filter(str.isdigit, str(client_cnpj))) if client_cnpj else ""
    nome_puro = os.path.basename(file_name)
    if nome_puro.startswith('.') or nome_puro.startswith('~') or not nome_puro.lower().endswith('.xml'):
        return None, False
    resumo = {
        "Arquivo": nome_puro, "Chave": "", "Tipo": "Outros", "Série": "0",
        "Número": 0, "Status": "NORMAIS", "Pasta": "RECEBIDOS_TERCEIROS/OUTROS",
        "Valor": 0.0, "Conteúdo": content_bytes
    }
    try:
        content_str = content_bytes[:20000].decode('utf-8', errors='ignore')
        match_ch = re.search(r'\d{44}', content_str)
        resumo["Chave"] = match_ch.group(0) if match_ch else ""
        tag_l = content_str.lower()
        tipo = "NF-e"
        if '<mod>65</mod>' in tag_l: tipo = "NFC-e"
        elif '<infcte' in tag_l: tipo = "CT-e"
        elif '<infmdfe' in tag_l: tipo = "MDF-e"
        status = "NORMAIS"
        if '110111' in tag_l: status = "CANCELADOS"
        elif '110110' in tag_l: status = "CARTA_CORRECAO"
        elif '<inutnfe' in tag_l or '<procinut' in tag_l:
            status = "INUTILIZADOS"; tipo = "Inutilizacoes"
        resumo["Tipo"] = tipo; resumo["Status"] = status
        resumo["Série"] = re.search(r'<(?:serie)>(\d+)</', tag_l).group(1) if re.search(r'<(?:serie)>(\d+)</', tag_l) else "0"
        n_match = re.search(r'<(?:nnf|nct|nmdf|nnfini)>(\d+)</', tag_l)
        resumo["Número"] = int(n_match.group(1)) if n_match else 0
        if status == "NORMAIS":
            v_match = re.search(r'<(?:vnf|vtprest)>([\d.]+)</', tag_l)
            resumo["Valor"] = float(v_match.group(1)) if v_match else 0.0
        
        cnpj_emit = re.search(r'<cnpj>(\d+)</cnpj>', tag_l).group(1) if re.search(r'<cnpj>(\d+)</cnpj>', tag_l) else ""
        is_p = (cnpj_emit == client_cnpj_clean) or (resumo["Chave"] and client_cnpj_clean in resumo["Chave"][6:20])
        resumo["Pasta"] = f"EMITIDOS_CLIENTE/{tipo}/{status}/Serie_{resumo['Série']}" if is_p else f"RECEBIDOS_TERCEIROS/{tipo}"
        return resumo, is_p
    except: return None, False

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")
aplicar_estilo_sentinela()

if 'v_ver' not in st.session_state: st.session_state['v_ver'] = 0
if 'executado' not in st.session_state: st.session_state['executado'] = False

def limpar_central():
    st.session_state.clear()
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

df_cli = carregar_clientes()

# --- SIDEBAR (Com Travas e Foto) ---
with st.sidebar:
    logo_path = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_path): st.image(logo_path, use_container_width=True)
    st.markdown("---")
    
    # Passo 1: Empresa
    emp_sel = st.selectbox("Passo 1: Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="f_emp")
    
    if emp_sel:
        # Passo 2: Regime (Bloqueado até Passo 1)
        reg_sel = st.selectbox("Passo 2: Escolha o Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="f_reg")
        
        if reg_sel:
            # Passo 3: Segmento (Bloqueado até Passo 2)
            seg_sel = st.selectbox("Passo 3: Escolha o Segmento", ["", "Comércio", "Indústria", "Equiparado"], key="f_seg")
            ret_sel = st.toggle("Passo 4: Habilitar MG (RET)", key="f_ret")
            
            st.markdown("---")
            cod_c = emp_sel.split(" - ")[0].strip()
            dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
            cnpj_limpo = "".join(filter(str.isdigit, str(dados_e['CNPJ'])))
            st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}</div>", unsafe_allow_html=True)
            
            path_base = f"Bases_Tributarias/{cod_c}-Bases_Tributarias.xlsx"
            if os.path.exists(path_base): st.success("💎 Modo Elite: Base Localizada")
            else: st.warning("🔍 Modo Cegas: Base não localizada")
            
            st.download_button("📥 Modelo Bases", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True, type="primary", key="f_mod")

# --- CABEÇALHO ---
c_t, c_r = st.columns([4, 1])
with c_t: st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    if st.button("🔄 LIMPAR TUDO"): limpar_central()

# --- ÁREA DE ARQUIVOS (ABAS) ---
if emp_sel and reg_sel:
    tab_xml, tab_dom = st.tabs(["📂 Garimpeiro: XMLs", "📄 Relatórios Domínio"])
    
    with tab_xml:
        xml_files = st.file_uploader("Arraste ZIPs ou XMLs", accept_multiple_files=True, type=['zip', 'xml'], key="up_xml")
    
    with tab_dom:
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            ae = st.file_uploader("Autorização de Entradas", type=['xlsx', 'csv'], key="up_ae")
        with col_d2:
            as_f = st.file_uploader("Autorização de Saídas", type=['xlsx', 'csv'], key="up_as")

    # --- PROCESSAMENTO ---
    if st.button("🚀 INICIAR AUDITORIA COMPLETA", use_container_width=True):
        if not xml_files:
            st.error("⚠️ O Garimpeiro precisa de XMLs para trabalhar!")
        else:
            try:
                with st.status("🔍 Garimpeiro em ação...", expanded=True) as status:
                    st.write("📦 Extraindo e classificando XMLs...")
                    df_xe, df_xs = extrair_dados_xml_recursivo(xml_files, cnpj_limpo)
                    
                    if df_xe.empty and df_xs.empty:
                        st.error("❌ Nenhum dado válido encontrado.")
                        st.stop()
                    
                    st.write("📊 Gerando Auditorias e Aba de Difal...")
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        gerar_excel_final(df_xe, df_xs, cod_c, writer, reg_sel, ret_sel, ae, as_f)
                    
                    st.download_button(
                        label="📥 BAIXAR RELATÓRIO COMPLETO",
                        data=output.getvalue(),
                        file_name=f"SENTINELA_{cod_c}_{cnpj_limpo}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
                    status.update(label="✅ Tudo pronto!", state="complete")
            except Exception as e:
                st.error(f"Erro: {e}")
                st.exception(e)
else:
    st.info("👈 Selecione a Empresa e o Regime na barra lateral para liberar os uploads.")

st.markdown("---")
st.caption("Sentinela V2.1 | Inteligência Fiscal 🧩")
