import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. SIDEBAR E FUNDO MOCHA --- */
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

        /* --- 2. TÍTULO SHINE DIAMOND --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            text-shadow: 0 0 20px rgba(255, 105, 180, 0.6), 0 0 40px rgba(255, 255, 255, 0.8) !important;
        }

        /* --- 3. ABAS MESTRE (PASTAS METALIZADAS) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] { 
            gap: 15px !important; 
            padding: 40px 0 0 20px !important; 
            align-items: flex-end;
        }

        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            margin-right: -30px !important;
            padding: 0px 70px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            box-shadow: 5px -5px 15px rgba(0,0,0,0.1), inset 0 2px 5px rgba(255,255,255,0.8) !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        /* 🔵 ATIVA XML (DIAMOND BLUE) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #E0F7FF 0%, #00BFFF 100%) !important;
            border-color: #00D1FF !important;
            box-shadow: 0 -10px 40px rgba(0, 209, 255, 0.5), inset 0 5px 20px rgba(255,255,255,1) !important;
            color: white !important;
            transform: translateY(-20px) scale(1.05) !important;
            z-index: 100 !important;
        }

        /* 💗 ATIVA CONFORMIDADE (DIAMOND PINK) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFD1E8 0%, #FF69B4 100%) !important;
            border-color: #FF1493 !important;
            box-shadow: 0 -10px 40px rgba(255, 105, 180, 0.6), inset 0 5px 20px rgba(255,255,255,1) !important;
            color: white !important;
            transform: translateY(-20px) scale(1.05) !important;
            z-index: 100 !important;
        }

        /* --- 4. 📦 O CAIXOTÃO BRANCO (PASTA ABERTA GIGANTE) --- */
        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.98) !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important; /* Colado na aba mãe para parecer pastinha */
            min-height: 700px !important;
            position: relative !important;
            z-index: 1 !important;
        }

        /* NEON SHINE BOATE (SOMENTE NA BORDA DO CAIXOTE) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #00D1FF !important;
            box-shadow: 0 0 20px #00D1FF, 0 0 60px rgba(0, 209, 255, 0.4), inset 0 0 15px rgba(255,255,255,1) !important;
        }

        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #FF69B4 !important;
            box-shadow: 0 0 20px #FF69B4, 0 0 60px rgba(255, 105, 180, 0.4), inset 0 0 15px rgba(255,255,255,1) !important;
        }

        /* --- 5. SUB-ABAS (DENTRO DO CAIXOTÃO) --- */
        .stTabs .stTabs [data-baseweb="tab-list"] {
            padding: 0 0 30px 0 !important;
            margin-top: 10px !important;
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F8F9FA !important;
            border-radius: 15px 45px 0 0 !important;
            font-size: 1.1rem !important;
            border: 1px solid #E8DCCB !important;
            margin-right: -10px !important;
        }

        /* SUB-ABAS ATIVAS (COM BRILHO DIAMANTE) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #00BFFF !important;
            box-shadow: 0 0 20px #00D1FF, inset 0 2px 10px rgba(255,255,255,0.8) !important;
            color: white !important;
        }

        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #FF69B4 !important;
            box-shadow: 0 0 20px #FF69B4, inset 0 2px 10px rgba(255,255,255,0.8) !important;
            color: white !important;
        }

        /* --- 📂 CAIXA DE UPLOAD (DENTRO DO BRILHO) --- */
        div[data-testid="stHorizontalBlock"] {
            background: #FFFFFF !important;
            padding: 30px !important;
            border-radius: 35px !important;
            border: 1px solid #eee !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03) !important;
        }

        </style>
    """, unsafe_allow_html=True)
