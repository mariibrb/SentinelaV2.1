import streamlit as st
import os, io, pandas as pd, zipfile, re, random
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- MOTOR GARIMPEIRO (Lógica com Trava de CNPJ) ---
def identify_xml_info(content_bytes, client_cnpj, file_name):
    client_cnpj_clean = "".join(filter(str.isdigit, str(client_cnpj))) if client_cnpj else ""
    nome_puro = os.path.basename(file_name)
    if nome_puro.startswith('.') or nome_puro.startswith('~') or not nome_puro.lower().endswith('.xml'):
        return None, False
    
    try:
        content_str = content_bytes[:20000].decode('utf-8', errors='ignore')
        tag_l = content_str.lower()
        
        cnpj_emit = re.search(r'<cnpj>(\d+)</cnpj>', tag_l).group(1) if re.search(r'<cnpj>(\d+)</cnpj>', tag_l) else ""
        cnpj_dest = re.search(r'<dest>.*?<cnpj>(\d+)</cnpj>', tag_l, re.DOTALL).group(1) if re.search(r'<dest>.*?<cnpj>(\d+)</cnpj>', tag_l, re.DOTALL) else ""
        
        is_p = (cnpj_emit == client_cnpj_clean)
        is_dest_p = (cnpj_dest == client_cnpj_clean)
        
        if not (is_p or is_dest_p):
            return None, False

        resumo = {
            "Arquivo": nome_puro, "Chave": "", "Tipo": "Outros", "Série": "0",
            "Número": 0, "Status": "NORMAIS", "Pasta": "OUTROS",
            "Valor": 0.0, "Conteúdo": content_bytes
        }
        
        match_ch = re.search(r'\d{44}', content_str)
        resumo["Chave"] = match_ch.group(0) if match_ch else ""
        
        tipo = "NF-e"
        if '<mod>65</mod>' in tag_l: tipo = "NFC-e"
        elif '<infcte' in tag_l: tipo = "CT-e"
        
        status = "NORMAIS"
        if '110111' in tag_l: status = "CANCELADOS"
        elif '110110' in tag_l: status = "CARTA_CORRECAO"
        
        resumo["Tipo"] = tipo; resumo["Status"] = status
        resumo["Série"] = re.search(r'<(?:serie)>(\d+)</', tag_l).group(1) if re.search(r'<(?:serie)>(\d+)</', tag_l) else "0"
        n_match = re.search(r'<(?:nnf|nct|nmdf|nnfini)>(\d+)</', tag_l)
        resumo["Número"] = int(n_match.group(1)) if n_match else 0
        
        if status == "NORMAIS":
            v_match = re.search(r'<(?:vnf|vtprest)>([\d.]+)</', tag_l)
            resumo["Valor"] = float(v_match.group(1)) if v_match else 0.0
        
        resumo["Pasta"] = f"EMITIDOS_CLIENTE/{tipo}/{status}/Serie_{resumo['Série']}" if is_p else f"RECEBIDOS_TERCEIROS/{tipo}"
        return resumo, is_p
    except: 
        return None, False

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")
aplicar_estilo_sentinela()

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

# --- SIDEBAR (O QUE HAVIA SUMIDO) ---
with st.sidebar:
    logo_path = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_path): st.image(logo_path, use_container_width=True)
    st.markdown("---")
    
    # Seleção de Empresa
    lista_empresas = [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()]
    emp_sel = st.selectbox("Passo 1: Empresa", lista_empresas, key="f_emp")
    
    cnpj_limpo = ""
    if emp_sel:
        reg_sel = st.selectbox("Passo 2: Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="f_reg")
        ret_sel = st.toggle("Habilitar MG (RET)", key="f_ret")
        
        cod_c = emp_sel.split(" - ")[0].strip()
        dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        cnpj_limpo = "".join(filter(str.isdigit, str(dados_e['CNPJ'])))
        
        st.markdown(f"<div style='background:#fff3e0; padding:10px; border-radius:5px; border-left:5px solid #ff6f00;'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}</div>", unsafe_allow_html=True)

# --- CORPO DO APP ---
st.markdown("<h1 style='color:#ff6f00;'>SENTINELA 2.1</h1>", unsafe_allow_html=True)

if emp_sel:
    tab_xml, tab_dominio = st.tabs(["📂 ANÁLISE XML", "📉 CONFORMIDADE DOMÍNIO"])

    with tab_xml:
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True)
        with c2: u_ae = st.file_uploader("📥 Autent. Entradas", accept_multiple_files=True)
        with c3: u_as = st.file_uploader("📤 Autent. Saídas", accept_multiple_files=True)
        
        if st.button("🚀 INICIAR ANÁLISE", use_container_width=True):
            if u_xml:
                with st.spinner("Processando..."):
                    try:
                        u_xml_validos = [f for f in u_xml if zipfile.is_zipfile(f)]
                        xe, xs = extrair_dados_xml_recursivo(u_xml_validos, cnpj_limpo)
                        
                        buf = io.BytesIO()
                        with pd.ExcelWriter(buf, engine='xlsxwriter') as writer:
                            # O Core agora cuida de todas as abas, incluindo as duas de DIFAL
                            gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, u_ae, u_as)
                        
                        st.session_state['relat_buf'] = buf.getvalue()
                        
                        # Garimpeiro
                        p_keys, rel_list, st_counts = set(), [], {"CANCELADOS": 0}
                        b_org, b_todos = io.BytesIO(), io.BytesIO()
                        with zipfile.ZipFile(b_org, "w") as z_org, zipfile.ZipFile(b_todos, "w") as z_todos:
                            for zip_file in u_xml_validos:
                                zip_file.seek(0)
                                with zipfile.ZipFile(zip_file) as z_in:
                                    for name in z_in.namelist():
                                        if name.lower().endswith('.xml'):
                                            xml_data = z_in.read(name)
                                            res, is_p = identify_xml_info(xml_data, cnpj_limpo, name)
                                            if res:
                                                key = res["Chave"] if res["Chave"] else name
                                                if key not in p_keys:
                                                    p_keys.add(key)
                                                    z_org.writestr(f"{res['Pasta']}/{name}", xml_data)
                                                    z_todos.writestr(name, xml_data)
                                                    rel_list.append(res)
                        
                        st.session_state.update({'z_org': b_org.getvalue(), 'z_todos': b_todos.getvalue(), 'relatorio': rel_list, 'executado': True})
                        st.rerun()
                    except Exception as e: st.error(f"Erro: {e}")

    if st.session_state.get('executado'):
        st.markdown("---")
        st.download_button("💾 BAIXAR RELATÓRIO", st.session_state['relat_buf'], f"Sentinela_{cod_c}.xlsx", use_container_width=True)
        st.markdown("### ⛏️ O GARIMPEIRO")
        st.metric("📦 VOLUME CLIENTE", len(st.session_state.get('relatorio', [])))
        co, ct = st.columns(2)
        with co: st.download_button("📂 ZIP ORGANIZADO", st.session_state['z_org'], "garimpo.zip", use_container_width=True)
        with ct: st.download_button("📦 TODOS XML", st.session_state['z_todos'], "todos_xml.zip", use_container_width=True)
else:
    st.info("👈 Selecione a empresa na lateral para começar.")
