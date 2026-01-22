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

        /* --- 2. ABAS MESTRE (EFEITO GLOSS METALIZADO) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] { gap: 20px !important; padding: 40px 0 !important; }

        .stTabs [data-baseweb="tab"] {
            height: 80px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 30px 80px 0 0 !important; 
            margin-right: -25px !important;
            padding: 0px 60px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.5rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            /* SHINE INTERNO */
            box-shadow: inset 0 2px 5px rgba(255,255,255,0.8) !important;
        }

        /* 🔵 SHINE AZUL ATIVO */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            box-shadow: 0 0 40px #00D1FF, inset 0 5px 15px rgba(255,255,255,0.8) !important;
            color: white !important;
        }

        /* 💗 SHINE ROSA ATIVO */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            box-shadow: 0 0 40px #FF69B4, inset 0 5px 15px rgba(255,255,255,0.8) !important;
            color: white !important;
        }

        /* --- 3. 📦 O CAIXOTÃO BRANCO (NEON BLOOM + GLOSS) --- */
        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.95) !important;
            padding: 40px !important;
            border-radius: 40px !important;
            margin-top: -5px !important;
            min-height: 600px !important;
            border: 6px solid transparent !important;
            /* EFEITO GLITTER/SHINE NO FUNDO */
            box-shadow: inset 0 20px 40px rgba(0,0,0,0.02) !important;
        }

        /* 🔵 NEON SHINE AZUL (Setor XML) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #00D1FF !important;
            /* BLOOM EXPLOSIVO + SHINE BRANCO */
            box-shadow: 0 0 20px #00D1FF, 0 0 80px rgba(0, 209, 255, 0.4), inset 0 3px 15px rgba(255,255,255,0.9) !important;
        }

        /* 💗 NEON SHINE ROSA (Setor Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #FF69B4 !important;
            /* BLOOM EXPLOSIVO + SHINE BRANCO */
            box-shadow: 0 0 20px #FF69B4, 0 0 80px rgba(255, 105, 180, 0.4), inset 0 3px 15px rgba(255,255,255,0.9) !important;
        }

        /* --- 4. SUB-ABAS (MINI-SHINE) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F8F9FA !important;
            border-radius: 15px 40px 0 0 !important;
            font-size: 1.1rem !important;
            /* SHINE NAS FILHAS */
            box-shadow: inset 0 2px 4px rgba(255,255,255,0.5) !important;
        }

        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { 
            background: #00BFFF !important; 
            box-shadow: 0 0 15px #00D1FF, inset 0 2px 8px rgba(255,255,255,0.6) !important;
            color: white !important; 
        }
        
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { 
            background: #FF69B4 !important; 
            box-shadow: 0 0 15px #FF69B4, inset 0 2px 8px rgba(255,255,255,0.6) !important;
            color: white !important; 
        }

        </style>
    """, unsafe_allow_html=True)
