import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* RESET TOTAL E REMOÇÃO DO BOTÃO DE FECHAR SIDEBAR */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"],
        [data-testid="sidebar-close-button"] { /* REMOVE O BOTÃO DE FECHAR */
            display: none !important;
            visibility: hidden !important;
        }
        
        .stApp { background: #FDFBF9 !important; }
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
        }
        .titulo-principal span { font-weight: 200 !important; color: #A67B5B; }

        .barra-marsala { 
            width: 60px; height: 3px; background: #FF69B4; 
            border-radius: 50px; margin-top: 10px; margin-bottom: 50px;
            box-shadow: 0 0 15px rgba(255, 105, 180, 0.6);
        }

        /* --- SIDEBAR BOUTIQUE (FIXO E SEM BOTÃO) --- */
        [data-testid="stSidebar"] {
            background-color: #F3E9DC !important;
            border-right: 1px solid rgba(166, 123, 91, 0.2) !important;
        }
        
        /* Força a largura e impede o colapso visual */
        [data-testid="stSidebar"][aria-expanded="true"] {
            min-width: 350px !important;
            max-width: 350px !important;
        }

        /* --- HIERARQUIA DE ABAS (O SEGREDO DA CONEXÃO) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        /* Abas Pai (Nível 1) - Maiores e imponentes */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px !important;
            background-color: transparent !important;
            margin-bottom: 20px !important;
        }

        /* Abas Filhas (Nível 2 - Dentro de Conformidade) */
        /* Aplicamos um recuo e uma escala menor para parecerem "dentro" */
        [data-testid="stVerticalBlock"] [data-testid="stVerticalBlock"] .stTabs [data-baseweb="tab"] {
            height: 40px !important;
            font-size: 13px !important;
            padding: 0px 20px !important;
            background: rgba(255, 255, 255, 0.5) !important;
            border-radius: 15px !important;
            margin-top: 10px !important;
            border: 1px dashed #BC8F8F !important; /* Linha tracejada para indicar conexão */
        }

        /* Efeito de Pílulas Flutuantes Gerais */
        .stTabs [data-baseweb="tab"] {
            height: 48px !important;
            background: rgba(166, 123, 91, 0.15) !important;
            border-radius: 25px !important; 
            padding: 0px 30px !important;
            font-size: 15px !important; 
            font-weight: 400 !important;
            color: #5D3A1A !important;
            transition: all 0.4s ease !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-2px) !important;
            background: white !important;
            color: #FF69B4 !important;
            box-shadow: 0 10px 20px rgba(255, 105, 180, 0.2) !important;
        }

        .stTabs [aria-selected="true"] {
            background: #5D3A1A !important;
            color: white !important;
            font-weight: 600 !important;
            box-shadow: 0 8px 20px rgba(93, 58, 26, 0.2) !important;
        }

        /* --- BOTÃO ADMINISTRATIVO PINK & MARROM --- */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #FF1493) !important;
            color: #5D3A1A !important; 
            border-radius: 40px !important;
            border: 2px solid #5D3A1A !important;
            box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4) !important;
            font-weight: 800 !important;
        }

        /* --- BOTÕES DO SISTEMA --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #A67B5B, #5D3A1A) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            border: none !important;
            text-transform: uppercase;
        }

        .status-container {
            background: white;
            padding: 20px;
            border-radius: 30px;
            border-left: 5px solid #FF69B4;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        }
        </style>
    """, unsafe_allow_html=True)
