import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os

try:
    from audit_resumo import gerar_aba_resumo
    from Auditorias.audit_icms import processar_icms
    from Auditorias.audit_ipi import processar_ipi
    from Auditorias.audit_pis_cofins import processar_pc
    # Importa o motor especialista
    from Apuracoes.apuracao_difal import gerar_resumo_uf
except ImportError as e:
    st.error(f"⚠️ Erro de Dependência: {e}")

# ... (Funções safe_float, buscar_tag_recursiva e processar_conteudo_xml mantidas íntegras)

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None):
    try: gerar_aba_resumo(writer)
    except: pass
    
    if not df_xs.empty:
        # Auditorias Padrão
        processar_icms(df_xs, writer, cod_cliente, df_xe)
        processar_ipi(df_xs, writer, cod_cliente)
        processar_pc(df_xs, writer, cod_cliente, regime)
        
        # --- O CORE CRIA A GUIA (ÚNICO RESPONSÁVEL) ---
        workbook = writer.book
        nome_aba = 'DIFAL_ST_FECP'
        worksheet = workbook.add_worksheet(nome_aba)
        writer.sheets[nome_aba] = worksheet
        
        # Chama o especialista para preencher a guia que acabamos de criar
        try:
            gerar_resumo_uf(df_xs, writer, df_xe)
        except Exception as e:
            st.error(f"Erro ao preencher dados de Difal: {e}")
