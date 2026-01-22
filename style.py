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
        
        /* FUNDO OFF-WHITE SUAVE */
        .stApp {
            background-color: #FDFBFA !important; 
        }

        /* AJUSTE DO CONTEÚDO */
        .block-container { padding-top: 2rem !important; }
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* TÍTULOS EM MOCA MOUSSE PROFUNDO */
        .titulo-principal { color: #5B4D42; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { 
            width: 80px; 
            height: 6px; 
            background: linear-gradient(90deg, #DB7093, #5B4D42); 
            border-radius: 10px; 
            margin-bottom: 30px; 
        }

        /* ABAS METALIZADAS - PALETA MOCA MOUSSE */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #E8E2DD !important; /* Tom Moca Mousse Claro */
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            color: #5B4D42 !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            border: 1px solid transparent !important;
        }

        /* EFEITO LUZ PINK NO HOVER (O SEU TOQUE ESPECIAL) */
        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.05) !important;
            transform: translateY(-3px) !important;
            background: #F2ECE9 !important;
            box-shadow: 0 10px 20px rgba(219, 112, 147, 0.2) !important; /* Glow Pink Sutil */
            border-top: 2px solid #DB7093 !important;
        }

        /* ABA ATIVA - MOCA MOUSSE FECHADO COM ILUMINAÇÃO PINK */
        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #7D6B5D 0%, #5B4D42 50%, #453A32 100%) !important;
            color: #FFFFFF !important;
            font-weight: 800 !important;
            box-shadow: 0 -5px 20px rgba(219, 112, 147, 0.25) !important;
            border-top: 3px solid #DB7093 !important;
            filter: contrast(1.05) !important;
        }

        /* BOTÕES LUXO - MOCA MOUSSE COM BRILHO METALIZADO E BORDA PINK */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #8C7A6B 0%, #5B4D42 50%, #453A32 100%) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 2px solid #DB7093 !important; /* Borda Pink Suave */
            box-shadow: inset 0 2px 3px rgba(255, 255, 255, 0.2), 0 4px 10px rgba(0, 0, 0, 0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(219, 112, 147, 0.4) !important; /* Glow Pink no Hover */
            filter: brightness(1.2) !important;
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #DB7093;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        /* MÉTRICAS (MANTENDO O EQUILÍBRIO) */
        [data-testid="stMetricValue"] {
            color: #5B4D42 !important;
            text-shadow: 0px 0px 10px rgba(219, 112, 147, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)
