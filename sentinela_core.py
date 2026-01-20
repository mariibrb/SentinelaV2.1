import pandas as pd
import io, zipfile, streamlit as st, xml.etree.ElementTree as ET, re, os

try:
    from audit_resumo import gerar_aba_resumo
    from Auditorias.audit_icms import processar_icms
    from Auditorias.audit_ipi import processar_ipi
    from Auditorias.audit_pis_cofins import processar_pc
    # Importamos apenas o seu módulo das tabelas
    from Apuracoes.apuracao_difal import gerar_resumo_uf
except ImportError as e:
    st.error(f"⚠️ Erro Crítico: {e}")

# ... (safe_float, buscar_tag_recursiva e processar_conteudo_xml mantidos originais)

def gerar_analise_xml(df_xe, df_xs, cod_cliente, writer, regime, is_ret, ae=None, as_f=None, ge=None, gs=None):
    try: gerar_aba_resumo(writer)
    except: pass
    
    if not df_xs.empty:
        # Situação da nota
        st_map = {}
        for f_auth in ([ae] if ae else []) + ([as_f] if as_f else []):
            try:
                f_auth.seek(0)
                df_a = pd.read_excel(f_auth, header=None) if f_auth.name.endswith('.xlsx') else pd.read_csv(f_auth, header=None, sep=None, engine='python')
                df_a[0] = df_a[0].astype(str).str.replace('NFe', '').str.strip()
                st_map.update(df_a.set_index(0)[5].to_dict())
            except: continue
        
        df_xs['Situação Nota'] = df_xs['CHAVE_ACESSO'].map(st_map).fillna('⚠️ N/Encontrada')
        
        # Auditorias padrão
        processar_icms(df_xs, writer, cod_cliente, df_xe)
        processar_ipi(df_xs, writer, cod_cliente)
        processar_pc(df_xs, writer, cod_cliente, regime)
        
        # --- A ABA 'DIFAL_ST_FECP' É CRIADA AQUI ---
        try:
            gerar_resumo_uf(df_xs, writer, df_xe)
        except Exception as e:
            st.error(f"Erro ao gerar aba DIFAL: {e}")
