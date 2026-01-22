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

        /* --- ESTILIZAÇÃO DIVISÓRIAS DE FICHÁRIO (ASPECTO FÍSICO) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px !important;
            background-color: transparent !important;
            padding: 20px 0 !important;
        }

        /* Estilo Inativo: Metal Fosco com Curva de Fichário */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #E0E0E0 100%) !important;
            border-radius: 25px 60px 0 0 !important; /* FORMATO DE DIVISÓRIA */
            margin-right: -20px !important; /* SOBREPOSIÇÃO TIPO FICHÁRIO */
            padding: 0px 50px !important;
            border: 1px solid #D1D1D1 !important;
            font-weight: 600 !important;
            color: #A0A0A0 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 5px 0 15px rgba(0,0,0,0.05) !important;
        }

        /* --- BRILHO E ELEVAÇÃO: ABAS MÃE --- */

        /* 🔵 ANÁLISE XML: AZUL BEBÊ METALIZADO + GLOW */
        .stTabs [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #E0FFFF 0%, #B0E0E6 100%) !important;
            color: #4682B4 !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #00D1FF !important;
            /* Efeito Glow Extremo */
            box-shadow: 0 -10px 20px rgba(0, 209, 255, 0.4), 0 0 30px rgba(0, 209, 255, 0.3) !important;
            z-index: 100 !important;
        }

        /* 💗 CONFORMIDADE: ROSA BEBÊ METALIZADO + GLOW */
        .stTabs [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFB6C1 100%) !important;
            color: #DB7093 !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #FF69B4 !important;
            /* Efeito Glow Extremo */
            box-shadow: 0 -10px 20px rgba(255, 105, 180, 0.4), 0 0 30px rgba(255, 105, 180, 0.3) !important;
            z-index: 100 !important;
        }

        /* --- SUB-ABAS: ROSA BEBÊ (IDENTIDADE FISCAL) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #FFFFFF !important;
            border-radius: 15px 35px 0 0 !important;
            font-size: 13px !important;
            border: 1px solid #FFD1DC !important;
        }

        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFD1DC 100%) !important;
            color: #C71585 !important;
            transform: translateY(-8px) !important;
            box-shadow: 0 0 20px rgba(255, 182, 193, 0.6) !important;
            border-top: 3px solid #FF69B4 !important;
        }

        /* BRILHO NO HOVER (MOUUSE SOBRE A ABA) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            filter: brightness(1.1) !important;
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
