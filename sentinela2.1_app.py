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
v = st.session_state['v_ver']

# --- SIDEBAR ---
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
        cnpj_limpo = "".join(filter(str.isdigit, str(dados_e['CNPJ'])))
        st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}</div>", unsafe_allow_html=True)
        
        path_base = f"Bases_Tributarias/{cod_c}-Bases_Tributarias.xlsx"
        if os.path.exists(path_base): st.success("💎 Modo Elite: Base Localizada")
        else: st.warning("🔍 Modo Cegas: Base não localizada")
            
        if ret_sel:
            path_ret = f"RET/{cod_c}-RET_MG.xlsx"
            if os.path.exists(path_ret): st.success("✅ Base RET (MG) Localizada")
            else: st.warning("⚠️ Base RET (MG) não localizada")
        
        st.download_button("📥 Modelo Bases", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True, type="primary", key="f_mod")

# --- CABEÇALHO ---
c_t, c_r = st.columns([4, 1])
with c_t: st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    if st.button("🔄 LIMPAR TUDO"): limpar_central()
import streamlit as st
import pandas as pd
import io
from sentinela_core import extrair_xml, gerar_analise_xml

# Configuração da Página (Estética Fofa solicitada)
st.set_page_config(page_title="Sentinela V2.1", layout="wide", page_icon="🛡️")

# CSS para o layout delicado e tons pastéis
st.markdown("""
    <style>
    .stApp { background-color: #FFF5F7; }
    .main { background: white; border-radius: 20px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    h1 { color: #FF69B4; font-family: 'Segoe UI'; }
    .stButton>button { background-color: #FFB6C1; color: white; border-radius: 10px; border: none; }
    .stButton>button:hover { background-color: #FF69B4; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Sentinela V2.1 - Auditoria Fiscal")

# --- SIDEBAR: CONFIGURAÇÕES E FILTROS ---
with st.sidebar:
    st.header("⚙️ Configurações")
    cnpj_auditado = st.text_input("CNPJ da Empresa Auditada", placeholder="Apenas números")
    cod_cliente = st.text_input("Código do Cliente (Domínio)", placeholder="Ex: 001")
    regime = st.selectbox("Regime Tributário", ["Lucro Presumido", "Lucro Real", "Simples Nacional"])
    
    st.divider()
    is_ret = st.checkbox("Gerar Auditoria RET MG?")
    
    st.divider()
    st.info("💡 Carregue os XMLs e os relatórios da Domínio para iniciar o Garimpeiro.")

# --- ÁREA DE UPLOAD ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📂 XMLs (Entradas e Saídas)")
    xml_files = st.file_uploader("Arraste aqui os ZIPs ou XMLs", accept_multiple_files=True, type=['zip', 'xml'])

with col2:
    st.subheader("📄 Relatórios Domínio")
    ae = st.file_uploader("Autorização de Entradas (Excel/CSV)", type=['xlsx', 'csv'])
    as_f = st.file_uploader("Autorização de Saídas (Excel/CSV)", type=['xlsx', 'csv'])

# --- PROCESSAMENTO ---
if st.button("🚀 Iniciar Auditoria Completa"):
    if not cnpj_auditado or not xml_files:
        st.warning("⚠️ Por favor, informe o CNPJ e carregue os arquivos XML.")
    else:
        try:
            with st.status("🔍 Garimpeiro em ação: Minerando arquivos...", expanded=True) as status:
                # 1. Extração Recursiva
                st.write("📦 Extraindo dados dos XMLs...")
                df_xe, df_xs = extrair_xml(xml_files, cnpj_auditado)
                
                if df_xe.empty and df_xs.empty:
                    st.error("❌ Nenhum XML válido foi processado.")
                    st.stop()
                
                st.write(f"✅ Sucesso! Entradas: {len(df_xe)} | Saídas: {len(df_xs)}")
                
                # 2. Geração do Relatório Excel
                st.write("📊 Gerando planilhas de auditoria...")
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    # O Core gerencia a criação das abas e chama o Difal internamente
                    gerar_analise_xml(
                        df_xe, df_xs, cod_cliente, writer, regime, 
                        is_ret, ae, as_f
                    )
                
                processed_data = output.getvalue()
                status.update(label="✅ Auditoria Concluída!", state="complete", expanded=False)

            # --- DOWNLOAD ---
            st.success("✨ Tudo pronto! O seu relatório de auditoria foi gerado com sucesso.")
            
            nome_arquivo = f"SENTINELA_V2.1_{cod_cliente}_{cnpj_auditado}.xlsx"
            st.download_button(
                label="📥 Baixar Relatório de Auditoria",
                data=processed_data,
                file_name=nome_arquivo,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
        except Exception as e:
            st.error(f"❌ Erro Crítico no Processamento: {e}")
            st.exception(e)

# Mensagem de rodapé fofa
st.markdown("---")
st.caption("Desenvolvido com ❤️ para facilitar sua rotina fiscal.")
