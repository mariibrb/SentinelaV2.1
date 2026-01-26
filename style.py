import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO CHIQUE */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #DEE2E6 100%) !important; }

        /* 2. OS NOVOS BOTÕES DE MÓDULO (OS CARDS) */
        /* Estilo para os botões que NÃO estão selecionados (Inativos) */
        div.stButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #CED4DA 100%) !important;
            color: #6C757D !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 12px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            height: 60px !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        }

        /* Hover genérico para dar um brilho antes de clicar */
        div.stButton > button:hover {
            transform: translateY(-5px) !important;
            border-color: #6C757D !important;
            color: #212529 !important;
        }

        /* 3. A MÁGICA: PINTANDO O BOTÃO ATIVO (PRIMARY) */
        
        /* 🟦 XML - AZUL VIBRANTE */
        div:has(#modulo-xml) div.stButton > button[kind="primary"] {
            background: #00BFFF !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 10px 25px rgba(0, 191, 255, 0.6) !important;
            transform: scale(1.05) !important;
        }

        /* 🟥 CONFORMIDADE - ROSA VIBRANTE */
        div:has(#modulo-conformidade) div.stButton > button[kind="primary"] {
            background: #FF69B4 !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 10px 25px rgba(255, 105, 180, 0.6) !important;
            transform: scale(1.05) !important;
        }

        /* 🟩 APURAÇÃO - VERDE VIBRANTE */
        div:has(#modulo-apuracao) div.stButton > button[kind="primary"] {
            background: #2ECC71 !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 10px 25px rgba(46, 204, 113, 0.6) !important;
            transform: scale(1.05) !important;
        }

        /* 4. ÁREA DE TRABALHO E PASTINHAS INTERNAS */
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 25px 0 0 !important;
            font-weight: 700;
            padding: 10px 20px !important;
        }

        /* Pastinhas internas acendendo conforme o módulo */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; }

        /* 5. ENVELOPES REATIVOS */
        [data-testid="stFileUploader"] {
            border-radius: 15px !important;
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
        }
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; background: #F0F9FF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; background: #FFF5F9 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #2ECC71 !important; background: #F5FFF9 !important; }

        </style>
    """, unsafe_allow_html=True)
