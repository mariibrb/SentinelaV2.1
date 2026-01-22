import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR ETERNA --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; /* MOCHA MOUSSE */
            border-right: 3px solid #FF69B4 !important; /* ROSA GLOSS */
            z-index: 999999 !important;
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE SUAVE */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important; 
        }
        
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER MONTSERRAT --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; /* MOCHA PROFUNDO */
            font-size: 3.2rem; 
            font-weight: 800; 
            text-transform: uppercase;
        }

        /* --- ASPECTO DIVISÓRIA DE FICHÁRIO METALIZADA --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        /* Estilo Inativo: Metal Bronzeado */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: linear-gradient(180deg, #E8DCCB 0%, #D4A373 100%) !important;
            border-radius: 25px 60px 0 0 !important; /* CURVA DE FICHÁRIO */
            margin-right: -15px !important; 
            padding: 0px 45px !important;
            border: 1px solid #A67B5B !important;
            font-weight: 600 !important;
            color: #5D3A1A !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 5px 0 15px rgba(0,0,0,0.1) !important;
        }

        /* --- LÓGICA DE CORES: MOCHA & ROSA PINK (METALIZADO + GLOW) --- */

        /* 🔵 FAMÍLIA XML: AZUL METALIZADO (Aba Mãe) */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #B0E0E6 0%, #4682B4 100%) !important;
            color: white !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #00D1FF !important;
            box-shadow: 0 0 25px rgba(0, 209, 255, 0.6) !important; /* GLOW AZUL */
            z-index: 100 !important;
        }

        /* 💗 FAMÍLIA FISCAL: ROSA PINK GLOSS (Mãe e Filhas: ICMS, PIS, RET, DIFAL) */
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("ICMS"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("PIS"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("RET"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("DIFAL"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #FF1493 !important;
            box-shadow: 0 0 25px rgba(255, 105, 180, 0.6) !important; /* GLOW ROSA */
            z-index: 100 !important;
        }

        /* --- SUB-ABAS (Rosa e menores, mas sobem igual) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            border-radius: 15px 35px 0 0 !important;
            background: #FFFFFF !important;
        }

        /* BOTÃO ADM COM BRILHO ROSA PINK */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #D4145A) !important;
            color: white !important; 
            box-shadow: 0 0 20px rgba(255, 20, 147, 0.5) !important;
            font-weight: 800 !important;
            border-radius: 40px !important;
            border: none !important;
        }

        /* BOTÕES DO SISTEMA (MOCHA METAL) */
        .stButton > button {
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            text-transform: uppercase;
        }
        </style>
    """, unsafe_allow_html=True)
