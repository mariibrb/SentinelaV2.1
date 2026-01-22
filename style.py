import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR ETERNA --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 3px solid #FF69B4 !important; 
            z-index: 999999 !important;
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important; 
        }
        
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.2rem; 
            font-weight: 800; 
            text-transform: uppercase;
        }

        /* --- ABAS MÃE (PASTAS GRANDES) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab"] {
            height: 75px !important;
            background: linear-gradient(180deg, #E8DCCB 0%, #D4A373 100%) !important;
            border-radius: 25px 60px 0 0 !important;
            margin-right: -15px !important; 
            padding: 0px 45px !important;
            border: 1px solid #A67B5B !important;
            font-size: 18px !important;
            font-weight: 800 !important;
            color: #5D3A1A !important;
            transition: all 0.4s ease !important;
        }

        /* CORES ABAS MÃE ATIVAS */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #B0E0E6 0%, #4682B4 100%) !important;
            color: white !important;
            transform: translateY(-10px) !important;
            box-shadow: 0 0 30px rgba(0, 209, 255, 0.6) !important;
        }

        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-10px) !important;
            box-shadow: 0 0 30px rgba(255, 105, 180, 0.6) !important;
        }

        /* --- SUB-ABAS (DIVISÓRIAS INTERNAS) --- */
        /* Criando o efeito de estar 'dentro' da pasta */
        .stTabs .stTabs {
            padding-left: 30px !important; /* RECUO PARA PARECER SUB-PASTA */
            border-left: 4px dashed #FFB6C1 !important; /* LINHA QUE CONECTA À MÃE */
            margin-top: 15px !important;
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #FFFFFF !important;
            border-radius: 15px 35px 0 0 !important;
            font-size: 14px !important;
            color: #DB7093 !important;
            border: 1px solid #FFD1DC !important;
            margin-right: 5px !important;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05) !important;
        }

        /* SUB-ABA ATIVA (BRILHO INTERNO) */
        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFD1DC 100%) !important;
            color: #C71585 !important;
            transform: scale(1.05) !important;
            box-shadow: 0 5px 15px rgba(255, 182, 193, 0.8) !important;
            border-bottom: 4px solid #FF69B4 !important;
        }

        /* BOTÕES E STATUS */
        .stButton > button {
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
        }

        .status-container {
            background: white;
            padding: 20px;
            border-radius: 30px;
            border-left: 8px solid #FF69B4;
            box-shadow: 0 10px 40px rgba(0,0,0,0.03);
        }
        </style>
    """, unsafe_allow_html=True)
