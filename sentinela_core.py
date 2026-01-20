import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os
from datetime import datetime

try:
    from audit_resumo import gerar_aba_resumo
    from Auditorias.audit_icms import processar_icms
    from Auditorias.audit_ipi import processar_ipi
    from Auditorias.audit_pis_cofins import processar_pc
    # Importação do seu motor de apuração
    from Apuracoes.apuracao_difal import gerar_resumo_uf
except ImportError as e:
    st.error(f"⚠️ Erro de Dependência: {e}")

# ... (Funções safe_float, buscar_tag_recursiva, tratar_ncm_texto e processar_conteudo_xml mantidas iguais)

def extrair_dados_xml_recursivo(files, cnpj_auditado):
    dados = []
    if not files: return pd.DataFrame(), pd.DataFrame()
    def ler_zip(zip_data):
        with zipfile.ZipFile(zip_data) as z:
            for n in z.namelist():
                if n.lower().endswith('.xml'):
                    with z.open(n) as f: processar_conteudo_xml(f.read(), dados, cnpj_auditado)
    for f in files:
        f.seek(0)
        if f.name.endswith('.xml'): processar_conteudo_xml(f.read(), dados, cnpj_auditado)
        elif f.name.endswith('.zip'): ler_zip(f)
    df = pd.DataFrame(dados)
    if df.empty: return pd.DataFrame(), pd.DataFrame()
    return df[df['TIPO_SISTEMA'] == "ENTRADA"].copy(), df[df['TIPO_SISTEMA'] == "SAIDA"].copy()

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, df_base_emp=None, modo_auditoria=None):
    try: gerar_aba_resumo(writer)
    except: pass
    
    if not df_xs.empty:
        # Auditorias que criam abas próprias (ICMS, IPI, PIS/COFINS)
        processar_icms(df_xs, writer, cod_cliente, df_xe)
        processar_ipi(df_xs, writer, cod_cliente)
        processar_pc(df_xs, writer, cod_cliente, regime)
        
        # --- CRIAÇÃO ÚNICA DA ABA NO SISTEMA ---
        workbook = writer.book
        nome_aba = 'RESUMO_DIFAL_ST' # Nome atualizado conforme a dica
        worksheet = workbook.add_worksheet(nome_aba)
        writer.sheets[nome_aba] = worksheet
        
        # Chama o seu código especialista para preencher a aba que acabamos de criar
        try:
            gerar_resumo_uf(df_xs, writer, df_xe)
        except Exception as e:
            st.error(f"Erro no preenchimento do DIFAL: {e}")
