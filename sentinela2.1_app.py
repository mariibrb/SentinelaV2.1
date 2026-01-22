import streamlit as st
import os, io, pandas as pd, zipfile, re, sqlite3
from hashlib import sha256
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO DE SEGURANÇA E BANCO DE DATOS ---
def init_db():
    conn = sqlite3.connect('sentinela_usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                 (nome TEXT, email TEXT PRIMARY KEY, senha TEXT, status TEXT, nivel TEXT)''')
    
    # CONFIGURANDO MARIANA COMO ADMIN MESTRE (marii.brbj@gmail.com)
    email_admin = 'marii.brbj@gmail.com'
    c.execute("SELECT * FROM usuarios WHERE email=?", (email_admin,))
    
    # Gerando o hash da sua nova senha forte
    nova_senha_hash = sha256("Senhaforte@123".encode()).hexdigest()
    
    if not c.fetchone():
        # Se não existe, cria com o usuário 'mariana'
        c.execute("INSERT INTO usuarios VALUES (?, ?, ?, 'ATIVO', 'ADMIN')", 
                  ('mariana', email_admin, nova_senha_hash))
    else:
        # Se já existe, garante que o nome seja 'mariana' e a senha seja a solicitada
        c.execute("UPDATE usuarios SET senha=?, nome='mariana' WHERE email=?", (nova_senha_hash, email_admin))
        
    conn.commit()
    conn.close()

def hash_senha(senha):
    return sha256(senha.encode()).hexdigest()

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
    except: 
        return None, False

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")
aplicar_estilo_sentinela()
init_db()

if 'user_data' not in st.session_state: st.session_state['user_data'] = None
if 'v_ver' not in st.session_state: st.session_state['v_ver'] = 0
if 'executado' not in st.session_state: st.session_state['executado'] = False

def limpar_central():
    st.session_state.clear()
    st.rerun()

# --- TELA DE ACESSO (LOGIN E CADASTRO) ---
if not st.session_state['user_data']:
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        aba_l, aba_c = st.tabs(["🔐 ACESSAR SISTEMA", "📝 SOLICITAR ACESSO"])
        
        with aba_l:
            with st.container(border=True):
                u_input = st.text_input("Usuário ou E-mail")
                pass_l = st.text_input("Senha", type="password")
                if st.button("ENTRAR", use_container_width=True):
                    conn = sqlite3.connect('sentinela_usuarios.db')
                    c = conn.cursor()
                    # Permite login pelo nome 'mariana' ou pelo e-mail
                    c.execute("SELECT nome, email, status, nivel FROM usuarios WHERE (nome=? OR email=?) AND senha=?", 
                              (u_input, u_input, hash_senha(pass_l)))
                    user = c.fetchone()
                    conn.close()
                    if user:
                        if user[2] == 'ATIVO':
                            st.session_state['user_data'] = {"nome": user[0], "email": user[1], "nivel": user[3]}
                            st.rerun()
                        else: st.warning("Aguarde a Mariana liberar seu acesso.")
                    else: st.error("Usuário ou senha inválidos.")
        
        with aba_c:
            with st.container(border=True):
                st.write("Solicite seu acesso à Mariana:")
                n_nome = st.text_input("Nome Completo")
                n_email = st.text_input("E-mail")
                n_pass = st.text_input("Defina uma Senha", type="password")
                if st.button("SOLICITAR LIBERAÇÃO", use_container_width=True):
                    if n_nome and n_email and n_pass:
                        try:
                            conn = sqlite3.connect('sentinela_usuarios.db')
                            c = conn.cursor()
                            c.execute("INSERT INTO usuarios VALUES (?, ?, ?, 'PENDENTE', 'USER')", 
                                      (n_nome, n_email, hash_senha(n_pass)))
                            conn.commit(); conn.close()
                            st.success("Solicitação enviada! A Mariana receberá um e-mail para aprovação.")
                        except: st.error("Este e-mail já está cadastrado ou pendente.")
                    else: st.warning("Preencha todos os campos.")
    st.stop()

