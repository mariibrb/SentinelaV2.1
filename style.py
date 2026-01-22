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

        /* --- 2. TÍTULO SENTINELA --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }

        /* --- 3. ABAS MESTRE (PASTAS METALIZADAS) --- */
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

        /* 🔵 SETOR XML: AZUL METALIZADO */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-20px) scale(1.05) !important;
            border-color: #00D1FF !important;
            z-index: 100 !important;
        }

        /* 💗 SETOR CONFORMIDADE: ROSA METALIZADO */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-20px) scale(1.05) !important;
            border-color: #FF1493 !important;
            z-index: 100 !important;
        }

        /* --- 4. 📦 O CAIXOTÃO BRANCO GIGANTE (MOLDURA INTERNA) --- */
        /* Esta regra cria a caixa branca grande em volta de toda a área de upload */
        div[data-testid="stHorizontalBlock"] {
            background: #FFFFFF !important;
            padding: 55px !important; /* Caixote grandão */
            border-radius: 55px !important;
            margin: 40px 0 !important;
            min-height: 450px !important; /* Força a caixa a ser imponente */
            transition: all 0.4s ease !important;
        }

        /* Borda Neon Azul Shine no Caixote do XML */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 4px solid #00D1FF !important;
            box-shadow: 0 0 25px rgba(0, 209, 255, 0.2), 0 10px 40px rgba(0, 0, 0, 0.05) !important;
        }

        /* Borda Neon Rosa Shine no Caixote da Conformidade */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div[data-testid="stHorizontalBlock"] {
            border: 4px solid #FFB6C1 !important;
            box-shadow: 0 0 25px rgba(255, 182, 193, 0.3), 0 10px 40px rgba(0, 0, 0, 0.05) !important;
        }

        [data-testid="stFileUploader"] {
            background: #F8F9FA !important;
            border: 1px dashed #D8C7B1 !important;
            border-radius: 15px !important;
            padding: 10px !important;
        }

        /* --- 5. SUB-ABAS (ALINHADAS POR SETOR) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 65px !important;
            background: #FDFDFD !important;
            border-radius: 20px 55px 0 0 !important;
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            margin-right: -10px !important;
        }

        /* Sub-abas Ativa Azul (Setor XML) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            border: 2px solid #00D1FF !important;
            transform: translateY(-12px) !important;
        }

        /* Sub-abas Ativa Rosa (Setor Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            border: 2px solid #FF1493 !important;
            transform: translateY(-12px) !important;
        }

        .stTabs .stTabs [aria-selected="true"] div { color: white !important; }

        </style>
    """, unsafe_allow_html=True)
