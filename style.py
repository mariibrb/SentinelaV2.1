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

        /* --- 3. ABAS MÃE (SETORIZAÇÃO) --- */
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

        /* 🔵 SETOR ANALISE XML: AZUL NEON SHINE */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            border-color: #00D1FF !important;
            box-shadow: 0 0 20px #00D1FF, 0 0 50px rgba(0, 209, 255, 0.6), inset 0 5px 15px rgba(255,255,255,0.8) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            z-index: 100 !important;
        }

        /* 💗 SETOR CONFORMIDADE: ROSA NEON SHINE */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            border-color: #FF1493 !important;
            box-shadow: 0 0 20px #FF1493, 0 0 50px rgba(255, 105, 180, 0.7), inset 0 5px 15px rgba(255,255,255,0.8) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            z-index: 100 !important;
        }

        /* --- 4. 📦 OS CAIXOTES BRANCOS (GAVETAS COM BRILHO) --- */
        
        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.85) !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -20px !important;
            box-shadow: inset 0 20px 40px rgba(0,0,0,0.05) !important;
            border: 4px solid transparent !important;
        }

        /* Caixote do Setor XML (Borda Azul Glow) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 4px solid #00D1FF !important;
            border-top: 8px solid #00BFFF !important;
            box-shadow: 0 15px 60px rgba(0, 209, 255, 0.3) !important;
        }

        /* Caixote do Setor Conformidade (Borda Rosa Glow) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 4px solid #FFB6C1 !important;
            border-top: 8px solid #FF69B4 !important;
            box-shadow: 0 15px 60px rgba(255, 105, 180, 0.3) !important;
        }

        /* --- 5. SUB-ABAS (SETORIZADAS) --- */
        
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 65px !important;
            background: #FDFDFD !important;
            border-radius: 20px 55px 0 0 !important;
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            margin-right: -10px !important;
        }

        /* Sub-abas do XML (Azul) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            border: 2px solid #00D1FF !important;
            box-shadow: 0 0 25px #00D1FF, inset 0 2px 5px rgba(255,255,255,0.5) !important;
            transform: translateY(-12px) !important;
        }

        /* Sub-abas da Conformidade (Rosa) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            border: 2px solid #FF1493 !important;
            box-shadow: 0 0 25px #FF69B4, inset 0 2px 5px rgba(255,255,255,0.5) !important;
            transform: translateY(-12px) !important;
        }

        .stTabs .stTabs [aria-selected="true"] div { color: white !important; }

        </style>
    """, unsafe_allow_html=True)
