import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* RESET TOTAL DO VISUAL */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* FUNDO DE ESTÚDIO LIMPO */
        .stApp {
            background: #FDFBF9 !important;
        }

        .block-container { padding-top: 2.5rem !important; }
        
        /* FONTE PRINCIPAL */
        html, body, [class*="st-"] { 
            font-family: 'Plus Jakarta Sans', sans-serif !important; 
        }

        /* --- O TÍTULO "DESIGNER" (FINO E IMPACTANTE) --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #3D2B1F; 
            font-size: 3.2rem; 
            font-weight: 800; 
            margin-bottom: 0px;
            letter-spacing: -1px;
            line-height: 1;
            text-transform: uppercase;
        }
        
        .titulo-principal span {
            font-weight: 200 !important; /* O "2.1" fica ultra fino e elegante */
            color: #A67B5B;
        }

        /* LINHA DE LUZ (SAI A BARRA GORDA, ENTRA A LINHA FINA) */
        .barra-marsala { 
            width: 60px; 
            height: 3px; /* Super fina */
            background: #FF69B4; 
            border-radius: 50px; 
            margin-top: 10px;
            margin-bottom: 50px;
            box-shadow: 0 0 15px rgba(255, 105, 180, 0.6); /* Brilho neon suave */
        }

        /* ABAS PÍLULA FLUTUANTES (MAIS REFINADAS) */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px !important;
            background-color: transparent !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 48px !important; /* Mais baixinha e elegante */
            background: rgba(230, 213, 195, 0.2) !important;
            border-radius: 25px !important; 
            padding: 0px 30px !important;
            font-size: 15px !important; 
            font-weight: 400 !important;
            color: #5D4D42 !important;
            border: 1px solid rgba(255, 255, 255, 0.8) !important;
            transition: all 0.4s ease !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-2px) !important;
            background: white !important;
            color: #FF69B4 !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05) !important;
        }

        .stTabs [aria-selected="true"] {
            background: #3D2B1F !important;
            color: white !important;
            font-weight: 600 !important;
            box-shadow: 0 8px 20px rgba(61, 43, 31, 0.2) !important;
        }

        /* --- BOTÃO ADMINISTRATIVO (PINK MARIANA REFINADO) --- */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: #FF69B4 !important;
            color: #3D2B1F !important; 
            border-radius: 40px !important;
            border: 1.5px solid #3D2B1F !important;
            box-shadow: 0 5px 15px rgba(255, 105, 180, 0.3) !important;
            font-weight: 700 !important;
            height: 45px !important;
        }

        /* --- BOTÕES DO SISTEMA (MOCA MOUSSE SLIM) --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: #5D3A1A !important; /* Cor sólida Mocha Mousse Nobre */
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s ease !important;
            letter-spacing: 0.5px;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            background: #3D2B1F !important;
            box-shadow: 0 10px 25px rgba(255, 105, 180, 0.3) !important; 
        }

        /* CONTAINER DE STATUS REFINADO */
        .status-container {
            background: white;
            padding: 20px;
            border-radius: 30px;
            border-left: 5px solid #FF69B4;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        }
        </style>
    """, unsafe_allow_html=True)
