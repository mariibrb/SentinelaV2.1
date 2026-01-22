import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 3px solid #FFB6C1 !important; 
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

        /* --- ESTILIZAÇÃO DIVISÓRIAS METALIZADAS --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        /* Abas Inativas (Metal Fosco) */
        .stTabs [data-baseweb="tab"] {
            height: 65px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #E0E0E0 100%) !important;
            border-radius: 20px 45px 0 0 !important;
            margin-right: -15px !important;
            padding: 0px 45px !important;
            border: 1px solid #D1D1D1 !important;
            font-weight: 600 !important;
            color: #A0A0A0 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 5px 0 10px rgba(0,0,0,0.05) !important;
        }

        /* --- O BRILHO NEON (GLOW) E METALIZADO --- */

        /* 🔵 ANÁLISE XML: AZUL BEBÊ COM NEON INTENSO */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #E0FFFF 0%, #87CEEB 100%) !important; /* Efeito Metal */
            color: #0056b3 !important;
            transform: translateY(-15px) !important; /* Pulo maior */
            border: 2px solid #00D1FF !important;
            /* EFEITO GLOW MULTICAMADAS: */
            box-shadow: 0 0 15px #00D1FF, 0 0 30px #00D1FF, 0 0 45px rgba(0, 209, 255, 0.3) !important; 
            z-index: 100 !important;
            text-shadow: 0 0 5px rgba(255,255,255,0.8) !important;
        }

        /* 💗 FAMÍLIA FISCAL: ROSA BEBÊ COM NEON INTENSO (ICMS, PIS, RET, DIFAL) */
        .stTabs [data-baseweb="tab"]:has(div:contains("ICMS"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("PIS"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("RET"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("DIFAL"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFB6C1 100%) !important; /* Efeito Metal Rosé */
            color: #C71585 !important;
            transform: translateY(-15px) !important; /* Pulo maior */
            border: 2px solid #FF69B4 !important;
            /* EFEITO GLOW MULTICAMADAS: */
            box-shadow: 0 0 15px #FF69B4, 0 0 30px #FF69B4, 0 0 45px rgba(255, 105, 180, 0.3) !important;
            z-index: 100 !important;
            text-shadow: 0 0 5px rgba(255,255,255,0.8) !important;
        }

        /* BRILHO NO HOVER (QUANDO PASSA O MOUSE) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-8px) !important;
            filter: brightness(1.2) !important;
            cursor: pointer !important;
        }

        /* SUB-ABAS (TAMBÉM COM BRILHO ROSA) */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 48px !important;
            padding: 0px 25px !important;
            border-radius: 12px 30px 0 0 !important;
            margin-right: -10px !important;
        }
        
        .stTabs .stTabs [aria-selected="true"] {
            background: #FFD1DC !important;
            box-shadow: 0 0 20px #FFB6C1 !important; /* Glow nas sub-abas */
        }

        /* BOTÃO ADM COM BRILHO PULSANTE */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FFB6C1, #FF1493) !important;
            color: white !important; 
            border: none !important;
            box-shadow: 0 0 20px rgba(255, 20, 147, 0.6) !important;
            font-weight: 800 !important;
        }
        </style>
    """, unsafe_allow_html=True)
