import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. ESTRUTURA E FUNDO --- */
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

        /* --- 2. 💎 ABAS MESTRE (ESTILO DIAMANTE) --- */
        /* Importante: Removendo o corte das abas que sobem */
        .stTabs {
            overflow: visible !important;
        }
        
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; /* Mais espaço no topo para não cortar */
            align-items: flex-end;
            overflow: visible !important;
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
            box-shadow: inset 0 2px 5px rgba(255,255,255,0.8) !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        /* 🔵 ATIVA XML (BLUE SHINE) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #E0F7FF 0%, #00BFFF 100%) !important;
            border-color: #00D1FF !important;
            box-shadow: 0 -10px 40px rgba(0, 209, 255, 0.5), inset 0 5px 20px rgba(255,255,255,1) !important;
            color: white !important;
            transform: translateY(-30px) scale(1.05) !important; /* Sobe sem ser cortada */
            z-index: 100 !important;
        }

        /* 💗 ATIVA CONFORMIDADE (PINK SHINE) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFD1E8 0%, #FF69B4 100%) !important;
            border-color: #FF1493 !important;
            box-shadow: 0 -10px 40px rgba(255, 105, 180, 0.6), inset 0 5px 20px rgba(255,255,255,1) !important;
            color: white !important;
            transform: translateY(-30px) scale(1.05) !important; /* Sobe sem ser cortada */
            z-index: 100 !important;
        }

        /* --- 3. 📦 O CAIXOTÃO (PASTA COM NEON DE BOATE) --- */
        [data-testid="stTabPanel"] {
            background: white !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            min-height: 700px !important;
            overflow: visible !important; /* Garante que nada interno seja cortado */
        }

        /* NEON BOATE SOMBREADO */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #00D1FF !important;
            box-shadow: 0 0 25px #00D1FF, 0 0 60px rgba(0, 209, 255, 0.4), inset 0 0 15px rgba(255,255,255,1) !important;
        }

        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #FF69B4 !important;
            box-shadow: 0 0 25px #FF69B4, 0 0 60px rgba(255, 105, 180, 0.4), inset 0 0 15px rgba(255,255,255,1) !important;
        }

        /* --- 4. SUB-ABAS INTERNAS --- */
        .stTabs .stTabs [data-baseweb="tab-list"] {
            padding: 10px 0 30px 0 !important;
            margin-top: 10px !important;
            overflow: visible !important;
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F8F9FA !important;
            border-radius: 15px 45px 0 0 !important;
            margin-right: -10px !important;
            box-shadow: inset 0 2px 5px rgba(255,255,255,0.8) !important;
        }

        /* Sub-abas Ativas Diamond */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #00BFFF !important;
            box-shadow: 0 0 20px #00D1FF, inset 0 2px 10px rgba(255,255,255,0.8) !important;
            color: white !important;
            transform: translateY(-10px) !important;
        }

        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #FF69B4 !important;
            box-shadow: 0 0 20px #FF69B4, inset 0 2px 10px rgba(255,255,255,0.8) !important;
            color: white !important;
            transform: translateY(-10px) !important;
        }

        </style>
    """, unsafe_allow_html=True)
