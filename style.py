import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

        /* RESET TOTAL DO VISUAL "ANOS 2000" */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* FUNDO DE ESTÚDIO REFINADO */
        .stApp {
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important;
        }

        .block-container { padding-top: 2rem !important; }
        
        /* FONTE DE GRIFE */
        html, body, [class*="st-"] { 
            font-family: 'Plus Jakarta Sans', sans-serif !important; 
        }

        /* --- O NOVO TÍTULO "SENTINELA" (ZERO WORDPAD) --- */
        .titulo-principal { 
            color: #3D2B1F; 
            font-size: 4.2rem; /* Aumentado para impacto */
            font-weight: 800; 
            margin-bottom: -5px;
            letter-spacing: -3px; /* Letras mais juntas como em marcas de luxo */
            line-height: 1;
            background: linear-gradient(180deg, #5D3A1A 0%, #3D2B1F 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            /* Efeito de profundidade real */
            filter: drop-shadow(0px 7px 15px rgba(61, 43, 31, 0.2));
        }

        /* BARRA PÍLULA DESIGNER */
        .barra-marsala { 
            width: 120px; 
            height: 12px; 
            background: linear-gradient(90deg, #FF69B4, #D4A373); 
            border-radius: 50px; 
            margin-bottom: 50px;
            box-shadow: 0 10px 20px rgba(255, 105, 180, 0.3), inset 0 2px 4px rgba(255, 255, 255, 0.4);
        }

        /* EXTERMINANDO O QUADRADO DAS ABAS */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important;
            background-color: transparent !important;
            padding: 10px 0px !important;
        }

        /* ABAS PÍLULA FLUTUANTES */
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: rgba(212, 163, 115, 0.15) !important;
            border-radius: 35px !important; 
            padding: 0px 35px !important;
            font-size: 16px !important; 
            font-weight: 600 !important;
            color: #5D3A1A !important;
            border: 1px solid rgba(255, 255, 255, 0.5) !important;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            background: white !important;
            color: #FF69B4 !important;
            box-shadow: 0 15px 30px rgba(255, 105, 180, 0.2) !important;
        }

        .stTabs [aria-selected="true"] {
            background: #3D2B1F !important;
            color: white !important;
            box-shadow: 0 15px 35px rgba(61, 43, 31, 0.4) !important;
        }

        /* --- BOTÃO ADMINISTRATIVO EXCLUSIVO MARIANA --- */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #FF1493) !important;
            color: #3D2B1F !important; 
            border: 2px solid #3D2B1F !important;
            box-shadow: 0 12px 28px rgba(255, 20, 147, 0.45) !important;
            font-weight: 800 !important;
            text-transform: uppercase;
        }

        /* --- BOTÕES PADRÃO (CARAMELO MOCHA) --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            padding: 18px 30px !important;
            font-weight: 700 !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important; 
            box-shadow: 8px 8px 20px rgba(0,0,0,0.06), inset 0 2px 4px rgba(255,255,255,0.2) !important;
            transition: all 0.4s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 15px 35px rgba(255, 105, 180, 0.3) !important; 
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background: white;
            padding: 30px;
            border-radius: 40px;
            border-left: 15px solid #FF69B4;
            box-shadow: 20px 20px 50px rgba(0,0,0,0.04);
        }

        [data-testid="stMetricValue"] {
            color: #3D2B1F !important;
            font-weight: 800 !important;
            letter-spacing: -1px;
        }
        </style>
    """, unsafe_allow_html=True)
