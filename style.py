import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO E CLIMA REATIVO (VOLTANDO AS CORES) */
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.8s ease-in-out !important; }

        div:has(#modulo-xml) .stApp { background: radial-gradient(circle at top right, #D6F2FF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-amarelo) .stApp { background: radial-gradient(circle at top right, #FFF9C4 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-conformidade) .stApp { background: radial-gradient(circle at top right, #FFDEEF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-apuracao) .stApp { background: radial-gradient(circle at top right, #DFFFEA 0%, #F8F9FA 100%) !important; }

        /* 2. BOTÕES DE MÓDULO (MENU SUPERIOR) - BRILHOS RESTAURADOS */
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
            opacity: 0.7;
        }

        /* ESTADOS SELECIONADOS (VOLTANDO O NEON) */
        div.stHorizontalBlock > div:nth-child(1) button { background: #00BFFF !important; }
        div:has(#modulo-xml) div.stHorizontalBlock > div:nth-child(1) button {
            opacity: 1 !important; transform: scale(1.1) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.7), 0 0 40px rgba(0, 191, 255, 0.5) !important;
            border: 3px solid #FFFFFF !important;
        }
        div.stHorizontalBlock > div:nth-child(3) button { background: #FF69B4 !important; }
        div:has(#modulo-conformidade) div.stHorizontalBlock > div:nth-child(3) button {
            opacity: 1 !important; transform: scale(1.1) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.7), 0 0 40px rgba(255, 105, 180, 0.5) !important;
            border: 3px solid #FFFFFF !important;
        }

        /* 3. ABAS INTERNAS (PASTINHAS COLORIDAS) */
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px 30px 0 0 !important;
            font-weight: 700; padding: 12px 25px !important;
            background: rgba(255,255,255,0.5) !important;
        }
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* 4. FILE UPLOADER (ENVELOPES COLORIDOS MANTIDOS) */
        [data-testid="stFileUploader"] {
            border-radius: 20px !important;
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            padding: 30px !important;
        }
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; }

        /* 5. A ÚNICA COISA QUE MUDA: O BOTÃO INTERNO PARA CINZA */
        /* Força o botão de upload a ser cinza em todos os módulos, sem mexer no resto */
        [data-testid="stFileUploader"] section button {
            background-color: #6C757D !important;
            color: white !important;
            border: none !important;
            box-shadow: none !important;
        }
        [data-testid="stFileUploader"] section button:hover { background-color: #495057 !important; }
        [data-testid="stFileUploader"] svg { fill: #6C757D !important; }

        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(10px);
            border-radius: 25px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
        }
        </style>
    """, unsafe_allow_html=True)
