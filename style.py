import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* BLINDAGEM CONTRA ÍCONES FANTASMAS */
        span[data-testid="stHeaderActionElements"], .st-emotion-cache-10oheav, #keyboard_double {
            display: none !important;
            visibility: hidden !important;
        }

        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        .titulo-principal { color: #1E1E1E; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-laranja { width: 80px; height: 6px; background: linear-gradient(90deg, #FF8C00, #FF4500); border-radius: 10px; margin-bottom: 30px; }

        /* --- ESTILO DAS ABAS (TABS) --- */
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px;
            background-color: transparent;
        }

        .stTabs [data-baseweb="tab"] {
            height: 70px !important; /* Abas mais altas */
            background: #f8f9fa !important;
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; /* Letras grandes para facilitar leitura */
            font-weight: 600 !important;
            color: #888 !important;
            border: 1px solid #eee !important;
            transition: all 0.3s ease-in-out !important;
        }

        /* IDENTIFICAÇÃO DA ABA ATIVA (LARANJA METALIZADO) */
        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #FF9D26 0%, #FF6F00 50%, #E65C00 100%) !important;
            color: white !important;
            font-weight: 800 !important;
            box-shadow: 
                inset 0 1px 0 rgba(255,255,255,0.4), 
                0 -5px 15px rgba(230, 92, 0, 0.3) !important;
            border: none !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.1);
            transform: translateY(-2px);
        }

        /* BOTÃO LARANJA METALIZADO REAL */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #FF9D26 0%, #FF6F00 50%, #E65C00 100%) !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 1px solid #FF8C00 !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 4px 15px rgba(230, 92, 0, 0.3) !important;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        .stButton > button:hover {
            filter: brightness(1.15);
            transform: translateY(-1px);
        }

        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #FF6F00;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
