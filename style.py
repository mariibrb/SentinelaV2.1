import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDO GERAL DA PÁGINA (CONFORME SETOR) */
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.5s ease; }
        
        div:has(#modulo-xml) .stApp { background-color: #F0F9FF !important; }
        div:has(#modulo-amarelo) .stApp { background-color: #FFFFF0 !important; }
        div:has(#modulo-conformidade) .stApp { background-color: #FFF5FA !important; }
        div:has(#modulo-apuracao) .stApp { background-color: #F7FFF9 !important; }

        /* 2. MENU SUPERIOR (BOTÕES GRANDES) */
        div.stButton > button {
            background: #FFFFFF !important;
            border: 2px solid #DEE2E6 !important;
            border-radius: 10px !important;
            color: #6C757D !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700 !important;
            height: 60px !important;
            transition: all 0.3s ease;
        }

        /* IDENTIDADE NO CLIQUE */
        div:has(#modulo-xml) div.stHorizontalBlock > div:nth-child(1) button { border: 3px solid #00BFFF !important; color: #00BFFF !important; box-shadow: 0 4px 10px rgba(0,191,255,0.2); }
        div:has(#modulo-amarelo) div.stHorizontalBlock > div:nth-child(2) button { border: 3px solid #FFD700 !important; color: #B8860B !important; box-shadow: 0 4px 10px rgba(255,215,0,0.2); }
        div:has(#modulo-conformidade) div.stHorizontalBlock > div:nth-child(3) button { border: 3px solid #FF69B4 !important; color: #FF69B4 !important; box-shadow: 0 4px 10px rgba(255,105,180,0.2); }
        div:has(#modulo-apuracao) div.stHorizontalBlock > div:nth-child(4) button { border: 3px solid #2ECC71 !important; color: #2ECC71 !important; box-shadow: 0 4px 10px rgba(46,204,113,0.2); }

        /* 3. CENTRAL DE IMPORTAÇÃO (OS QUADRADOS DA FOTO) */
        [data-testid="stFileUploader"] {
            border: 3px solid #DEE2E6 !important; /* Borda sólida como na foto */
            background: #FFFFFF !important;
            border-radius: 5px !important;
            padding: 20px !important;
        }

        /* COR DA BORDA DO UPLOAD POR SETOR */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #2ECC71 !important; }

        /* --- BOTÃO BROWSE FILES (UNICA PARTE CINZA) --- */
        [data-testid="stFileUploader"] section button {
            background-color: #F8F9FA !important;
            color: #6C757D !important;
            border: 1px solid #DEE2E6 !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
        }
        [data-testid="stFileUploader"] section button:hover { background-color: #E9ECEF !important; }

        /* 4. ABAS (TABS) INTERNAS */
        .stTabs [data-baseweb="tab"] {
            font-weight: 700;
            padding: 10px 20px !important;
        }
        
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { color: #00BFFF !important; border-bottom: 3px solid #00BFFF !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { color: #FF69B4 !important; border-bottom: 3px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { color: #2ECC71 !important; border-bottom: 3px solid #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
