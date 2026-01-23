import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        /* 1. ESTILO DO MENU DE SELEÇÃO (A REGUA NO TOPO) */
        [role="radiogroup"] {
            padding: 10px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
        }

        /* 2. DISTINÇÃO POR MÓDULO (A MÁGICA DO CLIMA) */

        /* --- CLIMA AZUL (ANÁLISE XML) --- */
        div:has(#modulo-xml) {
            --cor-primaria: #00D1FF;
            --brilho: rgba(0, 209, 255, 0.4);
        }
        div:has(#modulo-xml) [data-checked="true"] {
            background: var(--cor-primaria) !important;
            box-shadow: 0 0 20px var(--brilho) !important;
            color: white !important;
        }

        /* --- CLIMA ROSA (CONFORMIDADE) --- */
        div:has(#modulo-conformidade) {
            --cor-primaria: #FF00E5;
            --brilho: rgba(255, 0, 229, 0.4);
        }
        div:has(#modulo-conformidade) [data-checked="true"] {
            background: var(--cor-primaria) !important;
            box-shadow: 0 0 20px var(--brilho) !important;
            color: white !important;
        }

        /* --- CLIMA VERDE (APURAÇÃO) --- */
        div:has(#modulo-apuracao) {
            --cor-primaria: #00FF94;
            --brilho: rgba(0, 255, 148, 0.4);
        }
        div:has(#modulo-apuracao) [data-checked="true"] {
            background: var(--cor-primaria) !important;
            box-shadow: 0 0 20px var(--brilho) !important;
            color: black !important;
            font-weight: bold;
        }

        /* 3. REAÇÃO DO CONTEÚDO (PAINEL E BORDAS) */
        /* Faz a "Vareta" da pasta e os botões de upload reagirem à cor do módulo */
        div:has(#modulo-xml) [data-testid="stTabPanel"], 
        div:has(#modulo-conformidade) [data-testid="stTabPanel"], 
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] {
            border-top: 10px solid var(--cor-primaria) !important;
            transition: border-top 0.5s ease;
        }

        div:has(#modulo-xml) [data-testid="stFileUploader"],
        div:has(#modulo-conformidade) [data-testid="stFileUploader"],
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] {
            border-color: var(--cor-primaria) !important;
            background: rgba(255, 255, 255, 0.02) !important;
        }

        /* 4. ESTILO DAS ABAS (DEIXAR COM CARA DE PASTA MESMO) */
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px 30px 0 0 !important;
            margin-right: 5px;
            padding: 10px 25px !important;
            transition: all 0.3s;
        }

        .stTabs [aria-selected="true"] {
            background: var(--cor-primaria) !important;
            color: white !important;
            transform: translateY(-5px);
        }
        
        /* Ajuste específico para o texto do verde ser legível */
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] {
            color: black !important;
        }

        </style>
    """, unsafe_allow_html=True)
