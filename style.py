import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

        /* RESET TOTAL DO VISUAL */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* FUNDO AREIA QUENTE (SAI O CINZA, ENTRA O LUXO) */
        .stApp {
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important;
        }

        .block-container { padding-top: 2rem !important; }
        
        /* FONTE DE GRIFE */
        html, body, [class*="st-"] { 
            font-family: 'Plus Jakarta Sans', sans-serif !important; 
        }

        /* --- TÍTULO EM CARAMELO QUEIMADO --- */
        .titulo-principal { 
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            margin-bottom: -10px;
            letter-spacing: -2px;
            background: linear-gradient(135deg, #8B5A2B 0%, #5D3A1A 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* BARRA PINK (MARCA REGISTRADA MARIANA) */
        .barra-marsala { 
            width: 100px; 
            height: 10px; 
            background: #FF69B4; 
            border-radius: 50px; 
            margin-bottom: 50px;
            box-shadow: 0 10px 20px rgba(255, 105, 180, 0.3);
        }

        /* EXTERMINANDO O QUADRADO DAS ABAS */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important;
            background-color: transparent !important;
            padding: 10px 0px !important;
        }

        /* ABAS PÍLULA - COR CARAMELO MOCA (MAIS VIVA) */
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: rgba(212, 163, 115, 0.2) !important; /* Caramelo Transparente */
            border-radius: 30px !important; 
            padding: 0px 35px !important;
            font-size: 16px !important; 
            font-weight: 600 !important;
            color: #5D3A1A !important;
            border: 1px solid rgba(255, 255, 255, 0.6) !important;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            background: white !important;
            color: #FF69B4 !important; /* Brilha Pink no Hover */
            box-shadow: 0 15px 30px rgba(255, 105, 180, 0.2) !important;
        }

        .stTabs [aria-selected="true"] {
            background: #5D3A1A !important; /* Caramelo Profundo */
            color: white !important;
            box-shadow: 0 15px 35px rgba(93, 58, 26, 0.3) !important;
        }

        /* --- BOTÃO ADMINISTRATIVO PINK DA MARIANA --- */
        div.stButton > button:has(div:contains("GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #FF1493) !important;
            color: #5D3A1A !important; 
            border: 2px solid #5D3A1A !important;
            box-shadow: 0 10px 25px rgba(255, 20, 147, 0.4) !important;
        }

        /* --- BOTÕES PADRÃO (CARAMELO MOCHA) --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important; /* CARAMELO QUENTE */
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 18px 30px !important;
            font-weight: 700 !important;
            border: 2px solid rgba(255, 105, 180, 0.2) !important; 
            box-shadow: 8px 8px 20px rgba(0,0,0,0.05), inset 0 2px 4px rgba(255,255,255,0.2) !important;
            transition: all 0.3s ease-in-out !important;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: scale(1.03) !important;
            box-shadow: 0 20px 40px rgba(255, 105, 180, 0.4) !important; 
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background: white;
            padding: 25px;
            border-radius: 35px;
            border-left: 12px solid #FF69B4;
            box-shadow: 15px 15px 40px rgba(0,0,0,0.03);
        }

        [data-testid="stMetricValue"] {
            color: #5D3A1A !important;
            font-weight: 800 !important;
        }
        </style>
    """, unsafe_allow_html=True)
