import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. CONFIGURAÇÕES GERAIS --- */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }

        /* --- 2. ESTILO BASE DE TODAS AS ABAS (SEM COR AINDA) --- */
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%);
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 70px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
            transition: 0.3s ease !important;
        }

        /* BRILHO METALIZADO (HOVER) */
        .stTabs [data-baseweb="tab"]:hover {
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
            transform: translateY(-8px) !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* --- 3. A GRANDE MUDANÇA: PINTURA POR NÍVEL HIERÁRQUICO --- */
        
        /* === NÍVEL 1: AS MÃES (Top Level) === */
        /* Seleciona apenas as abas que NÃO estão dentro de um painel (ou seja, as do topo) */
        .main > .block-container > div > div > div > div > div[data-testid="stTabs"] > div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"] { 
            background: #00BFFF !important; transform: translateY(-30px) !important; color: white !important; 
        }
        .main > .block-container > div > div > div > div > div[data-testid="stTabs"] > div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"] { 
            background: #FF69B4 !important; transform: translateY(-30px) !important; color: white !important; 
        }
        .main > .block-container > div > div > div > div > div[data-testid="stTabs"] > div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"] { 
            background: #2ECC71 !important; transform: translateY(-30px) !important; color: white !important; 
        }

        /* === NÍVEL 2: AS FILHAS (Nested Level) === */
        /* Redefine o tamanho para as filhas (para não ficarem gigantes) */
        [data-testid="stTabPanel"] [data-testid="stTabs"] [data-baseweb="tab"] {
            height: 60px !important;
            background: #F1F3F5 !important;
            border-radius: 15px 45px 0 0 !important;
            padding: 0 30px !important;
        }

        /* 🟦 TERRITÓRIO AZUL (MÃE 1 ATIVA) */
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) 
        > [data-testid="stTabPanel"] 
        div[data-testid="stTabs"] button[aria-selected="true"] {
            background-color: #00BFFF !important;
            color: white !important;
            transform: translateY(-12px) !important;
        }

        /* 🟥 TERRITÓRIO ROSA (MÃE 2 ATIVA) - AQUI O RET É OBRIGADO A SER ROSA */
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) 
        > [data-testid="stTabPanel"] 
        div[data-testid="stTabs"] button[aria-selected="true"] {
            background-color: #FF69B4 !important;
            color: white !important;
            transform: translateY(-12px) !important;
        }

        /* 🟩 TERRITÓRIO VERDE (MÃE 3 ATIVA) */
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) 
        > [data-testid="stTabPanel"] 
        div[data-testid="stTabs"] button[aria-selected="true"] {
            background-color: #2ECC71 !important;
            color: white !important;
            transform: translateY(-12px) !important;
        }

        /* --- 4. CAIXOTÃO E ENVELOPES --- */
        [data-testid="stTabPanel"] { background: white !important; padding: 50px !important; border-radius: 0 60px 60px 60px !important; border: 6px solid transparent !important; }

        /* Neon do Caixotão */
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) > [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) > [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) > [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }

        /* Envelopes */
        [data-testid="stFileUploader"] { padding: 50px 45px 45px 45px !important; border-radius: 10px 10px 45px 45px !important; border-top: 18px solid #FDFDFD !important; position: relative !important; }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-size: 30px; z-index: 99; }
        
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px solid #A7E9FF !important; }
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px solid #A9DFBF !important; }

        /* --- 5. BOTÃO DE DOWNLOAD --- */
        div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important; color: #495057 !important; border: 2px solid #ADB5BD !important; border-radius: 15px !important; font-weight: 800 !important; height: 55px !important; width: 100% !important; text-transform: uppercase !important;
        }
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #00BFFF !important; border-color: #00BFFF !important; }
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; }
        div[data-testid="stTabs"]:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
