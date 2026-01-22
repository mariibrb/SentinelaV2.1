import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR ETERNA --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            display: block !important;
            visibility: visible !important;
            position: relative !important;
            background-color: #F3E9DC !important; 
            border-right: 2px solid #FFB6C1 !important; 
            z-index: 999999 !important;
        }

        [data-testid="sidebar-close-button"], 
        button[aria-label="Close sidebar"],
        .st-emotion-cache-6qob1r {
            display: none !important;
            visibility: hidden !important;
        }

        /* RESET DO LIXO VISUAL DO STREAMLIT */
        header, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"] {
            display: none !important;
        }

        /* FUNDO MOCHA MOUSSE */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important; 
        }
        
        .block-container { padding-top: 2.5rem !important; }
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER MONTSERRAT --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.2rem; 
            font-weight: 800; 
            margin-bottom: 0px;
            letter-spacing: -1px;
            text-transform: uppercase;
            line-height: 1;
        }
        .titulo-principal span { font-weight: 200 !important; color: #A67B5B; }

        .barra-marsala { 
            width: 60px; height: 3px; background: #FFB6C1; 
            border-radius: 50px; margin-top: 10px; margin-bottom: 50px;
            box-shadow: 0 0 20px rgba(255, 182, 193, 0.9);
        }

        /* --- ESTILIZAÇÃO DIVISÓRIAS DE FICHÁRIO METALIZADO --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 5px !important;
            background-color: transparent !important;
        }

        /* Configuração Geral das Abas (Separadores) */
        .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: linear-gradient(180deg, #F0F0F0 0%, #D1D1D1 100%) !important;
            border-radius: 15px 40px 0 0 !important;
            margin-right: -10px !important;
            padding: 0px 45px !important;
            border: 1px solid #C0C0C0 !important;
            font-weight: 600 !important;
            color: #888888 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), 5px 0 10px rgba(0,0,0,0.05) !important;
        }

        /* --- CORES POR ASSUNTO (METALIZADO + BRILHO) --- */

        /* ABA 1: ANÁLISE XML (Azul Bebê Metalizado) */
        .stTabs [data-baseweb="tab"]:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #B0E0E6 0%, #87CEEB 100%) !important;
            color: #4682B4 !important;
            z-index: 10 !important;
            transform: translateY(-8px) !important;
            border: 1px solid #ADD8E6 !important;
            box-shadow: 0 10px 30px rgba(173, 216, 230, 0.6), inset 0 2px 4px rgba(255,255,255,0.8) !important;
        }

        /* ABA 2: CONFORMIDADE (Rosa Bebê Metalizado) */
        .stTabs [data-baseweb="tab"]:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFD1DC 0%, #FFB6C1 100%) !important;
            color: #DB7093 !important;
            z-index: 10 !important;
            transform: translateY(-8px) !important;
            border: 1px solid #FFB6C1 !important;
            box-shadow: 0 10px 30px rgba(255, 182, 193, 0.6), inset 0 2px 4px rgba(255,255,255,0.8) !important;
        }

        /* --- SUB-ABAS (Sempre em Rosa Bebê conforme pedido) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 45px !important;
            font-size: 13px !important;
            background: #FFFFFF !important;
            border-radius: 10px !important;
            margin-right: 5px !important;
            border: 1px solid #FFD1DC !important;
        }
        
        .stTabs .stTabs [aria-selected="true"] {
            background: #FFD1DC !important;
            color: #DB7093 !important;
            box-shadow: 0 5px 15px rgba(255, 182, 193, 0.4) !important;
        }

        /* --- BOTÕES BOUTIQUE --- */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FFB6C1, #FF69B4) !important;
            color: #5D3A1A !important; 
            border-radius: 40px !important;
            font-weight: 800 !important;
            box-shadow: 0 10px 25px rgba(255, 182, 193, 0.5) !important;
        }

        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-weight: 600 !important;
            box-shadow: 0 8px 20px rgba(139, 90, 43, 0.2) !important;
            text-transform: uppercase;
        }

        /* CONTAINER DE STATUS */
        .status-container {
            background: white;
            padding: 20px;
            border-radius: 30px;
            border-left: 8px solid #FFB6C1;
            box-shadow: 0 10px 40px rgba(0,0,0,0.03);
        }
        </style>
    """, unsafe_allow_html=True)
