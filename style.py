import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. ESTRUTURA BASE --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            background-color: #E9ECEF !important; 
            border-right: 5px solid #FF69B4 !important;
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; 
        }

        /* --- 2. TÍTULO PRINCIPAL --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #495057 !important; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            padding: 20px 0 !important;
            background: transparent !important;
            text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important;
        }

        /* --- 3. ABAS MESTRE DIAMANTE (AZUL, ROSA, VERDE) --- */
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; 
            background: transparent !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 60px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.4rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
        }

        /* Lógica de cores para as 3 abas principais */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-30px); }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-30px); }
        .stTabs [data-baseweb="tab-list"] button:nth-child(3)[aria-selected="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-30px); }

        /* --- 4. O CAIXOTÃO (CONTEÚDO) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 40px !important;
            border-radius: 0 40px 40px 40px !important;
            border: 4px solid #DEE2E6 !important;
            min-height: 600px !important;
        }

        /* Efeito Neon Setorizado Reativo */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }

        /* --- 5. ENVELOPES DE UPLOAD (📄) --- */
        [data-testid="stFileUploader"] {
            padding: 40px !important;
            border-radius: 20px !important;
            margin-bottom: 20px !important;
            position: relative !important;
        }

        [data-testid="stFileUploader"]::before {
            content: "📄"; position: absolute; top: -25px; left: 50%; transform: translateX(-50%); font-size: 25px;
        }

        /* Cores dos Envelopes por Aba */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px solid #A7E9FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px solid #A9DFBF !important; }

        </style>
    """, unsafe_allow_html=True)
