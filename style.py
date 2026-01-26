import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO E CLIMA REATIVO (O FUNDO INTEIRO) */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        
        .stApp { transition: background 0.8s ease-in-out !important; }

        /* MUDANÇA DE CLIMA NO FUNDO INTEIRO */
        div:has(#modulo-xml) .stApp { 
            background: radial-gradient(circle at top right, #D6F2FF 0%, #F8F9FA 100%) !important; 
        }
        div:has(#modulo-conformidade) .stApp { 
            background: radial-gradient(circle at top right, #FFDEEF 0%, #F8F9FA 100%) !important; 
        }
        div:has(#modulo-apuracao) .stApp { 
            background: radial-gradient(circle at top right, #DFFFEA 0%, #F8F9FA 100%) !important; 
        }

        /* 2. BOTÕES DE MÓDULO (ESTILO CARDS NEON) */
        div.stButton > button {
            background: #FFFFFF !important;
            color: #6C757D !important;
            border: 2px solid #DEE2E6 !important;
            border-radius: 15px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            height: 70px !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            text-transform: uppercase;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        }

        /* 🟦 XML - AZUL VIBRANTE E FUNDO */
        div:has(#modulo-xml) div.stButton > button[kind="primary"] {
            background: #00BFFF !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(0, 191, 255, 0.5) !important;
            transform: scale(1.08) translateY(-5px) !important;
        }

        /* 🟥 CONFORMIDADE - ROSA VIBRANTE E FUNDO */
        div:has(#modulo-conformidade) div.stButton > button[kind="primary"] {
            background: #FF69B4 !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(255, 105, 180, 0.5) !important;
            transform: scale(1.08) translateY(-5px) !important;
        }

        /* 🟩 APURAÇÃO - VERDE VIBRANTE E FUNDO */
        div:has(#modulo-apuracao) div.stButton > button[kind="primary"] {
            background: #2ECC71 !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(46, 204, 113, 0.5) !important;
            transform: scale(1.08) translateY(-5px) !important;
        }

        /* 3. ABAS INTERNAS (PASTINHAS) */
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px 30px 0 0 !important;
            font-weight: 700;
            padding: 12px 25px !important;
            background: rgba(255,255,255,0.5) !important;
        }

        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; }

        /* 4. ENVELOPES E PAINEL */
        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(10px);
            border-radius: 25px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        }

        [data-testid="stFileUploader"] {
            border-radius: 20px !important;
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            padding: 30px !important;
        }

        /* Cores nos envelopes conforme o módulo */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
