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
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE */
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
        }

        /* --- SISTEMA DE FICHÁRIO (PASTINHAS) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important;
            background-color: transparent !important;
            padding: 20px 0 !important;
            align-items: flex-end;
        }

        /* ABA MÃE (CAPA DA PASTA) */
        .stTabs [data-baseweb="tab"] {
            height: 80px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important; /* Metalizado Mocha */
            border-radius: 30px 80px 0 0 !important; /* Curva de pasta real */
            margin-right: -20px !important;
            padding: 0px 60px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            transition: all 0.4s ease !important;
            box-shadow: 8px 0 15px rgba(0,0,0,0.1) !important;
        }

        /* --- ABA MÃE ABERTA (BRILHANDO E "PUXADA") --- */
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            transform: translateY(-20px) scale(1.05) !important;
            z-index: 100 !important;
            border-bottom: 5px solid white !important; /* Remove a linha de baixo para parecer que abriu */
        }

        /* BRILHO NEON DA PASTA XML (AZUL) */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            border-color: #00D1FF !important;
            box-shadow: 0 -15px 30px rgba(0, 209, 255, 0.4), 0 10px 40px rgba(0, 209, 255, 0.2) !important;
        }

        /* BRILHO NEON DA PASTA FISCAL (ROSA) */
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            border-color: #FF69B4 !important;
            box-shadow: 0 -15px 30px rgba(255, 105, 180, 0.4), 0 10px 40px rgba(255, 105, 180, 0.2) !important;
        }

        /* --- SUB-PASTINHAS (SAINDO DE DENTRO) --- */
        .stTabs .stTabs {
            background: rgba(255, 255, 255, 0.5) !important; /* Fundo translúcido */
            padding: 25px !important;
            border-radius: 0 30px 30px 30px !important;
            border: 2px solid #FFB6C1 !important;
            border-top: 5px solid #FF69B4 !important; /* Linha que conecta com a aba mãe */
            box-shadow: inset 0 10px 20px rgba(0,0,0,0.05) !important;
            margin-top: -10px !important; /* "Encaixa" debaixo da mãe */
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: white !important;
            border-radius: 15px 40px 0 0 !important;
            font-size: 1.1rem !important;
            color: #DB7093 !important;
            border: 1px solid #FFD1DC !important;
            margin-right: 5px !important;
        }

        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFB6C1 100%) !important;
            color: #C71585 !important;
            transform: translateY(-8px) !important;
            box-shadow: 0 8px 15px rgba(255, 182, 193, 0.6) !important;
        }

        /* BOTÕES DO SISTEMA */
        .stButton > button {
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            border-radius: 40px !important;
            font-weight: 700 !important;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
        }
        </style>
    """, unsafe_allow_html=True)
