import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* LIMPEZA TOTAL DO TOPO */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
            height: 0px !important;
            padding: 0px !important;
            margin: 0px !important;
        }
        
        /* FUNDO NEUTRO PROFISSIONAL */
        .stApp {
            background-color: #FDFBFA !important; 
        }

        /* AJUSTE DO CONTEÚDO */
        .block-container { padding-top: 2rem !important; }
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* TÍTULOS */
        .titulo-principal { color: #2D1B1B; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { 
            width: 80px; 
            height: 6px; 
            background: linear-gradient(90deg, #FF1493, #4B2E2E); 
            border-radius: 10px; 
            margin-bottom: 30px; 
        }

        /* ABAS METALIZADAS COM BRILHO NO HOVER (RESTAURADO) */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #EAD7D7 !important;
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            color: #2D1B1B !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            border: 1px solid transparent !important;
        }

        /* O BRILHO AO PASSAR O MOUSE (HOVER) */
        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.2) !important;
            transform: translateY(-3px) !important;
            color: #FF1493 !important; /* Texto brilha em pink no hover */
            background: #F5E6E6 !important;
            box-shadow: 0 10px 20px rgba(255, 20, 147, 0.15) !important;
            border-top: 2px solid #FF1493 !important;
        }

        /* ABA ATIVA COM GLOW MÁXIMO */
        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #4B2E2E 0%, #2D1B1B 100%) !important;
            color: #FF1493 !important;
            font-weight: 800 !important;
            box-shadow: 0 -5px 20px rgba(255, 20, 147, 0.4) !important;
            border-top: 3px solid #FF1493 !important;
            filter: contrast(1.1) !important;
        }

        /* BOTÕES LUXO COM BRILHO E BORDA PINK */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #5D4037 0%, #2D1B1B 50%, #1A0F0F 100%) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 2px solid #FF1493 !important;
            box-shadow: inset 0 2px 3px rgba(255, 255, 255, 0.2), 0 4px 10px rgba(255, 20, 147, 0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 20, 147, 0.6) !important; 
            filter: brightness(1.3) !important;
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #FF1493;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        /* MÉTRICAS EM PINK */
        [data-testid="stMetricValue"] {
            color: #FF1493 !important;
            text-shadow: 0px 0px 5px rgba(255, 20, 147, 0.2);
        }
        </style>
    """, unsafe_allow_html=True)
