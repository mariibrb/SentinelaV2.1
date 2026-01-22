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
        
        /* FUNDO CREME QUENTE (PARA COMBINAR COM O CHOCOLATE) */
        .stApp {
            background-color: #FAF7F2 !important; 
        }

        /* AJUSTE DO CONTEÚDO */
        .block-container { padding-top: 2rem !important; }
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* TÍTULOS EM CHOCOLATE PROFUNDO */
        .titulo-principal { color: #3D2314; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { 
            width: 80px; 
            height: 6px; 
            background: linear-gradient(90deg, #FF69B4, #3D2314); 
            border-radius: 10px; 
            margin-bottom: 30px; 
        }

        /* ABAS METALIZADAS - CHOCOLATE COM BRILHO */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #E3D5CA !important; /* Tom café com leite quente */
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            color: #3D2314 !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }

        /* BRILHO PINK NO HOVER (O TOQUE MARIANA) */
        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.1) !important;
            transform: translateY(-3px) !important;
            background: #F2E9E4 !important;
            box-shadow: 0 10px 20px rgba(255, 105, 180, 0.2) !important;
            border-top: 2px solid #FF69B4 !important;
        }

        /* ABA ATIVA - CHOCOLATE AMARGO COM ILUMINAÇÃO PINK */
        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #5C3D2E 0%, #3D2314 50%, #24140B 100%) !important;
            color: #FFFFFF !important;
            font-weight: 800 !important;
            box-shadow: 0 -5px 20px rgba(255, 105, 180, 0.3) !important;
            border-top: 3px solid #FF69B4 !important;
            filter: contrast(1.1) !important;
        }

        /* BOTÕES LUXO - CHOCOLATE COM BORDA PINK DIAMOND */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #5C3D2E 0%, #3D2314 50%, #24140B 100%) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 2px solid #FF69B4 !important; /* PINK HOT */
            box-shadow: inset 0 2px 3px rgba(255, 255, 255, 0.2), 0 4px 10px rgba(255, 105, 180, 0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 105, 180, 0.5) !important; /* Brilho Pink forte no hover */
            filter: brightness(1.2) !important;
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #FF69B4;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        /* MÉTRICAS */
        [data-testid="stMetricValue"] {
            color: #3D2314 !important;
            text-shadow: 0px 0px 10px rgba(255, 105, 180, 0.15);
        }
        </style>
    """, unsafe_allow_html=True)
