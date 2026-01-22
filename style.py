import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 4px solid #FF69B4 !important;
            z-index: 999999 !important;
            box-shadow: 10px 0 30px rgba(0,0,0,0.1) !important;
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE PROFISSIONAL */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }
        
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }

        /* --- SISTEMA DE FICHÁRIO (PASTINHAS) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important;
            background-color: transparent !important;
            padding: 30px 0 !important;
            align-items: flex-end;
        }

        /* ABA MÃE INATIVA (METALIZADO BRONZE) */
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 30px 80px 0 0 !important;
            margin-right: -25px !important;
            padding: 0px 60px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 8px 0 15px rgba(0,0,0,0.1), inset 0 2px 5px rgba(255,255,255,0.5) !important;
        }

        /* --- O BRILHO NEON EXTREMO (AQUI ESTÁ O SEGREDO) --- */

        /* 🔵 PASTA XML ATIVA (AZUL NEON) */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.06) !important;
            border-color: #00D1FF !important;
            /* CAMADAS DE BRILHO NEON QUE VOCÊ AMOU: */
            box-shadow: 0 0 15px #00D1FF, 0 0 30px #00D1FF, 0 0 60px rgba(0, 209, 255, 0.4), inset 0 5px 10px rgba(255,255,255,0.8) !important;
            z-index: 100 !important;
            text-shadow: 0 0 10px rgba(255,255,255,0.5) !important;
        }

        /* 💗 PASTA FISCAL ATIVA (ROSA NEON GLOSS) */
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.06) !important;
            border-color: #FF69B4 !important;
            /* CAMADAS DE BRILHO NEON QUE VOCÊ AMOU: */
            box-shadow: 0 0 15px #FF69B4, 0 0 30px #FF69B4, 0 0 60px rgba(255, 105, 180, 0.4), inset 0 5px 10px rgba(255,255,255,0.8) !important;
            z-index: 100 !important;
            text-shadow: 0 0 10px rgba(255,255,255,0.5) !important;
        }

        /* --- PAINEL INTERNO (GAVETA ABERTA) --- */
        .stTabs .stTabs {
            background: rgba(255, 255, 255, 0.7) !important;
            padding: 30px !important;
            border-radius: 0 40px 40px 40px !important;
            border: 3px solid #FFB6C1 !important;
            border-top: 8px solid #FF69B4 !important; /* CONEXÃO COM A CAPA ROSA */
            /* BRILHO NEON REFLETIDO NO PAINEL */
            box-shadow: 0 0 40px rgba(255, 105, 180, 0.2), inset 0 10px 30px rgba(0,0,0,0.05) !important;
            margin-top: -15px !important;
            animation: slideUp 0.5s ease-out;
        }

        /* SUB-ABAS (FICHAS NEON) */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: #FFFFFF !important;
            border-radius: 15px 40px 0 0 !important;
            font-size: 1.1rem !important;
            color: #DB7093 !important;
            border: 1px solid #FFD1DC !important;
            margin-right: 5px !important;
        }

        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFB6C1 100%) !important;
            color: #C71585 !important;
            transform: translateY(-10px) !important;
            /* BRILHO NEON NA SUB-ABA */
            box-shadow: 0 0 15px #FFB6C1, 0 10px 20px rgba(255, 182, 193, 0.8) !important;
            border-bottom: 4px solid #FF69B4 !important;
        }

        /* EFEITO HOVER */
        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.2) !important;
            transform: translateY(-5px) !important;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
    """, unsafe_allow_html=True)
