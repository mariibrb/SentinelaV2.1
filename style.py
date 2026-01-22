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
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }

        /* --- 2. ABAS MESTRE (ETIQUETAS) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] { gap: 20px !important; padding: 40px 0 0 0 !important; }

        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 30px 90px 0 0 !important; 
            margin-right: -25px !important;
            padding: 0px 65px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
        }

        /* --- 3. 📦 O CAIXOTÃO BRANCO (PASTA ABERTA) --- */
        [data-testid="stTabPanel"] {
            background: white !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            min-height: 700px !important;
            border: 6px solid transparent !important;
        }

        /* 🔵 NEON LETREIRO DE BOATE AZUL (Setor XML) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #00D1FF !important;
            /* Efeito Letreiro Boate: 4 camadas de brilho que explodem para fora */
            box-shadow: 
                0 0 10px #00D1FF, 
                0 0 40px #00D1FF, 
                0 0 90px rgba(0, 209, 255, 0.7), 
                0 0 150px rgba(0, 209, 255, 0.3) !important;
        }

        /* 💗 NEON LETREIRO DE BOATE ROSA (Setor Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #FF69B4 !important;
            /* Efeito Letreiro Boate: 4 camadas de brilho que explodem para fora */
            box-shadow: 
                0 0 10px #FF69B4, 
                0 0 40px #FF69B4, 
                0 0 90px rgba(255, 105, 180, 0.7), 
                0 0 150px rgba(255, 105, 180, 0.3) !important;
        }

        /* --- 4. SUB-ABAS INTERNAS (MORANDO NO CAIXOTÃO) --- */
        .stTabs .stTabs [data-baseweb="tab-list"] { padding: 10px 0 30px 0 !important; }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F8F9FA !important;
            border-radius: 15px 45px 0 0 !important;
            font-size: 1.1rem !important;
            border: 1px solid #E8DCCB !important;
        }

        /* Ativas Sólidas */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* --- 5. UPLOADER --- */
        [data-testid="stFileUploader"] {
            background: #FDFDFD !important;
            border: 2px dashed #D8C7B1 !important;
            border-radius: 20px !important;
        }

        </style>
    """, unsafe_allow_html=True)
