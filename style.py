import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO E CLIMA REATIVO (FUNDO DO APP) */
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.8s ease-in-out !important; }

        div:has(#modulo-xml) .stApp { background: radial-gradient(circle at top right, #D6F2FF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-amarelo) .stApp { background: radial-gradient(circle at top right, #FFF9C4 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-conformidade) .stApp { background: radial-gradient(circle at top right, #FFDEEF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-apuracao) .stApp { background: radial-gradient(circle at top right, #DFFFEA 0%, #F8F9FA 100%) !important; }

        /* 2. TÍTULO E VERSÃO */
        .titulo-principal {
            margin-top: 0px !important;
            padding-top: 0px !important;
            padding-bottom: 50px !important;
            display: block;
            width: 100%;
        }

        /* 3. BOTÕES DE MÓDULO (MENU SUPERIOR) */
        div.stButton > button {
            color: white !important;
            border: none !important;
            border-radius: 15px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            height: 75px !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            text-transform: uppercase;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
            opacity: 0.6 !important;
        }

        div.stButton > button:hover {
            opacity: 1 !important;
            transform: translateY(-5px) !important;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.9) !important;
        }

        /* ESTADOS ATIVOS (BRILHO NEON) */
        div.stHorizontalBlock > div:nth-child(1) button { background: #00BFFF !important; }
        div:has(#modulo-xml) div.stHorizontalBlock > div:nth-child(1) button {
            opacity: 1 !important; transform: scale(1.1) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.8), 0 0 40px rgba(0, 191, 255, 0.5) !important;
            border: 3px solid #FFFFFF !important;
        }

        div.stHorizontalBlock > div:nth-child(2) button { background: #FFD700 !important; color: #424242 !important; }
        div:has(#modulo-amarelo) div.stHorizontalBlock > div:nth-child(2) button {
            opacity: 1 !important; transform: scale(1.1) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 1) !important;
            border: 3px solid #FFFFFF !important;
        }

        div.stHorizontalBlock > div:nth-child(3) button { background: #FF69B4 !important; }
        div:has(#modulo-conformidade) div.stHorizontalBlock > div:nth-child(3) button {
            opacity: 1 !important; transform: scale(1.1) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.8), 0 0 40px rgba(255, 105, 180, 0.5) !important;
            border: 3px solid #FFFFFF !important;
        }

        div.stHorizontalBlock > div:nth-child(4) button { background: #2ECC71 !important; }
        div:has(#modulo-apuracao) div.stHorizontalBlock > div:nth-child(4) button {
            opacity: 1 !important; transform: scale(1.1) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.8), 0 0 40px rgba(46, 204, 113, 0.5) !important;
            border: 3px solid #FFFFFF !important;
        }

        /* 4. ÁREA DE UPLOAD TOTALMENTE CINZA NEUTRO */
        /* Borda do container */
        [data-testid="stFileUploader"] {
            border-radius: 20px !important;
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            padding: 30px !important;
        }

        /* Botão "Browse files" interno */
        [data-testid="stFileUploader"] section button {
            background-color: #6C757D !important;
            color: white !important;
            border: none !important;
        }

        /* Texto de limite e arraste */
        [data-testid="stFileUploader"] section div {
            color: #6C757D !important;
        }

        /* 5. ABAS INTERNAS E PAINÉIS */
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px 30px 0 0 !important;
            font-weight: 700;
            padding: 12px 25px !important;
            background: rgba(255,255,255,0.5) !important;
        }

        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-amarelo) .stTabs [aria-selected="true"] { background: #FFD700 !important; color: #424242 !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; }

        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(10px);
            border-radius: 25px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
        }
        </style>
    """, unsafe_allow_html=True)
