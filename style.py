import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* RESET TOTAL E SEGURANÇA DA PORTA DA SIDEBAR */
        header, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* --- BOTÃO DE PÂNICO: FORÇAR A SETINHA DA SIDEBAR A APARECER --- */
        [data-testid="stSidebarCollapsedControl"] {
            display: flex !important;
            visibility: visible !important;
            left: 15px !important;
            top: 15px !important;
            z-index: 1000001 !important;
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 50% !important;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.4) !important;
            width: 45px !important;
            height: 45px !important;
            border: 2px solid #FF69B4 !important;
        }

        [data-testid="stSidebarCollapsedControl"] button {
            color: #FF69B4 !important; /* Setinha em Pink Mariana */
            transform: scale(1.3);
        }

        /* FUNDO AREIA QUENTE BOUTIQUE */
        .stApp {
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important;
        }

        .block-container { padding-top: 2.5rem !important; }
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER MONTSERRAT --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.2rem; 
            font-weight: 800; 
            margin-bottom: 0px;
            letter-spacing: -1px;
            text-transform: uppercase;
        }
        .titulo-principal span { font-weight: 200 !important; color: #A67B5B; }

        .barra-marsala { 
            width: 60px; height: 3px; background: #FF69B4; 
            border-radius: 50px; margin-top: 10px; margin-bottom: 50px;
            box-shadow: 0 0 15px rgba(255, 105, 180, 0.8);
        }

        /* --- SIDEBAR BOUTIQUE --- */
        [data-testid="stSidebar"] {
            background-color: #F3E9DC !important;
            border-right: 1px solid rgba(166, 123, 91, 0.2) !important;
        }

        /* --- ABAS COM HIERARQUIA E BRILHO ROSA --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab"] {
            height: 48px !important;
            background: rgba(166, 123, 91, 0.15) !important;
            border-radius: 25px !important; 
            padding: 0px 30px !important;
            font-size: 15px !important; 
            font-weight: 400 !important;
            color: #5D3A1A !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            border: 1px solid rgba(255, 255, 255, 0.5) !important;
        }

        /* O BRILHO ROSA NO HOVER */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-3px) !important;
            background: white !important;
            color: #FF69B4 !important;
            filter: brightness(1.1) !important;
            box-shadow: 0 12px 25px rgba(255, 105, 180, 0.4) !important;
            border-top: 2px solid #FF69B4 !important;
        }

        .stTabs [aria-selected="true"] {
            background: #5D3A1A !important;
            color: white !important;
            font-weight: 600 !important;
            box-shadow: 0 8px 20px rgba(93, 58, 26, 0.2) !important;
        }

        /* Abas Filhas (Nível 2) - Conexão Visual Tracejada */
        [data-testid="stVerticalBlock"] [data-testid="stVerticalBlock"] .stTabs [data-baseweb="tab"] {
            height: 40px !important;
            font-size: 13px !important;
            border: 1px dashed #A67B5B !important;
            background: rgba(255, 255, 255, 0.5) !important;
        }

        /* --- BOTÃO ADM EXCLUSIVO (PINK & LETRAS MARROM) --- */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #FF1493) !important;
            color: #5D3A1A !important; 
            border-radius: 40px !important;
            border: 2px solid #5D3A1A !important;
            box-shadow: 0 10px 25px rgba(255, 20, 147, 0.5) !important;
            font-weight: 800 !important;
        }

        /* --- BOTÕES DO SISTEMA (CARAMELO MOCHA) --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-weight: 600 !important;
            box-shadow: 8px 8px 20px rgba(0,0,0,0.05), inset 0 2px 4px rgba(255,255,255,0.2) !important;
            transition: all 0.3s ease-in-out !important;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 15px 35px rgba(255, 105, 180, 0.35) !important;
            filter: brightness(1.1) !important;
        }
        </style>
    """, unsafe_allow_html=True)
