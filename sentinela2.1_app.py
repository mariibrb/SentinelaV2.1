import streamlit as st
import os, io, pandas as pd, zipfile, re, random
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

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
for k in ['garimpo_ok', 'relatorio', 'df_resumo', 'df_faltantes', 'st_counts', 'z_org', 'z_todos']:
    if k not in st.session_state: st.session_state[k] = pd.DataFrame() if 'df' in k else None

def limpar_central():
    st.session_state.clear()
    st.rerun()

# --- CARREGAMENTO ---
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

# --- SIDEBAR ORIGINAL (RESTAURADA) ---
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
        
        # Cartão de Status Aprovado
        st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}<br><b>CNPJ:</b> {dados_e['CNPJ']}</div>", unsafe_allow_html=True)
        
        # Verificação de Bases
        if os.path.exists(f"Bases_Tributárias/{cod_c}-Bases_Tributarias.xlsx"): st.success("✅ Base de Impostos Localizada")
        else: st.warning("⚠️ Base não localizada")
            
        if ret_sel:
            if os.path.exists(f"RET/{cod_c}-RET_MG.xlsx"): st.success("✅ Base RET (MG) Localizada")
            else: st.warning("⚠️ Base RET (MG) não localizada")
        
        st.download_button("📥 Modelo Bases", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True, type="primary", key="f_mod")

# --- CABEÇALHO ---
c_t, c_r = st.columns([4, 1])
with c_t: st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    if st.button("🔄 LIMPAR TUDO", use_container_width=True): limpar_central()

# --- CONTEÚDO ---
if emp_sel:
    tab_xml, tab_dominio = st.tabs(["📂 ANÁLISE XML", "📉 CONFORMIDADE DOMÍNIO"])

    with tab_xml:
        st.markdown("### 📥 Central de Importação")
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True, key=f"x_{v}")
        with c2: u_ae = st.file_uploader("📥 Autenticidade Entradas", accept_multiple_files=True, key=f"ae_{v}")
        with c3: u_as = st.file_uploader("📤 Autenticidade Saídas", accept_multiple_files=True, key=f"as_{v}")
        
        if st.button("🚀 INICIAR ANÁLISE XML", use_container_width=True, key=f"run_{v}"):
            if u_xml:
                with st.spinner("Realizando auditoria fiscal e garimpo..."):
                    try:
                        xe, xs = extrair_dados_xml_recursivo(u_xml, cnpj_limpo)
                        buf = io.BytesIO()
                        with pd.ExcelWriter(buf, engine='openpyxl') as writer:
                            gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, u_ae, u_as, None, None)
                        st.session_state['relat_buf'] = buf.getvalue()

                        # Processamento Garimpeiro
                        p_keys, rel_list, seq_map, st_counts = set(), [], {}, {"CANCELADOS": 0, "INUTILIZADOS": 0}
                        b_org, b_todos = io.BytesIO(), io.BytesIO()
                        with zipfile.ZipFile(b_org, "w") as z_org, zipfile.ZipFile(b_todos, "w") as z_todos:
                            for zip_file in u_xml:
                                with zipfile.ZipFile(zip_file) as z_in:
                                    for name in z_in.namelist():
                                        if name.lower().endswith('.xml'):
                                            xml_data = z_in.read(name)
                                            res, is_p = identify_xml_info(xml_data, cnpj_limpo, name)
                                            if res:
                                                key = res["Chave"] if res["Chave"] else name
                                                if key not in p_keys:
                                                    p_keys.add(key); z_org.writestr(f"{res['Pasta']}/{name}", xml_data); z_todos.writestr(name, xml_data); rel_list.append(res)
                                                    if is_p:
                                                        if res["Status"] in st_counts: st_counts[res["Status"]] += 1
                                                        sk = (res["Tipo"], res["Série"])
                                                        if sk not in seq_map: seq_map[sk] = {"nums": set(), "valor": 0.0}
                                                        seq_map[sk]["nums"].add(res["Número"]); seq_map[sk]["valor"] += res["Valor"]
                        
                        res_f, fal_f, nums_s = [], [], {}
                        for (t, s), d in seq_map.items():
                            ns = d["nums"]; res_f.append({"Documento": t, "Série": s, "Início": min(ns), "Fim": max(ns), "Qtd": len(ns), "Valor": round(d["valor"], 2)})
                            if s not in nums_s: nums_s[s] = set()
                            nums_s[s].update(ns)
                        for s, ns in nums_s.items():
                            if len(ns) > 1:
                                buracos = sorted(list(set(range(min(ns), max(ns) + 1)) - ns))
                                for b in buracos: fal_f.append({"Série": s, "Nº Faltante": b})
                        st.session_state.update({'z_org': b_org.getvalue(), 'z_todos': b_todos.getvalue(), 'relatorio': rel_list, 'df_resumo': pd.DataFrame(res_f), 'df_faltantes': pd.DataFrame(fal_f), 'st_counts': st_counts, 'garimpo_ok': True})
                    except Exception as e: st.error(f"Erro: {e}")

        if st.session_state.get('relat_buf'):
            st.markdown("<div style='text-align: center; padding: 15px;'><h2>✅ PROCESSAMENTO CONCLUÍDO</h2></div>", unsafe_allow_html=True)
            st.download_button("💾 BAIXAR RELATÓRIO FINAL", st.session_state['relat_buf'], f"Sentinela_{cod_c}.xlsx", use_container_width=True)
            
            st.markdown("---")
            st.markdown("<h2 style='text-align: center;'>⛏️ O GARIMPEIRO (Resultado da Extração)</h2>", unsafe_allow_html=True)
            sc = st.session_state.get('st_counts', {"CANCELADOS": 0, "INUTILIZADOS": 0})
            c1, c2, c3 = st.columns(3)
            c1.metric("📦 VOLUME TOTAL", len(st.session_state.get('relatorio', [])))
            c2.metric("❌ CANCELADAS", sc.get("CANCELADOS", 0)); c3.metric("🚫 INUTILIZADAS", sc.get("INUTILIZADOS", 0))

            col_res, col_fal = st.columns(2)
            with col_res:
                st.write("**Resumo por Série:**")
                st.dataframe(st.session_state.get('df_resumo'), use_container_width=True, hide_index=True)
            with col_fal:
                st.write("**Notas Faltantes:**")
                st.dataframe(st.session_state.get('df_faltantes'), use_container_width=True, hide_index=True)

            st.markdown("### 📥 EXTRAÇÃO DE ARQUIVOS")
            c_org, c_todos = st.columns(2)
            with c_org: st.download_button("📂 BAIXAR XMLs ORGANIZADOS", st.session_state['z_org'], "garimpo_pastas.zip", use_container_width=True)
            with c_todos: st.download_button("📦 BAIXAR TODOS XMLs", st.session_state['z_todos'], "todos_xml.zip", use_container_width=True)

    with tab_dominio:
        st.markdown("### 📉 Conformidade Domínio")
        sub_icms, sub_difal, sub_ret, sub_pis = st.tabs(["ICMS/IPI", "Difal/ST/FECP", "RET", "Pis/Cofins"])
        msg = "⚙️ **Módulo em Construção**"
        with sub_icms: st.info(msg)
        with sub_difal: st.info(msg)
        with sub_ret: st.info(msg)
        with sub_pis: st.info(msg)
else:
    st.info("👈 Selecione a empresa na barra lateral.")
