import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO E SIDEBAR */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.8s ease-in-out !important; }

        /* FUNDOS REATIVOS */
        div:has(#modulo-xml) .stApp { background: radial-gradient(circle at top right, #D6F2FF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-amarelo) .stApp { background: radial-gradient(circle at top right, #FFF9C4 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-conformidade) .stApp { background: radial-gradient(circle at top right, #FFDEEF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-apuracao) .stApp { background: radial-gradient(circle at top right, #DFFFEA 0%, #F8F9FA 100%) !important; }

        /* 2. MENU MASTER - CORES FIXAS NOS BOTÕES (IMPEDE O VERMELHO) */
        div.stButton > button {
            color: white !important;
            border: none !important;
            border-radius: 15px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            height: 70px !important;
            text-transform: uppercase;
            opacity: 0.65 !important;
            transition: all 0.4s ease !important;
        }

        /* Forçando a cor de cada zona individualmente */
        /* 1º Botão: AZUL (GARIMPEIRO) */
        div.stHorizontalBlock > div:nth-child(1) button { background-color: #00BFFF !important; }
        /* 2º Botão: AMARELO (CONCILIADOR) */
        div.stHorizontalBlock > div:nth-child(2) button { background-color: #FFD700 !important; color: #424242 !important; }
        /* 3º Botão: ROSA (AUDITOR) */
        div.stHorizontalBlock > div:nth-child(3) button { background-color: #FF69B4 !important; }
        /* 4º Botão: VERDE (ESPELHO) */
        div.stHorizontalBlock > div:nth-child(4) button { background-color: #2ECC71 !important; }

        /* BRILHO BRANCO NO MÓDULO ATIVO */
        div:has(#modulo-xml) div.stHorizontalBlock > div:nth-child(1) button,
        div:has(#modulo-amarelo) div.stHorizontalBlock > div:nth-child(2) button,
        div:has(#modulo-conformidade) div.stHorizontalBlock > div:nth-child(3) button,
        div:has(#modulo-apuracao) div.stHorizontalBlock > div:nth-child(4) button {
            opacity: 1 !important;
            transform: scale(1.08) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.9) !important;
            border: 3px solid #FFFFFF !important;
        }

        /* 3. AS ABAS (PASTINHAS) - CORES RESTAURADAS */
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px 30px 0 0 !important;
            font-weight: 700;
            padding: 12px 25px !important;
            background: rgba(255,255,255,0.5) !important;
            color: #6C757D !important;
        }

        /* COR DA PASTINHA ATIVA */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background-color: #00BFFF !important; color: white !important; }
        div:has(#modulo-amarelo) .stTabs [aria-selected="true"] { background-color: #FFD700 !important; color: #424242 !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background-color: #FF69B4 !important; color: white !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background-color: #2ECC71 !important; color: white !important; }

        /* 4. ÁREA DE UPLOAD - TOTALMENTE CINZA NEUTRO */
        [data-testid="stFileUploader"] {
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            border-radius: 20px !important;
            padding: 30px !important;
        }

        [data-testid="stFileUploader"] section button {
            background-color: #6C757D !important; 
            color: white !important;
            border: none !important;
        }

        [data-testid="stFileUploader"] svg { fill: #6C757D !important; }

        /* 5. PAINEL DAS ABAS (ENVELOPE) */
        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.9) !important;
            backdrop-filter: blur(10px);
            border-radius: 0 20px 20px 20px !important;
            padding: 35px !important;
            border: 1px solid #DEE2E6;
        }
        </style>
    """, unsafe_allow_html=True)
