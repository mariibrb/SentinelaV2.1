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

        /* --- 2. TÍTULO --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
        }

        /* --- 3. ABAS MESTRE (LIMPANDO O NEON) --- */
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
            box-shadow: 10px 0 20px rgba(0,0,0,0.1) !important;
            transition: all 0.3s ease !important;
        }

        /* Aba Ativa: Sem neon, apenas cor e elevação */
        .stTabs [aria-selected="true"] {
            transform: translateY(-20px) !important;
            color: white !important;
        }
        
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; }

        /* --- 4. 📦 PAINEL GERAL (GAVETA) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -20px !important;
            border: none !important; /* Sem neon aqui */
            box-shadow: 0 20px 80px rgba(0,0,0,0.05) !important;
        }

        /* --- 📂 O CAIXOTE GIGANTE COM BORDA NEON (AQUI MANDA O BRILHO) --- */
        div[data-testid="stHorizontalBlock"] {
            background: #FFFFFF !important;
            padding: 60px !important; /* Caixote grandão */
            border-radius: 50px !important;
            margin: 30px 0 !important;
            min-height: 400px !important;
            transition: all 0.4s ease !important;
        }

        /* 🔵 Borda Neon Azul no Caixote do XML */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 5px solid #00D1FF !important;
            box-shadow: 0 0 30px rgba(0, 209, 255, 0.5), 0 0 60px rgba(0, 209, 255, 0.2) !important;
        }

        /* 💗 Borda Neon Rosa no Caixote da Conformidade */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 5px solid #FF69B4 !important;
            box-shadow: 0 0 30px rgba(255, 105, 180, 0.5), 0 0 60px rgba(255, 105, 180, 0.2) !important;
        }

        /* --- 5. SUB-ABAS (LIMPANDO O NEON) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #FDFDFD !important;
            border-radius: 15px 45px 0 0 !important;
            font-size: 1.1rem !important;
            font-weight: 800 !important;
        }

        /* Sub-aba Ativa: Somente cor sólida */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        .stTabs .stTabs [aria-selected="true"] div { color: white !important; }

        /* Uploader limpo dentro do caixote neon */
        [data-testid="stFileUploader"] {
            background: #F8F9FA !important;
            border: 1px dashed #D8C7B1 !important;
            border-radius: 15px !important;
        }

        </style>
    """, unsafe_allow_html=True)
