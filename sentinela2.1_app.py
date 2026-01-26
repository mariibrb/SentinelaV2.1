import streamlit as st
import os
import io
import pandas as pd
import zipfile
import re
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from hashlib import sha256
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final

# --- CONFIGURAÇÃO DE E-MAIL (FUNCIONALIDADE GMAIL) ---
def enviar_email(destinatario, assunto, corpo):
    remetente = "marii.brbj@gmail.com"
    senha_app = "odmurqgqpamjlaog" 
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha_app)
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False

# --- CONFIGURAÇÃO DE SEGURANÇA E BANCO DE DATOS ---
def init_db():
    conn = sqlite3.connect('sentinela_usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                 (nome TEXT, usuario TEXT, email TEXT PRIMARY KEY, senha TEXT, status TEXT, nivel TEXT,
                  perm_xml INTEGER DEFAULT 1, perm_icms INTEGER DEFAULT 0, perm_difal INTEGER DEFAULT 0,
                  perm_pis INTEGER DEFAULT 0, perm_ret INTEGER DEFAULT 0)''')
    
    c.execute("PRAGMA table_info(usuarios)")
    colunas_atuais = [col[1] for col in c.fetchall()]
    colunas_novas = {'usuario': 'TEXT', 'perm_xml': 'INTEGER DEFAULT 1', 'perm_icms': 'INTEGER DEFAULT 0',
                     'perm_difal': 'INTEGER DEFAULT 0', 'perm_pis': 'INTEGER DEFAULT 0', 'perm_ret': 'INTEGER DEFAULT 0'}
    for col_nome, col_tipo in colunas_novas.items():
        if col_nome not in colunas_atuais:
            c.execute(f"ALTER TABLE usuarios ADD COLUMN {col_nome} {col_tipo}")
    
    email_admin = 'marii.brbj@gmail.com'
    senha_mestre = sha256("Senhaforte@123".encode()).hexdigest()
    c.execute("SELECT * FROM usuarios WHERE usuario='mariana' OR email=?", (email_admin,))
    if not c.fetchone():
        c.execute("""INSERT INTO usuarios (nome, usuario, email, senha, status, nivel, perm_xml, perm_icms, perm_difal, perm_pis, perm_ret) 
                     VALUES (?, ?, ?, ?, 'ATIVO', 'ADMIN', 1, 1, 1, 1, 1)""", 
                  ('Mariana', 'mariana', email_admin, senha_mestre))
    conn.commit(); conn.close()

def hash_senha(senha):
    return sha256(senha.encode()).hexdigest()

# --- MOTOR GARIMPEIRO ---
def identify_xml_info(content_bytes, client_cnpj, file_name):
    client_cnpj_clean = "".join(filter(str.isdigit, str(client_cnpj))) if client_cnpj else ""
    nome_puro = os.path.basename(file_name)
    if nome_puro.startswith('.') or nome_puro.startswith('~') or not nome_puro.lower().endswith('.xml'):
        return None, False
    resumo = {"Arquivo": nome_puro, "Chave": "", "Tipo": "Outros", "Série": "0", "Número": 0, "Status": "NORMAIS", "Pasta": "RECEBIDOS_TERCEIROS/OUTROS", "Valor": 0.0, "Conteúdo": content_bytes}
    try:
        content_str = content_bytes[:30000].decode('utf-8', errors='ignore')
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
        elif '<inutnfe' in tag_l or '<procinut' in tag_l: status = "INUTILIZADOS"; tipo = "Inutilizacoes"
        resumo["Tipo"] = tipo; resumo["Status"] = status
        serie_match = re.search(r'<(?:serie)>(\d+)</', tag_l)
        resumo["Série"] = serie_match.group(1) if serie_match else "0"
        n_match = re.search(r'<(?:nnf|nct|nmdf|nnfini)>(\d+)</', tag_l)
        resumo["Número"] = int(n_match.group(1)) if n_match else 0
        if status == "NORMAIS":
            v_match = re.search(r'<(?:vnf|vtprest)>([\d.]+)</', tag_l)
            if not v_match: v_match = re.search(r'<vprod>([\d.]+)</vprod>', tag_l)
            resumo["Valor"] = float(v_match.group(1)) if v_match else 0.0
        cnpj_emit_match = re.search(r'<cnpj>(\d+)</cnpj>', tag_l)
        cnpj_emit = cnpj_emit_match.group(1) if cnpj_emit_match else ""
        is_p = (cnpj_emit == client_cnpj_clean) or (resumo["Chave"] and client_cnpj_clean in resumo["Chave"][6:20])
        resumo["Pasta"] = f"EMITIDOS_CLIENTE/{tipo}/{status}/Serie_{resumo['Série']}" if is_p else f"RECEBIDOS_TERCEIROS/{tipo}"
        return resumo, is_p
    except Exception: return None, False

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sentinela 2.4.0 | Auditoria Fiscal", page_icon="🧡", layout="wide")

st.markdown("""
    <style>
    .stAppHeader {display: none !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    .block-container {padding-top: 1rem !important;}
    [data-testid="stSidebar"] div.stImage { margin-top: -65px !important; margin-bottom: -55px !important; padding: 0px !important; }
    </style>
    """, unsafe_allow_html=True)

aplicar_estilo_sentinela()
init_db()

# Session States Originais
if 'user_data' not in st.session_state: st.session_state['user_data'] = None
if 'v_ver' not in st.session_state: st.session_state['v_ver'] = 0
if 'executado' not in st.session_state: st.session_state['executado'] = False
if 'show_adm' not in st.session_state: st.session_state['show_adm'] = False
if 'change_pass_mode' not in st.session_state: st.session_state['change_pass_mode'] = False

# --- TELA DE ACESSO (Restaurada) ---
if not st.session_state['user_data']:
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        aba_l, aba_c, aba_r = st.tabs(["🔐 ACESSAR SISTEMA", "📝 SOLICITAR ACESSO", "🔑 ESQUECI SENHA"])
        with aba_l:
            with st.container(border=True):
                if st.session_state['change_pass_mode']:
                    st.warning("🛡️ SEGURANÇA: Defina uma nova senha.")
                    nova_s = st.text_input("Nova Senha", type="password")
                    conf_s = st.text_input("Confirme a Nova Senha", type="password")
                    if st.button("SALVAR E ACESSAR"):
                        if nova_s == conf_s and len(nova_s) >= 4:
                            conn = sqlite3.connect('sentinela_usuarios.db')
                            conn.execute("UPDATE usuarios SET senha=? WHERE email=?", (hash_senha(nova_s), st.session_state['temp_email']))
                            conn.commit(); conn.close(); st.session_state['change_pass_mode'] = False; st.rerun()
                else:
                    login_in = st.text_input("Usuário ou E-mail")
                    pass_l = st.text_input("Senha", type="password")
                    if st.button("ENTRAR NO SISTEMA", use_container_width=True):
                        conn = sqlite3.connect('sentinela_usuarios.db'); c = conn.cursor()
                        c.execute("SELECT nome, usuario, email, status, nivel, perm_xml, perm_icms, perm_difal, perm_pis, perm_ret FROM usuarios WHERE (usuario=? OR email=?) AND senha=?", (login_in, login_in, hash_senha(pass_l)))
                        user = c.fetchone(); conn.close()
                        if user and user[3] == 'ATIVO':
                            st.session_state['user_data'] = {"nome": user[0], "usuario": user[1], "email": user[2], "nivel": user[4], "perms": {"xml": user[5], "icms": user[6], "difal": user[7], "pis": user[8], "ret": user[9]}}
                            st.rerun()
    st.stop()

# --- TÍTULO PRINCIPAL ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.4.0</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

# --- SIDEBAR OPERACIONAL ---
modo_adm = st.session_state.get('show_adm', False)
@st.cache_data(ttl=600)
def carregar_clientes():
    p_lista = ["Clientes Ativos.xlsx", ".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx"]
    for p in p_lista:
        if os.path.exists(p):
            df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
            df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x)))); return df
    return pd.DataFrame()

df_cli = carregar_clientes(); v = st.session_state['v_ver']

with st.sidebar:
    for logo_p in ["logo.png", "streamlit/logo.png", ".streamlit/logo.png"]:
        if os.path.exists(logo_p): st.image(logo_p, use_container_width=True); break
    st.markdown("---")
    st.write(f"👤 Olá, **{st.session_state['user_data']['nome']}**")
    if st.session_state['user_data']['nivel'] == 'ADMIN':
        if st.button("🛠️ ABRIR GESTÃO ADMINISTRATIVA" if not modo_adm else "❌ FECHAR PAINEL ADM", use_container_width=True):
            st.session_state['show_adm'] = not modo_adm; st.rerun()
    if st.button("🚪 SAIR DO SISTEMA", use_container_width=True): st.session_state.clear(); st.rerun()
    st.markdown("---")
    if not modo_adm:
        emp_sel = st.selectbox("Passo 1: Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="f_emp")
        if emp_sel:
            reg_sel = st.selectbox("Passo 2: Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"])
            seg_sel = st.selectbox("Passo 3: Segmento", ["", "Comércio", "Indústria", "Equiparado"])
            ret_sel = st.toggle("Passo 4: Habilitar MG (RET)")
            cod_c = emp_sel.split(" - ")[0].strip(); dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]; cnpj_limpo = dados_e['CNPJ']
            st.markdown(f'<div class="status-container-mariana"><b>🔍 Analisando:</b><br>{dados_e["RAZÃO SOCIAL"]}<br><b>CNPJ:</b> {cnpj_limpo}</div>', unsafe_allow_html=True)
            path_base = f"Bases_Tributarias/{cod_c}-Bases_Tributarias.xlsx"
            st.success("💎 Modo Elite: Base Localizada") if os.path.exists(path_base) else st.warning("🔍 Modo Cegas: Base não localizada")
            if ret_sel:
                st.success("💎 Modo Elite: Base RET Localizada") if os.path.exists(f"RET/{cod_c}-RET_MG.xlsx") else st.warning("🔍 Modo Cegas: Base RET não localizada")
            with st.popover("📥 Modelo Bases", use_container_width=True):
                if st.text_input("Senha", type="password", key="p_modelo") == "Senhaforte@123":
                    st.download_button("Baixar Modelo", pd.DataFrame().to_csv(), "modelo.xlsx", use_container_width=True)

# --- ÁREA CENTRAL (NAVEGAÇÃO POR RÁDIO HORIZONTAL - ORIGINAL) ---
if emp_sel and not modo_adm:
    perms = st.session_state['user_data']['perms']
    modulos_disponiveis = []
    if perms.get('xml'): modulos_disponiveis.append("GARIMPEIRO")
    modulos_disponiveis.extend(["CONCILIADOR", "AUDITOR", "ESPELHO"])
    
    modulo_atual = st.radio("Selecione o Módulo:", modulos_disponiveis, horizontal=True, label_visibility="collapsed")
    st.markdown("---")

    if modulo_atual == "GARIMPEIRO":
        st.markdown('<div id="modulo-xml"></div>', unsafe_allow_html=True)
        st.markdown("### 📥 Central de Importação e Garimpo")
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 ZIP XML", accept_multiple_files=True, key=f"x_{v}")
        with c2: u_ae = st.file_uploader("📥 Autenticidade Entradas", accept_multiple_files=True, key=f"ae_{v}")
        with c3: u_as = st.file_uploader("📤 Autenticidade Saídas", accept_multiple_files=True, key=f"as_{v}")
        
        if st.button("🚀 INICIAR GARIMPEIRO", use_container_width=True):
            if u_xml:
                with st.spinner("Auditando..."):
                    u_validos = [f for f in u_xml if zipfile.is_zipfile(f)]
                    xe, xs = extrair_dados_xml_recursivo(u_validos, cnpj_limpo)
                    buf = io.BytesIO()
                    with pd.ExcelWriter(buf, engine='xlsxwriter') as writer:
                        gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, u_ae, u_as, None, "CEGAS")
                    st.session_state['relat_buf'] = buf.getvalue()
                    
                    p_keys, rel_list, seq_map, st_counts = set(), [], {}, {"CANCELADOS": 0, "INUTILIZADOS": 0}
                    b_org, b_todos = io.BytesIO(), io.BytesIO()
                    with zipfile.ZipFile(b_org, "w") as z_org, zipfile.ZipFile(b_todos, "w") as z_todos:
                        for zf in u_validos:
                            zf.seek(0)
                            with zipfile.ZipFile(zf) as zi:
                                for name in zi.namelist():
                                    if name.lower().endswith('.xml'):
                                        xml_d = zi.read(name)
                                        res, is_p = identify_xml_info(xml_d, cnpj_limpo, name)
                                        if res and res["Chave"] not in p_keys:
                                            p_keys.add(res["Chave"])
                                            z_org.writestr(f"{res['Pasta']}/{name}", xml_d); z_todos.writestr(name, xml_d)
                                            rel_list.append(res)
                                            if is_p:
                                                if res["Status"] in st_counts: st_counts[res["Status"]] += 1
                                                sk = (res["Tipo"], res["Série"])
                                                if sk not in seq_map: seq_map[sk] = {"nums": set(), "valor": 0.0}
                                                seq_map[sk]["nums"].add(res["Número"]); seq_map[sk]["valor"] += res["Valor"]
                    
                    res_f, fal_f = [], []
                    for (t, s), d in seq_map.items():
                        ns = d["nums"]
                        res_f.append({"Documento": t, "Série": s, "Início": min(ns), "Fim": max(ns), "Qtd": len(ns), "Valor": round(d["valor"], 2)})
                        for b in sorted(list(set(range(min(ns), max(ns) + 1)) - ns)): fal_f.append({"Série": s, "Nº Faltante": b})
                    st.session_state.update({'z_org': b_org.getvalue(), 'z_todos': b_todos.getvalue(), 'df_resumo': pd.DataFrame(res_f), 'df_faltantes': pd.DataFrame(fal_f), 'st_counts': st_counts, 'relatorio': rel_list, 'executado': True})
                    st.rerun()

        if st.session_state.get('executado'):
            st.markdown("---")
            st.write("### 📥 Área de Downloads")
            d1, d2, d3 = st.columns(3)
            with d1: st.download_button("💾 RELATÓRIO ANALISES", st.session_state['relat_buf'], "Analise.xlsx", use_container_width=True, type="primary")
            with d2: st.download_button("📂 ZIP SEPARADINHO", st.session_state['z_org'], "organizado.zip", use_container_width=True)
            with d3: st.download_button("📦 DOWNLOAD COMPLETO", st.session_state['z_todos'], "completo.zip", use_container_width=True)

    elif modulo_atual == "CONCILIADOR":
        st.markdown('<div id="modulo-amarelo"></div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; padding: 60px; background: rgba(255, 215, 0, 0.1); border: 2px dashed #FFD700; border-radius: 30px;">
                <h1 style="font-size: 80px; margin-bottom: 0px;">🕵️‍♀️</h1>
                <h2 style="color: #B8860B; font-weight: 800;">OPERAÇÃO PENTE FINO</h2>
                <p style="font-size: 20px; color: #555;"><b>Calma, Mariana!</b> Estamos treinando os robôs para o cruzamento <b>XML vs Domínio</b>.</p>
            </div>
        """, unsafe_allow_html=True)

    elif modulo_atual == "AUDITOR":
        st.markdown('<div id="modulo-conformidade"></div>', unsafe_allow_html=True)
        sub_auditor = ["💰 PIS/COFINS", "📊 ICMS/IPI", "⚖️ DIFAL/ST"]
        if ret_sel: sub_auditor.insert(2, "🏨 RET")
        tabs_auditor = st.tabs(sub_auditor)
        for j, nome_sub in enumerate(sub_auditor):
            with tabs_auditor[j]:
                st.markdown(f"#### Auditoria {nome_sub}")
                c1, c2 = st.columns(2)
                with c1: st.file_uploader("📑 Gerencial Domínio", type=['xlsx'], key=f"g_aud_{j}_{v}")
                with c2: st.button(f"🚀 INICIAR AUDITORIA {nome_sub}", use_container_width=True, key=f"btn_aud_{j}")

    elif modulo_atual == "ESPELHO":
        st.markdown('<div id="modulo-apuracao"></div>', unsafe_allow_html=True)
        st.tabs(["📊 Livro de Saídas", "📊 Livro de Entradas", "📉 Resumo Real vs Esperado"])

elif modo_adm:
    # Painel ADM Original...
    st.subheader("🛠️ GESTÃO DE USUÁRIOS")
    conn = sqlite3.connect('sentinela_usuarios.db'); df_u = pd.read_sql_query("SELECT * FROM usuarios", conn)
    st.dataframe(df_u, use_container_width=True); conn.close()
