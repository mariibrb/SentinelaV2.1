import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. ESTRUTURA --- */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }

        /* --- 2. TÍTULO --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important; color: #495057 !important; 
            font-size: 3.5rem; font-weight: 800; text-transform: uppercase;
            text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important;
        }

        /* --- 3. ABAS MESTRE (AS MÃES) --- */
        /* Aplicamos o estilo apenas no primeiro nível de abas */
        div[data-testid="stTabs"] > div > div[data-baseweb="tab-list"] {
            gap: 15px !important; padding: 60px 0 0 20px !important;
        }

        div[data-testid="stTabs"] > div > div[data-baseweb="tab-list"] button[data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 70px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            transition: all 0.3s ease !important;
        }

        /* Hover Metalizado nas Mães */
        div[data-testid="stTabs"] > div > div[data-baseweb="tab-list"] button[data-baseweb="tab"]:hover {
            background: linear-gradient(70deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.2s infinite linear !important;
            transform: translateY(-8px) !important;
        }

        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* Cores das Mães Selecionadas */
        div[data-testid="stTabs"] > div > div[data-baseweb="tab-list"] button:nth-of-type(1)[aria-selected="true"] { background: #00BFFF !important; transform: translateY(-30px) !important; color: white !important; }
        div[data-testid="stTabs"] > div > div[data-baseweb="tab-list"] button:nth-of-type(2)[aria-selected="true"] { background: #FF69B4 !important; transform: translateY(-30px) !important; color: white !important; }
        div[data-testid="stTabs"] > div > div[data-baseweb="tab-list"] button:nth-of-type(3)[aria-selected="true"] { background: #2ECC71 !important; transform: translateY(-30px) !important; color: white !important; }

        /* --- 4. SUB-ABAS (AS FILHAS - HERANÇA BLINDADA) --- */
        /* Selecionamos apenas as abas que estão DENTRO do painel de uma aba mãe */
        [data-testid="stTabPanel"] div[data-testid="stTabs"] button[data-baseweb="tab"] {
            height: 60px !important; background: #F1F3F5 !important; border-radius: 15px 45px 0 0 !important; padding: 0 30px !important;
        }

        /* 🛡️ LÓGICA DE HERANÇA POR BLOCO (A REGRA DE ONTEM) */
        /* Se a Mãe 2 (ROSA) está ativa, TODAS as sub-abas selecionadas dentro dela ficam ROSAS */
        div[data-testid="stTabs"]:has(button:nth-of-type(2)[aria-selected="true"]) [data-testid="stTabPanel"] button[aria-selected="true"] {
            background-color: #FF69B4 !important; transform: translateY(-12px) !important; color: white !important;
        }

        /* Se a Mãe 3 (VERDE) está ativa, TODAS as sub-abas selecionadas dentro dela ficam VERDES */
        div[data-testid="stTabs"]:has(button:nth-of-type(3)[aria-selected="true"]) [data-testid="stTabPanel"] button[aria-selected="true"] {
            background-color: #2ECC71 !important; transform: translateY(-12px) !important; color: white !important;
        }

        /* --- 5. ENVELOPES --- */
        [data-testid="stFileUploader"] { padding: 50px 45px 45px 45px !important; border-radius: 10px 10px 45px 45px !important; border-top: 18px solid #FDFDFD !important; position: relative !important; }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-size: 30px; z-index: 99; }
        
        div[data-testid="stTabs"]:has(button:nth-of-type(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }
        div[data-testid="stTabs"]:has(button:nth-of-type(3)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px solid #A9DFBF !important; }

        </style>
    """, unsafe_allow_html=True)
