import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR ETERNA --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            display: block !important;
            visibility: visible !important;
            position: relative !important;
            background-color: #F3E9DC !important; 
            border-right: 2px solid #FF69B4 !important;
            z-index: 999999 !important;
        }

        [data-testid="sidebar-close-button"], 
        button[aria-label="Close sidebar"],
        .st-emotion-cache-6qob1r {
            display: none !important;
            visibility: hidden !important;
        }

        /* RESET DO LIXO VISUAL */
        header, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"] {
            display: none !important;
        }

        /* FUNDO MOCHA MOUSSE */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important; 
        }
        
        .block-container { padding-top: 2.5rem !important; }
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.2rem; 
            font-weight: 800; 
            margin-bottom: 0px;
            letter-spacing: -1px;
            text-transform: uppercase;
            line-height: 1;
        }
        .titulo-principal span { font-weight: 200 !important; color: #A67B5B; }

        .barra-marsala { 
            width: 60px; height: 3px; background: #FF69B4; 
            border-radius: 50px; margin-top: 10px; margin-bottom: 50px;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.9); /* BRILHO NA BARRA */
        }

        /* --- ESTILIZAÇÃO DAS ABAS COM BRILHO --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: white !important;
            border-radius: 15px 15px 0 0 !important;
            margin-right: 12px !important;
            padding: 0px 40px !important;
            border: 1px solid #E0E0E0 !important;
            font-weight: 600 !important;
            transition: all 0.3s ease-in-out !important;
        }

        /* --- IDENTIDADE VISUAL + GLOW (BRILHO) --- */

        /* ABA 1: GARIMPEIRO (Rosa com Brilho Neon) */
        .stTabs [data-baseweb="tab"]:nth-child(1) {
            border-bottom: 4px solid #FF69B4 !important;
            color: #FF69B4 !important;
        }
        .stTabs [data-baseweb="tab"]:nth-child(1)[aria-selected="true"] {
            background: #FF69B4 !important;
            color: white !important;
            box-shadow: 0 0 25px rgba(255, 105, 180, 0.6) !important; /* BRILHO ROSA */
        }

        /* ABA 2: CONFORMIDADE (Verde com Brilho Neon) */
        .stTabs [data-baseweb="tab"]:nth-child(2) {
            border-bottom: 4px solid #00D1FF !important; /* Mudei para um azul ciano brilhante para contrastar melhor */
            color: #00D1FF !important;
        }
        .stTabs [data-baseweb="tab"]:nth-child(2)[aria-selected="true"] {
            background: #00D1FF !important;
            color: white !important;
            box-shadow: 0 0 25px rgba(0, 209, 255, 0.6) !important; /* BRILHO CIANO */
        }

        /* --- BOTÃO ADM (BRILHO PULSANTE) --- */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #FF1493) !important;
            color: white !important; 
            border-radius: 40px !important;
            border: none !important;
            font-weight: 800 !important;
            box-shadow: 0 0 20px rgba(255, 20, 147, 0.5) !important;
        }

        /* --- BOTÕES DO SISTEMA (BRILHO CARAMELO) --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-weight: 600 !important;
            box-shadow: 0 5px 15px rgba(139, 90, 43, 0.3) !important;
            transition: all 0.3s ease-in-out !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 0 25px rgba(255, 105, 180, 0.4) !important; /* BRILHO NO HOVER */
        }

        /* CONTAINER DE STATUS COM BORDA ILUMINADA */
        .status-container {
            background: white;
            padding: 20px;
            border-radius: 30px;
            border-left: 6px solid #FF69B4;
            box-shadow: 0 10px 40px rgba(255, 105, 180, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)
