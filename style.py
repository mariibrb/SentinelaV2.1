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
            border-right: 2px solid #FF69B4 !important;
            z-index: 999999 !important;
        }

        /* RESET DO LIXO VISUAL */
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

        /* --- TÍTULO DESIGNER --- */
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
            width: 60px; height: 3px; background: #FF69B4; 
            border-radius: 50px; margin-top: 10px; margin-bottom: 50px;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.9);
        }

        /* --- ESTILIZAÇÃO DIVISÓRIAS DE FICHÁRIO METALIZADO --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 5px !important;
            background-color: transparent !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: linear-gradient(180deg, #E0E0E0 0%, #BDBDBD 100%) !important; /* Metal Inativo */
            border-radius: 15px 40px 0 0 !important;
            margin-right: -10px !important;
            padding: 0px 45px !important;
            border: 1px solid #9E9E9E !important;
            font-weight: 600 !important;
            color: #616161 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), 5px 0 10px rgba(0,0,0,0.1) !important;
        }

        /* --- MÓDULOS COM ACABAMENTO METALIZADO E GLOW --- */

        /* ABA 1: GARIMPEIRO (Ouro Rosé Metalizado) */
        .stTabs [data-baseweb="tab"]:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB7C5 0%, #FF69B4 100%) !important;
            color: white !important;
            z-index: 10 !important;
            transform: translateY(-8px) scale(1.05) !important;
            border: 1px solid #FF1493 !important;
            box-shadow: 0 10px 30px rgba(255, 105, 180, 0.5), inset 0 2px 4px rgba(255,255,255,0.6) !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        }

        /* ABA 2: CONFORMIDADE (Prata Cromada / Azul Ice) */
        .stTabs [data-baseweb="tab"]:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            z-index: 10 !important;
            transform: translateY(-8px) scale(1.05) !important;
            border: 1px solid #0099CC !important;
            box-shadow: 0 10px 30px rgba(0, 191, 255, 0.5), inset 0 2px 4px rgba(255,255,255,0.6) !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        }

        /* --- BOTÃO ADM METALIZADO --- */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #D4145A) !important;
            color: white !important; 
            border-radius: 40px !important;
            font-weight: 800 !important;
            border: 1px solid #FFFFFF55 !important;
            box-shadow: 0 15px 35px rgba(255, 20, 147, 0.4), inset 0 -4px 10px rgba(0,0,0,0.2) !important;
        }

        /* --- BOTÕES DO SISTEMA (BRONZE ESCOVADO) --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #D4A373 0%, #A67B5B 100%) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-weight: 600 !important;
            border: 1px solid #8B5A2B !important;
            box-shadow: 0 8px 20px rgba(139, 90, 43, 0.2), inset 0 2px 2px rgba(255,255,255,0.3) !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: scale(1.02) !important;
            filter: brightness(1.1) !important;
            box-shadow: 0 12px 25px rgba(255, 105, 180, 0.3) !important;
        }

        /* CONTAINER DE STATUS METAL */
        .status-container {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            padding: 20px;
            border-radius: 30px;
            border-left: 8px solid #FF69B4;
            box-shadow: 10px 10px 30px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
