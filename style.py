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

        /* TÍTULOS EM MARROM (TEXTO SEMPRE ESCURO) */
        .titulo-principal { color: #2D1B1B; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { 
            width: 80px; 
            height: 6px; 
            background: linear-gradient(90deg, #E75480, #4B2E2E); /* Pink mais suave (Dark Pink) */
            border-radius: 10px; 
            margin-bottom: 30px; 
        }

        /* ABAS METALIZADAS - TEXTO SEMPRE MARROM */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #EAD7D7 !important;
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            color: #2D1B1B !important; /* Texto Marrom */
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            border: 1px solid transparent !important;
        }

        /* EFEITO LUZ NO HOVER (BRILHO ROSA SUAVE) */
        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.1) !important;
            transform: translateY(-3px) !important;
            color: #2D1B1B !important; /* Texto continua Marrom */
            background: #F5E6E6 !important;
            box-shadow: 0 10px 20px rgba(231, 84, 128, 0.2) !important; /* Brilho Rosa Suave */
            border-top: 2px solid #E75480 !important; /* Luz Pink no topo */
        }

        /* ABA ATIVA COM FOCO EM MARROM E LUZ PINK */
        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #4B2E2E 0%, #2D1B1B 100%) !important;
            color: #FFFFFF !important; /* Texto Branco para contraste no Marrom */
            font-weight: 800 !important;
            box-shadow: 0 -5px 20px rgba(231, 84, 128, 0.3) !important; /* Aura de luz Pink */
            border-top: 3px solid #E75480 !important;
            filter: contrast(1.1) !important;
        }

        /* BOTÕES LUXO - MARROM COM BRILHO PINK NA BORDA E HOVER */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #5D4037 0%, #2D1B1B 50%, #1A0F0F 100%) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 2px solid #E75480 !important; /* Borda Pink Suave */
            box-shadow: inset 0 2px 3px rgba(255, 255, 255, 0.2), 0 4px 10px rgba(0, 0, 0, 0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(231, 84, 128, 0.4) !important; /* Efeito Luz Rosa no Hover */
            filter: brightness(1.2) !important;
            color: #FFFFFF !important; /* Texto continua Branco */
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #E75480; /* Detalhe Luz Pink */
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        /* MÉTRICAS (TEXTO MARROM COM FUNDO DE LUZ) */
        [data-testid="stMetricValue"] {
            color: #2D1B1B !important;
            text-shadow: 0px 0px 8px rgba(231, 84, 128, 0.2); /* Glow Pink ao redor do número */
        }
        </style>
    """, unsafe_allow_html=True)
