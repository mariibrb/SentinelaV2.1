import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. SIDEBAR E FUNDO --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 5px solid #FF69B4 !important;
            z-index: 999999 !important;
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }

        /* --- 2. TÍTULO SHINE --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            text-shadow: 0 0 15px rgba(255, 105, 180, 0.4);
        }

        /* --- 3. ABAS MESTRE (SETORIZAÇÃO) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] { gap: 20px !important; padding: 40px 0 !important; }

        .stTabs [data-baseweb="tab"] {
            height: 90px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 40px 110px 0 0 !important; 
            margin-right: -35px !important;
            padding: 0px 75px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.7rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            box-shadow: 10px 0 20px rgba(0,0,0,0.15), inset 0 2px 5px rgba(255,255,255,0.8) !important;
        }

        /* 🔵 SETOR XML: AZUL */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            border-color: #00D1FF !important;
            box-shadow: 0 0 50px rgba(0, 209, 255, 0.6), inset 0 5px 15px rgba(255,255,255,0.8) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
        }

        /* 💗 SETOR CONFORMIDADE: ROSA */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            border-color: #FF1493 !important;
            box-shadow: 0 0 50px rgba(255, 105, 180, 0.7), inset 0 5px 15px rgba(255,255,255,0.8) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
        }

        /* --- 4. 📦 O PAINEL DE FUNDO (GAVETA GERAL) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -20px !important;
            box-shadow: 0 20px 80px rgba(0,0,0,0.05) !important;
            border: 4px solid transparent !important;
        }

        /* --- 📂 A CAIXA GIGANTE DE UPLOAD (MOLDURA NEON) --- */
        div[data-testid="stHorizontalBlock"] {
            background: #FFFFFF !important;
            padding: 45px !important; /* Aumentei o espaço interno */
            border-radius: 45px !important;
            margin: 30px 0 !important;
            transition: all 0.4s ease !important;
        }

        /* 🔵 Moldura Neon Azul (Setor XML) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 3px solid #00D1FF !important;
            box-shadow: 0 0 25px rgba(0, 209, 255, 0.2), inset 0 0 15px rgba(0, 209, 255, 0.05) !important;
        }

        /* 💗 Moldura Neon Rosa (Setor Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 3px solid #FFB6C1 !important;
            box-shadow: 0 0 25px rgba(255, 182, 193, 0.3), inset 0 0 15px rgba(255, 182, 193, 0.05) !important;
        }

        /* Limpeza dos campos individuais */
        [data-testid="stFileUploader"] {
            background: #F8F9FA !important;
            border: 1px dashed #D8C7B1 !important;
            border-radius: 20px !important;
        }

        /* --- 5. SUB-ABAS SETORIZADAS --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 65px !important;
            background: #FDFDFD !important;
            border-radius: 20px 55px 0 0 !important;
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            margin-right: -10px !important;
        }

        /* Ativas (Azul e Rosa) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            box-shadow: 0 0 20px #00D1FF !important;
            transform: translateY(-12px) !important;
        }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            box-shadow: 0 0 20px #FF69B4 !important;
            transform: translateY(-12px) !important;
        }

        .stTabs .stTabs [aria-selected="true"] div { color: white !important; }

        </style>
    """, unsafe_allow_html=True)