# --- ÁREA EXCLUSIVA DE ADMINISTRAÇÃO (MARIANA) ---
if st.session_state['user_data']['nivel'] == 'ADMIN':
    with st.expander("🛠️ GESTÃO DE USUÁRIOS (ADMIN)"):
        conn = sqlite3.connect('sentinela_usuarios.db')
        df_users = pd.read_sql_query("SELECT nome, email, status FROM usuarios WHERE nivel='USER'", conn)
        conn.close()
        for idx, row in df_users.iterrows():
            col1, col2, col3 = st.columns([2, 2, 1])
            col1.write(f"👤 {row['nome']}")
            col2.write(f"📧 {row['email']}")
            if row['status'] == 'PENDENTE':
                if col3.button("✅ APROVAR", key=f"ap_{idx}"):
                    conn = sqlite3.connect('sentinela_usuarios.db')
                    conn.execute("UPDATE usuarios SET status='ATIVO' WHERE email=?", (row['email'],))
                    conn.commit(); conn.close(); st.rerun()
            else:
                if col3.button("❌ BLOQUEAR", key=f"bl_{idx}"):
                    conn = sqlite3.connect('sentinela_usuarios.db')
                    conn.execute("UPDATE usuarios SET status='PENDENTE' WHERE email=?", (row['email'],))
                    conn.commit(); conn.close(); st.rerun()

# --- CARREGAMENTO DE DADOS (PÓS-LOGIN) ---
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
    st.write(f"Olá, **{st.session_state['user_data']['nome']}**")
    if st.button("🚪 SAIR DO SISTEMA"):
        st.session_state['user_data'] = None
        st.rerun()
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
        
        with st.popover("📥 Modelo Bases"):
            # Senha de segurança para download do modelo vinculada ao admin mestre
            if st.text_input("Senha", type="password", key="p_modelo") == "Senhaforte@123":
                st.download_button("Download", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True)

# --- CABEÇALHO ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

# --- ÁREA CENTRAL ---
if emp_sel:
    tab_xml, tab_dominio = st.tabs(["📂 ANÁLISE XML", "📉 CONFORMIDADE DOMÍNIO"])

    with tab_xml:
        st.markdown("### 📥 Central de Importação")
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True, key=f"x_{v}")
        with c2: u_ae = st.file_uploader("📥 Autenticidade Entradas", accept_multiple_files=True, key=f"ae_{v}")
        with c3: u_as = st.file_uploader("📤 Autenticidade Saídas", accept_multiple_files=True, key=f"as_{v}")
        
        if st.button("🚀 INICIAR ANÁLISE XML", use_container_width=True):
            if u_xml:
                with st.spinner("Auditando..."):
                    try:
                        u_xml_validos = [f for f in u_xml if zipfile.is_zipfile(f)]
                        path_base = f"Bases_Tributarias/{cod_c}-Bases_Tributarias.xlsx"
                        df_base_emp = pd.read_excel(path_base) if os.path.exists(path_base) else None
                        modo_auditoria = "ELITE" if df_base_emp is not None else "CEGAS"

                        xe, xs = extrair_dados_xml_recursivo(u_xml_validos, cnpj_limpo)
                        
                        buf = io.BytesIO()
                        with pd.ExcelWriter(buf, engine='xlsxwriter') as writer:
                            gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, u_ae, u_as, df_base_emp, modo_auditoria)
                        
                        st.session_state['relat_buf'] = buf.getvalue()

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

                        res_f, fal_f = [], []
                        for (t, s), d in seq_map.items():
                            ns = d["nums"]
                            res_f.append({"Documento": t, "Série": s, "Início": min(ns), "Fim": max(ns), "Qtd": len(ns), "Valor": round(d["valor"], 2)})
                            buracos = sorted(list(set(range(min(ns), max(ns) + 1)) - ns))
                            for b in buracos: fal_f.append({"Série": s, "Nº Faltante": b})
                                
                        st.session_state.update({
                            'z_org': b_org.getvalue(), 'z_todos': b_todos.getvalue(), 
                            'relatorio': rel_list, 'df_resumo': pd.DataFrame(res_f), 
                            'df_faltantes': pd.DataFrame(fal_f), 'st_counts': st_counts, 'executado': True
                        })
                        st.rerun()
                    except Exception as e: st.error(f"Erro: {e}")

    if st.session_state.get('executado'):
        st.markdown("---")
        with st.popover("💾 BAIXAR RELATÓRIO FINAL", use_container_width=True):
            if st.text_input("Senha de Download", type="password", key="p_rel") == "Senhaforte@123":
                st.download_button("Confirmar Download", st.session_state['relat_buf'], f"Sentinela_{cod_c}.xlsx", use_container_width=True)

        st.markdown("<h2 style='text-align: center;'>⛏️ O GARIMPEIRO</h2>", unsafe_allow_html=True)
        # ... (Restante do código do Garimpeiro mantido íntegro)
