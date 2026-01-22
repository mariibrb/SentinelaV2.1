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
            text-shadow: 0 0 10px rgba(93, 58, 26, 0.1);
        }

        /* --- 3. ABAS MESTRE (METALIZADAS E LIMPAS) --- */
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
            box-shadow: 10px 0 20px rgba(0,0,0,0.1), inset 0 2px 5px rgba(255,255,255,0.8) !important;
            transition: all 0.3s ease !important;
        }

        /* ABA ATIVA (SEM NEON EXTERNO, APENAS ELEVAÇÃO) */
        .stTabs [aria-selected="true"] {
            transform: translateY(-20px) scale(1.05) !important;
            z-index: 100 !important;
            border-bottom: 5px solid white !important;
        }

        /* --- 4. 📦 O CAIXOTÃO BRANCO GIGANTE (A ÁREA DE FOCO) --- */
        
        div[data-testid="stHorizontalBlock"] {
            background: #FFFFFF !important;
            padding: 60px !important; /* CAIXOTE GRANDÃO */
            border-radius: 50px !important;
            margin: 40px 0 !important;
            min-height: 500px !important; /* FORÇA O CAIXOTE A SER GIGANTE */
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* 🔵 BORDA NEON AZUL (SETOR XML) NO CAIXOTE */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 5px solid #00D1FF !important;
            box-shadow: 0 0 30px #00D1FF, 0 0 60px rgba(0, 209, 255, 0.2) !important;
        }

        /* 💗 BORDA NEON ROSA (SETOR CONFORMIDADE) NO CAIXOTE */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 5px solid #FF69B4 !important;
            box-shadow: 0 0 30px #FF69B4, 0 0 60px rgba(255, 105, 180, 0.2) !important;
        }

        /* --- 5. PAINEL DE FUNDO (GAVETA GERAL) --- */
        [data-testid="stTabPanel"] {
            background: transparent !important; /* Fundo transparente para o caixote brilhar sozinho */
            padding: 20px !important;
        }

        /* --- 6. SUB-ABAS (SETORIZADAS) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            border-radius: 15px 45px 0 0 !important;
            font-size: 1.1rem !important;
            font-weight: 800 !important;
        }

        /* Ativas das sub-abas sem o neon das mães */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #00BFFF !important;
            color: white !important;
        }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #FF69B4 !important;
            color: white !important;
        }

        </style>
    """, unsafe_allow_html=True)
