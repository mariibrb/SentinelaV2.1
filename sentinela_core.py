import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os

# --- IMPORTAÇÃO DOS MÓDULOS ESPECIALISTAS ---
try:
    from audit_resumo import gerar_aba_resumo             # Aba: RESUMO
    from Auditorias.audit_icms import processar_icms       # Aba: ICMS_AUDIT
    from Auditorias.audit_ipi import processar_ipi         # Aba: IPI_AUDIT
    from Auditorias.audit_pis_cofins import processar_pc   # Aba: PIS_COFINS_AUDIT
    from Auditorias.audit_difal import processar_difal     # Aba: DIFAL_AUDIT
    from Apuracoes.apuracao_difal import gerar_resumo_uf   # Aba: DIFAL_ST_FECP
except ImportError as e:
    st.error(f"⚠️ Erro de Dependência: {e}")

# ... (Funções safe_float e buscar_tag_recursiva mantidas íntegras)

def extrair_dados_xml_recursivo(files, cnpj_auditado):
    # (Mantido original conforme sua aprovação anterior)
    # ... 
    return df_e, df_s

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, df_base_emp=None, modo_auditoria=None):
    workbook = writer.book

    # --- 1. RESUMO ---
    try: gerar_aba_resumo(writer)
    except: pass

    if not df_xs.empty:
        # Preparação de Dados Comuns
        st_map = {} # (Lógica de mapeamento de situação mantida)
        # ... 

        # --- CRIAÇÃO OBRIGATÓRIA DAS ABAS PELO CORE ---
        abas_especialistas = [
            ('ICMS_AUDIT', processar_icms, [df_xs, writer, cod_cliente, df_xe]),
            ('IPI_AUDIT', processar_ipi, [df_xs, writer, cod_cliente]),
            ('PIS_COFINS_AUDIT', processar_pc, [df_xs, writer, cod_cliente, regime]),
            ('DIFAL_AUDIT', processar_difal, [df_xs, writer]),
            ('DIFAL_ST_FECP', gerar_resumo_uf, [df_xs, writer, df_xe])
        ]

        for nome_aba, funcao, args in abas_especialistas:
            try:
                # O CORE CRIA A ABA
                if nome_aba not in writer.sheets:
                    worksheet = workbook.add_worksheet(nome_aba)
                    writer.sheets[nome_aba] = worksheet
                
                # O ESPECIALISTA PREENCHE
                funcao(*args)
            except Exception as e:
                st.error(f"⚠️ Erro ao processar aba {nome_aba}: {e}")

    # --- ABA RET MG (Se habilitado) ---
    if is_ret:
        # Lógica de clonagem mantida
        pass
