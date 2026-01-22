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
        
        /* FUNDO ROSADINHO DELICADO */
        .stApp {
            background-color: #FFF0F5 !important; /* Lavender Blush - um rosa bem clarinho e elegante */
        }

        /* AJUSTE DO CONTEÚDO */
        .block-container { padding-top: 2rem !important; }
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* TÍTULOS */
        .titulo-principal { color: #4B2E2E; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { width: 80px; height: 6px; background: linear-gradient(90deg, #FF69B4, #4B2E2E); border-radius: 10px; margin-bottom: 30px; }

        /* ABAS METALIZADAS - MARROM COM TEXTO ROSA */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #EAD7D7 !important;
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            color: #4B2E2E !important;
            transition: all 0.3s ease !important;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #6B4423 0%, #4B2E2E 50%, #2D1B1B 100%) !important;
            color: #FFB6C1 !important; /* Rosa claro no texto da aba ativa */
            font-weight: 800 !important;
            box-shadow: 0 -5px 15px rgba(75, 46, 46, 0.3) !important;
        }

        /* BOTÕES MARROM CHOCOLATE COM BORDA PINK E BRILHO (RESTAURADO) */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #8B5A2B 0%, #4B2E2E 50%, #351C1C 100%) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 2px solid #FF1493 !important; /* BORDA DEEP PINK */
            box-shadow: inset 0 2px 3px rgba(255,255,255,0.3), 0 4px 10px rgba(0,0,0,0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 20, 147, 0.4) !important; /* Glow Pink no Hover */
            filter: brightness(1.2) !important;
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #FF69B4; /* Detalhe Pink */
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
