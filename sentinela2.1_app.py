import streamlit as st
import os, io, pandas as pd, zipfile, re, random
from style import aplicar_estilo_sentinela
from sentinela_core import extrair_dados_xml_recursivo, gerar_excel_final
from Apuracoes.apuracao_difal import gerar_resumo_uf 

# --- MOTOR GARIMPEIRO (Lógica Íntegra Original de Identificação) ---
def identify_xml_info(content_bytes, client_cnpj, file_name):
    """
    Identifica o tipo de XML (NFe, CTe, NFCe), status e organiza em pastas.
    Lógica fundamental para a integridade da mineração.
    """
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
            
        resumo["Tipo"] = tipo
        resumo["Status"] = status
        resumo["Série"] = re.search(r'<(?:serie)>(\d+)</', tag_l).group(1) if re.search(r'<(?:serie)>(\d+)</', tag_l) else "0"
        
        n_match = re.search(r'<(?:nnf|nct|nmdf|nnfini)>(\d+)</', tag_l)
        resumo["Número"] = int(n_match.group(1)) if n_match else 0
        
        if status == "NORMAIS":
            v_match = re.search(r'<(?:vnf|vtprest)>([\d.]+)</', tag_l)
            resumo["Valor"] = float(v_match.group(1)) if v_match else 0.0
        
        # Identifica se o XML pertence ao cliente auditado
        cnpj_emit = re.search(r'<cnpj>(\d+)</cnpj>', tag_l).group(1) if re.search(r'<cnpj>(\d+)</cnpj>', tag_l) else ""
        is_p = (cnpj_emit == client_cnpj_clean) or (resumo["Chave"] and client_cnpj_clean in resumo["Chave"][6:20])
        
        resumo["Pasta"] = f"EMITIDOS_CLIENTE/{tipo}/{status}/Serie_{resumo['Série']}" if is_p else f"RECEBIDOS_TERCEIROS/{tipo}"
        return resumo, is_p
    except: 
        return None, False

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Sentinela 2.1 | Auditoria Fiscal", page_icon="🧡", layout="wide")
aplicar_estilo_sentinela()

if 'v_ver' not in st.session_state: st.session_state['v_ver'] = 0
if 'executado' not in st.session_state: st.session_state['executado'] = False

def limpar_central():
    st.session_state.clear()
    st.rerun()

@st.cache_data(ttl=600)
def carregar_clientes():
    """Busca o arquivo de clientes em múltiplos caminhos possíveis."""
    for p in [".streamlit/Clientes Ativos.xlsx", "streamlit/Clientes Ativos.xlsx", "Clientes Ativos.xlsx"]:
        if os.path.exists(p):
            try:
                df = pd.read_excel(p).dropna(subset=['CÓD', 'RAZÃO SOCIAL'])
                df['CÓD'] = df['CÓD'].apply(lambda x: str(int(float(x))))
                return df
            except: continue
    return pd.DataFrame()

df_cli = carregar_clientes()

# --- SIDEBAR (Com Travas de Segurança e Foto do Garimpeiro) ---
with st.sidebar:
    logo_path = ".streamlit/Sentinela.png" if os.path.exists(".streamlit/Sentinela.png") else "streamlit/Sentinela.png"
    if os.path.exists(logo_path): st.image(logo_path, use_container_width=True)
    
    st.markdown("---")
    # Passo 1: Seleção de Empresa (Obrigatório)
    emp_sel = st.selectbox("Passo 1: Empresa", [""] + [f"{l['CÓD']} - {l['RAZÃO SOCIAL']}" for _, l in df_cli.iterrows()], key="f_emp")
    
    # BLOQUEIO: Só libera os passos seguintes se o Passo 1 estiver preenchido
    if emp_sel:
        reg_sel = st.selectbox("Passo 2: Regime Fiscal", ["", "Lucro Real", "Lucro Presumido", "Simples Nacional", "MEI"], key="f_reg")
        
        # BLOQUEIO: Só libera Passo 3 se tiver regime
        if reg_sel:
            seg_sel = st.selectbox("Passo 3: Segmento", ["", "Comércio", "Indústria", "Equiparado"], key="f_seg")
            ret_sel = st.toggle("Passo 4: Habilitar MG (RET)", key="f_ret")
            
            st.markdown("---")
            cod_c = emp_sel.split(" - ")[0].strip()
            dados_e = df_cli[df_cli['CÓD'] == cod_c].iloc[0]
            cnpj_limpo = "".join(filter(str.isdigit, str(dados_e['CNPJ'])))
            
            st.markdown(f"<div class='status-container'>📍 <b>Analisando:</b><br>{dados_e['RAZÃO SOCIAL']}</div>", unsafe_allow_html=True)
            
            # Verificação de Bases Locais
            path_base = f"Bases_Tributarias/{cod_c}-Bases_Tributarias.xlsx"
            if os.path.exists(path_base): st.success("💎 Modo Elite: Base Localizada")
            else: st.warning("🔍 Modo Cegas: Base não localizada")
                # --- CABEÇALHO ---
