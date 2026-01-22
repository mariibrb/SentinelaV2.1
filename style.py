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

        /* --- 2. ABAS MESTRE --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px !important;
            padding: 40px 0 !important;
            align-items: flex-end;
        }

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
        }

        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* --- 3. 📦 O CAIXOTÃO BRANCO (COM NEON TURBINADO) --- */
        [data-testid="stTabPanel"] {
            background: white !important;
            padding: 40px !important;
            border-radius: 40px !important;
            margin-top: -5px !important;
            min-height: 600px !important;
            border: 6px solid transparent !important;
        }

        /* 🔵 NEON AZUL EXPLOSIVO (Setor XML) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #00D1FF !important;
            /* Aumentei de 30px para 80px de brilho */
            box-shadow: 0 0 20px #00D1FF, 0 0 80px rgba(0, 209, 255, 0.6), 0 10px 100px rgba(0, 0, 0, 0.1) !important;
        }

        /* 💗 NEON ROSA EXPLOSIVO (Setor Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #FF69B4 !important;
            /* Aumentei de 30px para 80px de brilho */
            box-shadow: 0 0 20px #FF69B4, 0 0 80px rgba(255, 105, 180, 0.6), 0 10px 100px rgba(0, 0, 0, 0.1) !important;
        }

        /* --- 4. SUB-ABAS INTERNAS --- */
        .stTabs .stTabs [data-baseweb="tab-list"] {
            padding: 10px 0 30px 0 !important;
            background: transparent !important;
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F8F9FA !important;
            border-radius: 15px 40px 0 0 !important;
            font-size: 1.1rem !important;
            padding: 0 40px !important;
        }

        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* --- 5. AREA DE UPLOAD --- */
        [data-testid="stFileUploader"] {
            background: #FFFFFF !important;
            border: 2px dashed #D8C7B1 !important;
            border-radius: 20px !important;
            padding: 20px !important;
        }
        </style>
    """, unsafe_allow_html=True)
