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

# --- CONFIGURAÇÃO DE SEGURANÇA E BANCO DE DATOS ---
def init_db():
    conn = sqlite3.connect('sentinela_usuarios.db')
    c = conn.cursor()
    
    # Criamos a tabela base caso não exista
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                 (nome TEXT, 
                  email TEXT PRIMARY KEY, 
                  senha TEXT, 
                  status TEXT, 
                  nivel TEXT)''')
    
    # Lógica de Migração de Colunas (Evita o KeyError: perm_icms)
    c.execute("PRAGMA table_info(usuarios)")
    colunas_atuais = [col[1] for col in c.fetchall()]
    
    colunas_novas = {
        'perm_icms': 'INTEGER DEFAULT 0',
        'perm_difal': 'INTEGER DEFAULT 0',
        'perm_pis': 'INTEGER DEFAULT 0',
        'perm_ret': 'INTEGER DEFAULT 0'
    }
    
    for col_nome, col_tipo in colunas_novas.items():
        if col_nome not in colunas_atuais:
            c.execute(f"ALTER TABLE usuarios ADD COLUMN {col_nome} {col_tipo}")
    
    # CONFIGURANDO MARIANA COMO ADMIN MESTRE
    email_admin = 'marii.brbj@gmail.com'
    nova_senha_hash = sha256("Senhaforte@123".encode()).hexdigest()
    
    c.execute("SELECT * FROM usuarios WHERE email=?", (email_admin,))
    if not c.fetchone():
        c.execute("""INSERT INTO usuarios 
                     (nome, email, senha, status, nivel, perm_icms, perm_difal, perm_pis, perm_ret) 
                     VALUES (?, ?, ?, 'ATIVO', 'ADMIN', 1, 1, 1, 1)""", 
                  ('mariana', email_admin, nova_senha_hash))
    else:
        # Garante que as permissões da Mariana estejam sempre no máximo e o nível seja ADMIN
        c.execute("""UPDATE usuarios 
                     SET nome='mariana', nivel='ADMIN', 
                         perm_icms=1, perm_difal=1, perm_pis=1, perm_ret=1 
                     WHERE email=?""", 
                  (email_admin,))
    
    conn.commit()
    conn.close()

def hash_senha(senha):
    return sha256(senha.encode()).hexdigest()

# --- MOTOR GARIMPEIRO (Lógica Íntegra e Detalhada) ---
def identify_xml_info(content_bytes, client_cnpj, file_name):
    client_cnpj_clean = "".join(filter(str.isdigit, str(client_cnpj))) if client_cnpj else ""
    nome_puro = os.path.basename(file_name)
    
    if nome_puro.startswith('.') or nome_puro.startswith('~') or not nome_puro.lower().endswith('.xml'):
        return None, False
    
    resumo = {
        "Arquivo": nome_puro, 
        "Chave": "", 
        "Tipo": "Outros", 
        "Série": "0",
        "Número": 0, 
        "Status": "NORMAIS", 
        "Pasta": "RECEBIDOS_TERCEIROS/OUTROS",
        "Valor": 0.0, 
        "Conteúdo": content_bytes
    }
    
    try:
        content_str = content_bytes[:30000].decode('utf-8', errors='ignore')
        match_ch = re.search(r'\d{44}', content_str)
        resumo["Chave"] = match_ch.group(0) if match_ch else ""
        
        tag_l = content_str.lower()
        tipo = "NF-e"
        
        if '<mod>65</mod>' in tag_l: 
            tipo = "NFC-e"
        elif '<infcte' in tag_l: 
            tipo = "CT-e"
        elif '<infmdfe' in tag_l: 
            tipo = "MDF-e"
        
        status = "NORMAIS"
        if '110111' in tag_l: 
            status = "CANCELADOS"
        elif '110110' in tag_l: 
            status = "CARTA_CORRECAO"
        elif '<inutnfe' in tag_l or '<procinut' in tag_l:
            status = "INUTILIZADOS"
            tipo = "Inutilizacoes"
            
        resumo["Tipo"] = tipo
        resumo["Status"] = status
        
        serie_match = re.search(r'<(?:serie)>(\d+)</', tag_l)
        resumo["Série"] = serie_match.group(1) if serie_match else "0"
        
        n_match = re.search(r'<(?:nnf|nct|nmdf|nnfini)>(\d+)</', tag_l)
        resumo["Número"] = int(n_match.group(1)) if n_match else 0
        
        if status == "NORMAIS":
            v_match = re.search(r'<(?:vnf|vtprest)>([\d.]+)</', tag_l)
            if not v_match:
                v_match = re.search(r'<vprod>([\d.]+)</vprod>', tag_l)
            resumo["Valor"] = float(v_match.group(1)) if v_match else 0.0
        
        cnpj_emit_match = re.search(r'<cnpj>(\d+)</cnpj>', tag_l)
        cnpj_emit = cnpj_emit_match.group(1) if cnpj_emit_match else ""
        
        is_p = (cnpj_emit == client_cnpj_clean) or (resumo["Chave"] and client_cnpj_clean in resumo["Chave"][6:20])
        
        if is_p:
            resumo["Pasta"] = f"EMITIDOS_CLIENTE/{tipo}/{status}/Serie_{resumo['Série']}"
        else:
            resumo["Pasta"] = f"RECEBIDOS_TERCEIROS/{tipo}"
            
        return resumo, is_p
    except Exception: 
        return None, False

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sentinela 2.1 | Auditoria Fiscal", 
    page_icon="🧡", 
    layout="wide"
)

aplicar_estilo_sentinela()
init_db()

st.markdown("""
    <style>
    .stAppHeader {display: none;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

if 'user_data' not in st.session_state: 
    st.session_state['user_data'] = None
if 'v_ver' not in st.session_state: 
    st.session_state['v_ver'] = 0
if 'executado' not in st.session_state: 
    st.session_state['executado'] = False

def limpar_central():
    st.session_state.clear()
    st.rerun()

# --- TELA DE ACESSO (LOGIN E SOLICITAÇÃO) ---
if not st.session_state['user_data']:
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        aba_l, aba_c = st.tabs(["🔐 ACESSAR SISTEMA", "📝 SOLICITAR ACESSO"])
        
        with aba_l:
            with st.container(border=True):
                u_input = st.text_input("Usuário ou E-mail")
                pass_l = st.text_input("Senha", type="password")
                if st.button("ENTRAR NO SISTEMA", use_container_width=True):
                    conn = sqlite3.connect('sentinela_usuarios.db')
                    c = conn.cursor()
                    c.execute("""SELECT nome, email, status, nivel, perm_icms, perm_difal, perm_pis, perm_ret 
                                 FROM usuarios 
                                 WHERE (nome=? OR email=?) AND senha=?""", 
                              (u_input, u_input, hash_senha(pass_l)))
                    user = c.fetchone()
                    conn.close()
                    
                    if user:
                        if user[2] == 'ATIVO':
                            st.session_state['user_data'] = {
                                "nome": user[0], 
                                "email": user[1], 
                                "nivel": user[3],
                                "perms": {
                                    "icms": user[4], 
                                    "difal": user[5], 
                                    "pis": user[6], 
                                    "ret": user[7]
                                }
                            }
                            st.rerun()
                        else:
                            st.warning("Seu acesso está em fase de análise administrativa.")
                    else:
                        st.error("Usuário ou senha inválidos.")
        
        with aba_c:
            with st.container(border=True):
                st.write("### Solicite seu acesso:")
                n_nome = st.text_input("Nome Completo")
                n_email = st.text_input("E-mail Profissional")
                n_pass = st.text_input("Defina uma Senha", type="password")
                if st.button("SOLICITAR LIBERAÇÃO", use_container_width=True):
                    if n_nome and n_email and n_pass:
                        try:
                            conn = sqlite3.connect('sentinela_usuarios.db')
                            conn.execute("""INSERT INTO usuarios 
                                            (nome, email, senha, status, nivel, perm_icms, perm_difal, perm_pis, perm_ret) 
                                            VALUES (?, ?, ?, 'PENDENTE', 'USER', 0, 0, 0, 0)""", 
                                         (n_nome, n_email, hash_senha(n_pass)))
                            conn.commit()
                            conn.close()
                            st.success("Solicitação enviada! Você será notificado após a análise do sistema.")
                        except Exception:
                            st.error("Este e-mail já está cadastrado ou possui pedido pendente.")
                    else:
                        st.warning("Por favor, preencha todos os campos obrigatórios.")
    st.stop()

# --- PAINEL DE ADMINISTRAÇÃO ELITE (MARIANA - COM EDIÇÃO) ---
if st.session_state['user_data']['nivel'] == 'ADMIN':
    with st.expander("🛠️ GESTÃO DE USUÁRIOS E PERMISSÕES (SISTEMA)", expanded=False):
        conn = sqlite3.connect('sentinela_usuarios.db')
        df_u = pd.read_sql_query("SELECT * FROM usuarios ORDER BY nivel ASC", conn)
        
        for idx, row in df_u.iterrows():
            is_me = (row['email'] == st.session_state['user_data']['email'])
            with st.container(border=True):
                c1, c2, c3, c4 = st.columns([2, 2, 3, 2])
                
                # --- Campos de Edição de Cadastro ---
                novo_nome = c1.text_input("Nome", value=row['nome'], key=f"nome_{idx}")
                novo_email_input = c1.text_input("E-mail", value=row['email'], key=f"mail_{idx}")
                
                # Controle de Status e Reset de Senha
                st_txt = "🟢 ATIVO" if row['status'] == 'ATIVO' else "🟡 PENDENTE"
                c2.write(f"Status Atual: {st_txt}")
                if c2.button("🔄 Reset Senha", key=f"rs_{idx}"):
                    conn.execute("UPDATE usuarios SET senha=? WHERE email=?", (hash_senha("123456"), row['email']))
                    conn.commit()
                    st.info(f"Senha resetada para: 123456")

                # Permissões Grânulares
                p_i = c3.checkbox("Audit ICMS/IPI", value=bool(row['perm_icms']), key=f"i_{idx}")
                p_d = c3.checkbox("Audit DIFAL/ST", value=bool(row['perm_difal']), key=f"d_{idx}")
                p_p = c3.checkbox("Audit PIS/COFINS", value=bool(row['perm_pis']), key=f"p_{idx}")
                p_r = c3.checkbox("Audit RET", value=bool(row['perm_ret']), key=f"r_{idx}")

                # Botões de Ação
                if not is_me:
                    if row['status'] == 'PENDENTE':
                        if c4.button("✅ LIBERAR", key=f"ok_{idx}", use_container_width=True):
                            conn.execute("""UPDATE usuarios 
                                            SET nome=?, email=?, status='ATIVO', perm_icms=?, perm_difal=?, perm_pis=?, perm_ret=? 
                                            WHERE email=?""", 
                                         (novo_nome, novo_email_input, int(p_i), int(p_d), int(p_p), int(p_r), row['email']))
                            conn.commit()
                            st.rerun()
                    else:
                        if c4.button("⛔ BLOQUEAR", key=f"bk_{idx}", use_container_width=True):
                            conn.execute("UPDATE usuarios SET status='PENDENTE' WHERE email=?", (row['email'],))
                            conn.commit()
                            st.rerun()
                    
                    if c4.button("🗑️ EXCLUIR", key=f"del_{idx}", use_container_width=True):
                        conn.execute("DELETE FROM usuarios WHERE email=?", (row['email'],))
                        conn.commit()
                        st.rerun()
                    
                    # Botão Salvar para usuários comuns
                    if c4.button("💾 SALVAR ALTERAÇÕES", key=f"save_{idx}", use_container_width=True, type="primary"):
                        conn.execute("""UPDATE usuarios 
                                        SET nome=?, email=?, perm_icms=?, perm_difal=?, perm_pis=?, perm_ret=? 
                                        WHERE email=?""", 
                                     (novo_nome, novo_email_input, int(p_i), int(p_d), int(p_p), int(p_r), row['email']))
                        conn.commit()
                        st.success("Cadastro atualizado!")
                else:
                    c4.write("🛡️ Conta Mestre Protegida")
                    if c4.button("💾 ATUALIZAR MEU PERFIL", key=f"save_me_{idx}", use_container_width=True, type="primary"):
                        conn.execute("""UPDATE usuarios 
                                        SET nome=?, email=?, perm_icms=?, perm_difal=?, perm_pis=?, perm_ret=? 
                                        WHERE email=?""", 
                                     (novo_nome, novo_email_input, int(p_i), int(p_d), int(p_p), int(p_r), row['email']))
                        conn.commit()
                        st.session_state['user_data']['nome'] = novo_nome
                        st.session_state['user_data']['email'] = novo_email_input
                        st.success("Seu perfil foi atualizado!")
        conn.close()

# --- CARREGAMENTO DE CLIENTES ---
@st.cache_data(ttl=600)
def carregar_clientes():
    p_lista = ["Clientes Ativos.xlsx", ".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx"]
    for p in p_lista:
        if os.path.exists(p):
            try:
                df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except Exception:
                continue
    return pd.DataFrame()

df_cli = carregar_clientes()
v = st.session_state['v_ver']

# --- SIDEBAR ---
with st.sidebar:
    if os.path.exists(".streamlit/Sentinela.png"):
        st.image(".streamlit/Sentinela.png", use_container_width=True)
    st.markdown("---")
    st.write(f"👤 Olá, **{st.session_state['user_data']['nome']}**")
    if st.button("🚪 SAIR DO SISTEMA", use_container_width=True):
        st.session_state.clear()
        st.rerun()
    st.markdown("---")
    
    emp_sel = st.selectbox("Passo 1: Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="f_emp")
    
    if emp_sel:
        reg_sel = st.selectbox("Passo 2: Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="f_reg")
        seg_sel = st.selectbox("Passo 3: Segmento", ["", "Comércio", "Indústria", "Equiparado"], key="f_seg")
        ret_sel = st.toggle("Passo 4: Habilitar MG (RET)", key="f_ret")
        
        cod_c = emp_sel.split(" - ")[0].strip()
        dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
        cnpj_limpo = "".join(filter(str.isdigit, str(dados_e['CNPJ'])))
        st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}</div>", unsafe_allow_html=True)
        
        path_base = f"Bases_Tributarias/{cod_c}-Bases_Tributarias.xlsx"
        if os.path.exists(path_base):
            st.success("💎 Modo Elite: Base Localizada")
        else:
            st.warning("🔍 Modo Cegas: Base não localizada")
            
        with st.popover("📥 Modelo Bases", use_container_width=True):
            if st.text_input("Senha", type="password", key="p_modelo") == "Senhaforte@123":
                st.download_button("Baixar Modelo", pd.DataFrame().to_csv(), "modelo.csv", use_container_width=True)

# --- CABEÇALHO ---
st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)

# --- ÁREA CENTRAL ---
if emp_sel:
    perms = st.session_state['user_data']['perms']
    abas_v = ["📂 ANÁLISE XML"]
    if perms['icms']: abas_v.append("📊 ICMS/IPI")
    if perms['difal']: abas_v.append("⚖️ DIFAL/ST")
    if perms['ret']: abas_v.append("🏨 RET")
    if perms['pis']: abas_v.append("💰 PIS/COFINS")
    
    tabs = st.tabs(abas_v)

    # --- ABA XML (O GARIMPEIRO INTEGRAL) ---
    with tabs[0]:
        st.markdown("### 📥 Central de Importação e Garimpo")
        c1, c2, c3 = st.columns(3)
        with c1: u_xml = st.file_uploader("📁 XML (ZIP)", accept_multiple_files=True, key=f"x_{v}")
        with c2: u_ae = st.file_uploader("📥 Autenticidade Entradas", accept_multiple_files=True, key=f"ae_{v}")
        with c3: u_as = st.file_uploader("📤 Autenticidade Saídas", accept_multiple_files=True, key=f"as_{v}")
        
        if st.button("🚀 INICIAR ANÁLISE XML", use_container_width=True):
            if u_xml:
                with st.spinner("Auditando..."):
                    try:
                        u_validos = [f for f in u_xml if zipfile.is_zipfile(f)]
                        df_base_emp = pd.read_excel(path_base) if os.path.exists(path_base) else None
                        xe, xs = extrair_dados_xml_recursivo(u_validos, cnpj_limpo)
                        
                        buf = io.BytesIO()
                        with pd.ExcelWriter(buf, engine='xlsxwriter') as writer:
                            gerar_excel_final(xe, xs, cod_c, writer, reg_sel, ret_sel, u_ae, u_as, df_base_emp, "ELITE" if df_base_emp is not None else "CEGAS")
                        
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
                                                z_org.writestr(f"{res['Pasta']}/{name}", xml_d)
                                                z_todos.writestr(name, xml_d)
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
                            for b in sorted(list(set(range(min(ns), max(ns) + 1)) - ns)):
                                fal_f.append({"Série": s, "Nº Faltante": b})
                        
                        st.session_state.update({
                            'z_org': b_org.getvalue(), 
                            'z_todos': b_todos.getvalue(), 
                            'df_resumo': pd.DataFrame(res_f), 
                            'df_faltantes': pd.DataFrame(fal_f), 
                            'st_counts': st_counts, 
                            'relatorio': rel_list, 
                            'executado': True
                        })
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro no Processamento: {e}")

    # --- ABAS DE CONFORMIDADE RESTAURADAS ---
    idx_aba = 1
    if perms['icms']:
        with tabs[idx_aba]:
            st.markdown("#### 📊 Auditoria ICMS/IPI")
            c1, c2 = st.columns(2)
            with c1: st.file_uploader("📑 Gerencial Saídas", type=['xlsx'], key=f"icms_s_{v}")
            with c2: st.file_uploader("📑 Gerencial Entradas", type=['xlsx'], key=f"icms_e_{v}")
            st.button("⚖️ CRUZAR ICMS/IPI", use_container_width=True, key="btn_icms")
        idx_aba += 1
    
    if perms['difal']:
        with tabs[idx_aba]:
            st.markdown("#### ⚖️ Auditoria Difal / ST / FECP")
            c1, c2, c3 = st.columns(3)
            with c1: st.file_uploader("📑 Gerencial Saídas", type=['xlsx'], key=f"dif_s_{v}")
            with c2: st.file_uploader("📑 Gerencial Entradas", type=['xlsx'], key=f"dif_e_{v}")
            with c3: st.file_uploader("📄 Demonstrativo DIFAL", type=['xlsx'], key=f"dom_dif_{v}")
            st.button("⚖️ CRUZAR DIFAL/ST", use_container_width=True, key="btn_difal")
        idx_aba += 1

    if perms['ret']:
        with tabs[idx_aba]:
            st.markdown("#### 🏨 Auditoria RET")
            if ret_sel:
                c1, c2, c3 = st.columns(3)
                with c1: st.file_uploader("📑 Gerencial Saídas", type=['xlsx'], key=f"ret_s_{v}")
                with c2: st.file_uploader("📑 Gerencial Entradas", type=['xlsx'], key=f"ret_e_{v}")
                with c3: st.file_uploader("📄 Demonstrativo RET", type=['xlsx'], key=f"dom_ret_{v}")
                st.button("⚖️ VALIDAR RET", use_container_width=True, key="btn_ret")
            else:
                st.warning("⚠️ Habilite o RET na Sidebar para este módulo.")
        idx_aba += 1

    if perms['pis']:
        with tabs[idx_aba]:
            st.markdown("#### 💰 Auditoria PIS/Cofins")
            c1, c2, c3 = st.columns(3)
            with c1: st.file_uploader("📑 Gerencial Saídas", type=['xlsx'], key=f"pis_s_{v}")
            with c2: st.file_uploader("📑 Gerencial Entradas", type=['xlsx'], key=f"pis_e_{v}")
            with c3: st.file_uploader("📄 Demonstrativo PIS/COFINS", type=['xlsx'], key=f"dom_pisc_{v}")
            st.button("⚖️ CRUZAR PIS/COFINS", use_container_width=True, key="btn_pis")

    # --- RESULTADOS E DOWNLOADS ---
    if st.session_state.get('executado'):
        st.markdown("---")
        with st.popover("📥 ACESSAR DOWNLOADS SEGUROS", use_container_width=True):
            if st.text_input("Senha", type="password", key="p_down") == "Senhaforte@123":
                st.download_button("💾 RELATÓRIO FINAL EXCEL", st.session_state['relat_buf'], f"Sentinela_{cod_c}.xlsx", use_container_width=True)
                st.download_button("📂 ZIP ORGANIZADO", st.session_state['z_org'], "garimpo_pastas.zip", use_container_width=True)
        
        st.markdown("<h2 style='text-align: center;'>⛏️ O GARIMPEIRO</h2>", unsafe_allow_html=True)
        sc = st.session_state.get('st_counts')
        c1, c2, c3 = st.columns(3)
        c1.metric("📦 VOLUME TOTAL", len(st.session_state.get('relatorio', [])))
        c2.metric("❌ CANCELADAS", sc.get("CANCELADOS", 0))
        c3.metric("🚫 INUTILIZADAS", sc.get("INUTILIZADOS", 0))
        
        cr, cf = st.columns(2)
        with cr:
            st.write("**Resumo por Série:**")
            st.dataframe(st.session_state['df_resumo'], use_container_width=True, hide_index=True)
        with cf:
            st.write("**Notas Faltantes na Sequência:**")
            st.dataframe(st.session_state['df_faltantes'], use_container_width=True, hide_index=True)
else:
    st.info("👈 Selecione a empresa na barra lateral para começar.")