c_t, c_r = st.columns([4, 1])
with c_t: 
    st.markdown("<div class='titulo-principal'>SENTINELA 2.1</div><div class='barra-laranja'></div>", unsafe_allow_html=True)
with c_r:
    if st.button("🔄 LIMPAR TUDO"): limpar_central()

# --- ÁREA DE TRABALHO (Apenas se configurado no Sidebar) ---
if emp_sel and reg_sel:
    # RESTAURADO: Abas de Organização para facilitar a visualização
    tab_xml, tab_dominio = st.tabs(["📂 Garimpeiro: XMLs", "📄 Relatórios Domínio"])
    
    with tab_xml:
        xml_files = st.file_uploader("Arraste ZIPs ou XMLs", accept_multiple_files=True, type=['zip', 'xml'], key="up_xml")
        if xml_files:
            st.info(f"📊 {len(xml_files)} arquivos prontos para mineração.")
            
    with tab_dominio:
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            ae = st.file_uploader("Autorização de Entradas (Excel/CSV)", type=['xlsx', 'csv'], key="up_ae")
        with col_d2:
            as_f = st.file_uploader("Autorização de Saídas (Excel/CSV)", type=['xlsx', 'csv'], key="up_as")

    # --- BOTÃO DE EXECUÇÃO ---
    if st.button("🚀 INICIAR AUDITORIA COMPLETA", use_container_width=True):
        if not xml_files:
            st.error("⚠️ O Garimpeiro não pode trabalhar sem arquivos XML!")
        else:
            try:
                with st.status("🔍 Garimpeiro em ação: Minerando e Auditando...", expanded=True) as status:
                    # 1. Extração Recursiva
                    st.write("📦 Minerando dados e processando pastas...")
                    df_xe, df_xs = extrair_dados_xml_recursivo(xml_files, cnpj_limpo)
                    
                    if df_xe.empty and df_xs.empty:
                        st.error("❌ Nenhum dado foi localizado nos arquivos enviados.")
                        st.stop()
                    
                    # 2. Geração do Relatório via Core
                    st.write("📊 Construindo planilhas e aba DIFAL_ST_FECP...")
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        gerar_excel_final(
                            df_xe, df_xs, cod_c, writer, reg_sel, 
                            ret_sel, ae, as_f, df_base_emp=None, modo_auditoria="Completa"
                        )
                    
                    processed_data = output.getvalue()
                    status.update(label="✅ Processamento Concluído!", state="complete")

                # --- DOWNLOAD ---
                st.balloons()
                st.success(f"✨ Auditoria de {dados_e['RAZÃO SOCIAL']} finalizada com sucesso!")
                
                st.download_button(
                    label="📥 BAIXAR RELATÓRIO DE AUDITORIA",
                    data=processed_data,
                    file_name=f"SENTINELA_2.1_{cod_c}_{cnpj_limpo}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"❌ Erro Crítico no Processamento: {e}")
                st.exception(e)
else:
    # ESTÉTICA: Mensagem central se nada estiver selecionado
    st.markdown("""
        <div style='text-align: center; padding: 50px; border: 2px dashed #FFB6C1; border-radius: 20px; color: #888;'>
            <h3>🌸 Bem-vinda ao Sentinela 2.1</h3>
            <p>Por favor, utilize a barra lateral à esquerda para selecionar a empresa e o regime fiscal.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Sentinela V2.1 | Inteligência Fiscal Recursiva 🧡")
