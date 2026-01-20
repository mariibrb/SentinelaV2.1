import streamlit as st
import os, io, pandas as pd, zipfile, re, random
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final
from Apuracoes.apuracao_difal import gerar_resumo_uf 

# --- MOTOR GARIMPEIRO (Lógica Íntegra Original com Trava de CNPJ) ---
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
        tag_l = content_str.lower()
        
        # Filtro de Identidade: Busca CNPJ Emitente e Destinatário
        cnpj_emit = re.search(r'<cnpj>(\d+)</cnpj>', tag_l).group(1) if re.search(r'<cnpj>(\d+)</cnpj>', tag_l) else ""
        cnpj_dest = re.search(r'<dest>.*?<cnpj>(\d+)</cnpj>', tag_l, re.DOTALL).group(1) if re.search(r'<dest>.*?<cnpj>(\d+)</cnpj>', tag_l, re.DOTALL) else ""
        
        # Só prossegue se o cliente selecionado for parte da nota
        is_p = (cnpj_emit == client_cnpj_clean)
        is_dest_p = (cnpj_dest == client_cnpj_clean)
        
        if not (is_p or is_dest_p):
            return None, False

        match_ch = re.search(r'\d{44}', content_str)
        resumo["Chave"] = match_ch.group(0) if match_ch else ""
        
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
    for p in [".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx", "Clientes Ativos.xlsx"]:
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
        reg_sel = st.selectbox("Passo 2: Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="f_reg")
        seg_sel = st.selectbox("Passo 3: Segmento", ["", "Comércio", "Indústria", "Equiparado"], key="f_seg")
        ret_sel = st.toggle("Passo 4: Habilitar MG (RET)", key="f_ret")
        st.markdown("---")
        cod_c = emp_sel.split(" - ")[0].strip()
        dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        cnpj_limpo = "".join(filter(str.isdigit, str(dados_e['CNPJ'])))
        st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}</div>", unsafe_allow_html=True)
        
        st.download_button("📥 Modelo Bases", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True, type="primary", key="f_mod")

# --- CABEÇALHO ---
c_t, c_r = st.columns([4, 1])
with c_t: st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    if st.button("🔄 LIMPAR TUDO"): limpar_central()

# --- CONTEÚDO ---
if emp_sel:
    tab_xml, tab_dominio = st.tabs(["📂 ANÁLISE XML", "📉 CONFORMIDADE DOMÍNIO"])

    with tab_xml:
        st.markdown("### 📥 Central de Importação")
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True, key=f"x_{v}")
        with c2: u_ae = st.file_uploader("📥 Autent. Entradas", accept_multiple_files=True, key=f"ae_{v}")
        with c3: u_as = st.file_uploader("📤 Autent. Saídas", accept_multiple_files=True, key=f"as_{v}")
        
        if st.button("🚀 INICIAR ANÁLISE XML", use_container_width=True):
            if u_xml:
                with st.spinner("Auditando..."):
                    try:
                        u_xml_validos = [f for f in u_xml if zipfile.is_zipfile(f)]
                        xe, xs = extrair_dados_xml_recursivo(u_xml_validos, cnpj_limpo)
                        buf = io.BytesIO()
                        with pd.ExcelWriter(buf, engine='xlsxwriter') as writer:
                            gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, u_ae, u_as)
                            # Chama a aba de apuração DIFAL/ST/FECP sem dar conflito de aba
                            gerar_resumo_uf(xs, writer, xe) 
                        
                        st.session_state['relat_buf'] = buf.getvalue()
                        
                        # Garimpeiro
                        p_keys, rel_list, seq_map, st_counts = set(), [], {}, {"CANCELADOS": 0, "INUTILIZADOS": 0}
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
                                                    if is_p:
                                                        if res["Status"] in st_counts: st_counts[res["Status"]] += 1
                                                        sk = (res["Tipo"], res["Série"])
                                                        if sk not in seq_map: seq_map[sk] = {"nums": set(), "valor": 0.0}
                                                        seq_map[sk]["nums"].add(res["Número"])
                                                        seq_map[sk]["valor"] += res["Valor"]

                        res_f = []
                        for (t, s), d in seq_map.items():
                            res_f.append({"Doc": t, "Série": s, "Qtd": len(d["nums"]), "Valor": round(d["valor"], 2)})
                            
                        st.session_state.update({'z_org': b_org.getvalue(), 'z_todos': b_todos.getvalue(), 'relatorio': rel_list, 'df_resumo': pd.DataFrame(res_f), 'st_counts': st_counts, 'executado': True})
                        st.rerun()
                    except Exception as e: st.error(f"Erro: {e}")

    if st.session_state.get('executado'):
        st.markdown("---")
        st.download_button("💾 BAIXAR RELATÓRIO FINAL", st.session_state['relat_buf'], f"Sentinela_{cod_c}.xlsx", use_container_width=True)
        st.markdown("<h2 style='text-align: center;'>⛏️ O GARIMPEIRO</h2>", unsafe_allow_html=True)
        st.metric("📦 VOLUME CLIENTE", len(st.session_state.get('relatorio', [])))
        st.dataframe(st.session_state['df_resumo'], use_container_width=True)
        co, ct = st.columns(2)
        with co: st.download_button("📂 ZIP ORGANIZADO", st.session_state['z_org'], "garimpo.zip", use_container_width=True)
        with ct: st.download_button("📦 TODOS XML", st.session_state['z_todos'], "todos_xml.zip", use_container_width=True)
else:
    st.info("👈 Selecione a empresa na barra lateral.")
