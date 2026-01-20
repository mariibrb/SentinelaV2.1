import streamlit as st
import zipfile, io, os, re, pandas as pd, random
from style import aplicar_estilo_sentinela

# --- SETUP ---
st.set_page_config(page_title="O Garimpeiro | Extração XML", page_icon="⛏️", layout="wide")
aplicar_estilo_sentinela()

# --- MOTOR DE IDENTIFICAÇÃO ---
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

# --- ESTADOS DO SISTEMA ---
keys = ['garimpo_ok', 'confirmado', 'z_org', 'z_todos', 'relatorio', 'df_resumo', 'df_faltantes', 'st_counts']
for k in keys:
    if k not in st.session_state:
        if 'df' in k: st.session_state[k] = pd.DataFrame()
        elif 'z_' in k: st.session_state[k] = None
        elif k == 'relatorio': st.session_state[k] = []
        elif k == 'st_counts': st.session_state[k] = {"CANCELADOS": 0, "INUTILIZADOS": 0}
        else: st.session_state[k] = False

st.markdown("<h1 class='titulo-garimpeiro'>⛏️ O GARIMPEIRO</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ⛏️ Painel de Extração")
    cnpj_input = st.text_input("CNPJ DO CLIENTE")
    cnpj_limpo = "".join(filter(str.isdigit, cnpj_input))
    if len(cnpj_limpo) == 14:
        if st.button("✅ LIBERAR OPERAÇÃO"):
            st.session_state['confirmado'] = True; st.rerun()
    st.divider()
    if st.button("🗑️ RESETAR SISTEMA"):
        st.session_state.clear(); st.rerun()

if st.session_state['confirmado']:
    if not st.session_state['garimpo_ok']:
        uploaded_files = st.file_uploader("Suba seus arquivos:", accept_multiple_files=True)
        if uploaded_files and st.button("🚀 INICIAR GRANDE GARIMPO"):
            p_keys, rel_list, seq_map, st_counts = set(), [], {}, {"CANCELADOS": 0, "INUTILIZADOS": 0}
            buf_org, buf_todos = io.BytesIO(), io.BytesIO()
            with st.status("⛏️ Processando...", expanded=True):
                with zipfile.ZipFile(buf_org, "w") as z_org, zipfile.ZipFile(buf_todos, "w") as z_todos:
                    for f in uploaded_files:
                        f_bytes = f.read()
                        items = [(os.path.basename(f.name), f_bytes)]
                        if f.name.lower().endswith('.zip'):
                            items = []
                            with zipfile.ZipFile(io.BytesIO(f_bytes)) as z_in:
                                for n in z_in.namelist():
                                    if n.lower().endswith('.xml'): items.append((os.path.basename(n), z_in.read(n)))
                        for name, xml_data in items:
                            res, is_p = identify_xml_info(xml_data, cnpj_limpo, name)
                            if res:
                                key = res["Chave"] if res["Chave"] else name
                                if key not in p_keys:
                                    p_keys.add(key); z_org.writestr(f"{res['Pasta']}/{name}", xml_data); z_todos.writestr(name, xml_data); rel_list.append(res)
                                    if is_p:
                                        if res["Status"] in st_counts: st_counts[res["Status"]] += 1
                                        sk = (res["Tipo"], res["Série"]); 
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
            st.session_state.update({'z_org': buf_org.getvalue(), 'z_todos': buf_todos.getvalue(), 'relatorio': rel_list, 'df_resumo': pd.DataFrame(res_f), 'df_faltantes': pd.DataFrame(fal_f), 'st_counts': st_counts, 'garimpo_ok': True})
            st.rerun()
    else:
        st.success("⛏️ Garimpo Concluído!")
        sc = st.session_state['st_counts']
        c1, c2, c3 = st.columns(3)
        c1.metric("📦 VOLUME", len(st.session_state['relatorio']))
        c2.metric("❌ CANCELADAS", sc.get("CANCELADOS", 0)); c3.metric("🚫 INUTILIZADAS", sc.get("INUTILIZADOS", 0))
        st.markdown("### 📊 RESUMO E AUDITORIA")
        st.dataframe(st.session_state['df_resumo'], use_container_width=True, hide_index=True)
        st.dataframe(st.session_state['df_faltantes'], use_container_width=True, hide_index=True)
        
        st.divider()
        st.markdown("### 🔍 PENEIRA INDIVIDUAL (BUSCA)")
        busca = st.text_input("Número ou Chave:")
        if busca:
            df_full = pd.DataFrame(st.session_state['relatorio'])
            filtro = df_full[df_full['Número'].astype(str).contains(busca) | df_full['Chave'].contains(busca)]
            for _, row in filtro.iterrows():
                st.download_button(f"📥 XML Nº {row['Número']} ({row['Status']})", row['Conteúdo'], row['Arquivo'], key=f"dl_{row['Chave']}_{random.random()}")

        st.divider()
        col1, col2 = st.columns(2)
        with col1: st.download_button("📂 BAIXAR ORGANIZADO", st.session_state['z_org'], "garimpo_pastas.zip", use_container_width=True)
        with col2: st.download_button("📦 BAIXAR TODOS XML", st.session_state['z_todos'], "todos_xml.zip", use_container_width=True)
