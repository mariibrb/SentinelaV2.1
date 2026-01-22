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
        
        /* FUNDO OFF-WHITE QUENTE */
        .stApp {
            background-color: #FDFBF9 !important; 
        }

        /* AJUSTE DO CONTEÚDO */
        .block-container { padding-top: 2rem !important; }
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* TÍTULOS EM MOCHA MOUSSE PROFUNDO */
        .titulo-principal { color: #5D3A1A; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { 
            width: 80px; 
            height: 6px; 
            background: linear-gradient(90deg, #FF69B4, #A67B5B); 
            border-radius: 10px; 
            margin-bottom: 30px; 
        }

        /* ABAS METALIZADAS - CARAMELO MOCHA */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #E6D5C3 !important; 
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            color: #5D3A1A !important; /* Texto Marrom padrão */
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            border: 1px solid transparent !important;
        }

        /* CORREÇÃO DE LEGIBILIDADE NO HOVER (BRILHO PINK + TEXTO ESCURO) */
        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.05) !important;
            transform: translateY(-3px) !important;
            background: #F0E2D3 !important;
            color: #3E2511 !important; /* TEXTO ESCURECE NO HOVER PARA DAR LEITURA */
            box-shadow: 0 10px 20px rgba(255, 105, 180, 0.2) !important;
            border-top: 2px solid #FF69B4 !important;
        }

        /* ABA ATIVA - MOCHA CARAMELO COM ILUMINAÇÃO PINK */
        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #A67B5B 0%, #5D3A1A 50%, #3E2511 100%) !important;
            color: #FFFFFF !important; /* Texto Branco para contraste total no Marrom */
            font-weight: 800 !important;
            box-shadow: 0 -5px 20px rgba(255, 105, 180, 0.3) !important;
            border-top: 3px solid #FF69B4 !important;
            filter: contrast(1.1) !important;
        }

        /* BOTÕES LUXO - CARAMELO MOCHA COM BORDA PINK GLOSS */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #A67B5B 0%, #5D3A1A 50%, #3E2511 100%) !important;
            color: #FFFFFF !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 2px solid #FF69B4 !important; 
            box-shadow: inset 0 2px 3px rgba(255, 255, 255, 0.3), 0 4px 10px rgba(255, 105, 180, 0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 105, 180, 0.5) !important; 
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
            color: #5D3A1A !important;
            text-shadow: 0px 0px 10px rgba(255, 105, 180, 0.15);
        }
        </style>
    """, unsafe_allow_html=True)
