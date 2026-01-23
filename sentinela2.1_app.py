import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* 1. ESTRUTURA GERAL */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* 2. DESIGN DAS ABAS */
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 70px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
            transition: 0.3s ease !important;
        }
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-8px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* Mães Ativas (Design Base) */
        .stTabs > div > [data-baseweb="tab-list"] > button[aria-selected="true"] {
            transform: translateY(-30px) !important; color: white !important;
        }

        /* 3. LÓGICA DAS BANDEIRAS (INFALÍVEL) */
        /* O CSS agora procura o ID que colocamos no Python */

        /* --- 🔵 BANDEIRA AZUL (XML) --- */
        .stTabs:has(#marcador-azul) {
            /* Pinta a Mãe */
            > div > [data-baseweb="tab-list"] > button[aria-selected="true"] { background: #00BFFF !important; }
            /* Pinta TODAS as sub-abas */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #00BFFF !important; color: white !important; }
            /* Acabamentos */
            [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
            [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px solid #A7E9FF !important; }
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #00BFFF !important; border-color: #00BFFF !important; }
        }

        /* --- 🩷 BANDEIRA ROSA (CONFORMIDADE) --- */
        .stTabs:has(#marcador-rosa) {
            /* Pinta a Mãe */
            > div > [data-baseweb="tab-list"] > button[aria-selected="true"] { background: #FF69B4 !important; }
            /* Pinta TODAS as sub-abas (Incluindo RET) */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #FF69B4 !important; color: white !important; }
            /* Acabamentos */
            [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
            [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; }
        }

        /* --- 🟢 BANDEIRA VERDE (APURAÇÃO) --- */
        .stTabs:has(#marcador-verde) {
            /* Pinta a Mãe */
            > div > [data-baseweb="tab-list"] > button[aria-selected="true"] { background: #2ECC71 !important; }
            /* Pinta TODAS as sub-abas */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #2ECC71 !important; color: white !important; }
            /* Acabamentos */
            [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }
            [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px solid #A9DFBF !important; }
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; }
        }

        /* 4. RESET E COMPONENTES */
        [data-testid="stTabPanel"] { background: white !important; padding: 50px !important; border-radius: 0 60px 60px 60px !important; border: 6px solid transparent !important; }
        /* Reset Sub-abas */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] { height: 60px !important; background: #F1F3F5 !important; border-radius: 15px 45px 0 0 !important; }
        
        [data-testid="stFileUploader"] { padding: 50px 45px 45px 45px !important; border-radius: 10px 10px 45px 45px !important; margin: 25px 0 !important; position: relative !important; }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-size: 30px; z-index: 99; }
        div.stDownloadButton > button { background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important; color: #495057 !important; border: 2px solid #ADB5BD !important; border-radius: 15px !important; font-weight: 800 !important; height: 55px !important; width: 100% !important; text-transform: uppercase !important; }
        
        </style>
    """, unsafe_allow_html=True)
