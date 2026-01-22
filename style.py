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
        
        /* FUNDO OFF-WHITE (SAI O ROSA INFANTIL, ENTRA O NEUTRO) */
        .stApp {
            background-color: #F8F5F2 !important; 
        }

        /* AJUSTE DO CONTEÚDO */
        .block-container { padding-top: 2rem !important; }
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* TÍTULOS EM MARROM CAFÉ */
        .titulo-principal { color: #3D2B1F; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { 
            width: 80px; 
            height: 6px; 
            background: linear-gradient(90deg, #D4A373, #3D2B1F); 
            border-radius: 10px; 
            margin-bottom: 30px; 
        }

        /* ABAS METALIZADAS - MARROM SÓBRIO */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #E5E1DA !important;
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            color: #3D2B1F !important;
            transition: all 0.3s ease !important;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #5D4037 0%, #3D2B1F 50%, #261A13 100%) !important;
            color: #F1D4D4 !important; /* Rosa seco apenas no texto ativo */
            font-weight: 800 !important;
            box-shadow: 0 -5px 15px rgba(61, 43, 31, 0.3) !important;
        }

        /* BOTÕES MARROM CHOCOLATE COM BORDA ROSA SECO (RESTAURADO E DISCRETO) */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #5D4037 0%, #3D2B1F 50%, #261A13 100%) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 2px solid #BC8F8F !important; /* ROSY BROWN (Rosa antigo/seco) */
            box-shadow: inset 0 2px 3px rgba(255,255,255,0.2), 0 4px 10px rgba(0,0,0,0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(188, 143, 143, 0.3) !important; /* Glow discreto */
            filter: brightness(1.2) !important;
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #BC8F8F; /* Detalhe em Rosa Seco */
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
