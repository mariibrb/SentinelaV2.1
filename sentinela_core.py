import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os

try:
    from audit_resumo import gerar_aba_resumo
    from Auditorias.audit_icms import processar_icms
    from Auditorias.audit_ipi import processar_ipi
    from Auditorias.audit_pis_cofins import processar_pc
    # IMPORTANTE: O Core agora apenas importa o seu motor de apuração
    from Apuracoes.apuracao_difal import gerar_resumo_uf
except ImportError as e:
    st.error(f"⚠️ Erro de Dependência: {e}")

# ... (Funções safe_float, buscar_tag_recursiva e processar_conteudo_xml mantidas íntegras)

def gerar_excel_final(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None):
    # 1. Cria a Aba Resumo (audit_resumo.py)
    try: gerar_aba_resumo(writer)
    except: pass
    
    if not df_xs.empty:
        # 2. Executa as auditorias padrão (Cada uma cria sua própria aba: AUDIT_ICMS, etc)
        processar_icms(df_xs, writer, cod_cliente, df_xe)
        processar_ipi(df_xs, writer, cod_cliente)
        processar_pc(df_xs, writer, cod_cliente, regime)
        
        # O COMANDO 'processar_difal(df_xs, writer)' FOI REMOVIDO DAQUI 
        # para não duplicar com o seu novo módulo abaixo.

        # 3. CHAMA O RESPONSÁVEL ÚNICO PELA ABA DE DIFAL
        # O seu módulo apuracao_difal.py assume o comando total da aba 'DIFAL_ST_FECP'
        try: 
            gerar_resumo_uf(df_xs, writer, df_xe)
        except Exception as e:
            st.error(f"Erro na aba de Saldo DIFAL: {e}")
