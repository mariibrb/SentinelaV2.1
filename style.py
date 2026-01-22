import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- CONFIGURAÇÃO DA SIDEBAR --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 3px solid #FFB6C1 !important; 
            z-index: 999999 !important;
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important; 
        }
        
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.2rem; 
            font-weight: 800; 
            text-transform: uppercase;
        }

        /* --- ASPECTO DIVISÓRIA DE FICHÁRIO METALIZADA --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #E0E0E0 100%) !important;
            border-radius: 25px 60px 0 0 !important; /* CURVA DE FICHÁRIO */
            margin-right: -15px !important; 
            padding: 0px 45px !important;
            border: 1px solid #D1D1D1 !important;
            font-weight: 600 !important;
            color: #A0A0A0 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 5px 0 15px rgba(0,0,0,0.05) !important;
        }

        /* --- LÓGICA DE CORES POR CONTEXTO (BRILHO E ELEVAÇÃO) --- */

        /* 🔵 FAMÍLIA XML (AZUL BEBÊ) */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #E0FFFF 0%, #B0E0E6 100%) !important;
            color: #4682B4 !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #00D1FF !important;
            box-shadow: 0 -10px 20px rgba(0, 209, 255, 0.4), 0 0 30px rgba(0, 209, 255, 0.3) !important;
            z-index: 100 !important;
        }

        /* 💗 FAMÍLIA FISCAL - MÃE E FILHAS (ROSA BEBÊ) */
        /* Esta regra agora pega pelo nome, então ICMS/IPI ficará rosa! */
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("ICMS"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("PIS"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("RET"))[aria-selected="true"],
        .stTabs [data-baseweb="tab"]:has(div:contains("DIFAL"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFB6C1 100%) !important;
            color: #DB7093 !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #FF69B4 !important;
            box-shadow: 0 -10px 20px rgba(255, 105, 180, 0.4), 0 0 30px rgba(255, 105, 180, 0.3) !important;
            z-index: 100 !important;
        }

        /* --- SUB-ABAS (Sempre Rosa Bebê) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            border-radius: 15px 35px 0 0 !important;
            margin-right: -10px !important;
        }

        /* BOTÃO ADM COM BRILHO */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FFB6C1, #FF1493) !important;
            color: white !important; 
            box-shadow: 0 0 20px rgba(255, 20, 147, 0.6) !important;
            font-weight: 800 !important;
            border-radius: 40px !important;
        }
        </style>
    """, unsafe_allow_html=True)
