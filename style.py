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

        /* --- 3. ABAS MESTRE DIAMANTE (MODELO RIHANNA) --- */
        .stTabs [data-baseweb="tab-list"] { gap: 15px !important; padding: 60px 0 0 20px !important; }
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 60px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.4rem !important;
            font-weight: 800 !important;
            transition: all 0.3s ease !important;
        }

        /* Elevação das Mães */
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] { transform: translateY(-30px) !important; color: white !important; }

        /* DNA das Mães (Cores Fixas) */
        .stTabs [data-baseweb="tab-list"] button:nth-of-type(1)[aria-selected="true"] { background: #00BFFF !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-of-type(2)[aria-selected="true"] { background: #FF69B4 !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-of-type(3)[aria-selected="true"] { background: #2ECC71 !important; }

        /* --- 4. O CAIXOTÃO --- */
        [data-testid="stTabPanel"] { background: #FFFFFF !important; padding: 40px !important; border-radius: 0 40px 40px 40px !important; border: 6px solid transparent !important; }

        /* Neon Setorizado */
        .stTabs:has(button:nth-of-type(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
        .stTabs:has(button:nth-of-type(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
        .stTabs:has(button:nth-of-type(3)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }

        /* --- 5. SUB-ABAS (HERANÇA GENÉTICA REAL) --- */
        .stTabs .stTabs [data-baseweb="tab"] { height: 60px !important; border-radius: 15px 45px 0 0 !important; background: #F1F3F5 !important; }
        
        /* Elevação das Filhas */
        .stTabs .stTabs button[aria-selected="true"] { transform: translateY(-12px) !important; color: white !important; }

        /* DNA AZUL: Herda da Mãe 1 */
        .stTabs:has(button:nth-of-type(1)[aria-selected="true"]) .stTabs button[aria-selected="true"] { background-color: #00BFFF !important; }

        /* DNA ROSA: Herda da Mãe 2 (TODAS as 5 subpastas ficam ROSAS) */
        .stTabs:has(button:nth-of-type(2)[aria-selected="true"]) .stTabs button[aria-selected="true"] { background-color: #FF69B4 !important; }

        /* DNA VERDE: Herda da Mãe 3 (TODAS as 5 subpastas ficam VERDES) */
        .stTabs:has(button:nth-of-type(3)[aria-selected="true"]) .stTabs button[aria-selected="true"] { background-color: #2ECC71 !important; }

        /* --- 6. ENVELOPES (MODELO MESTRE) --- */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            border-top: 18px solid #FDFDFD !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
            margin: 25px 0 !important;
            position: relative !important;
            border: 2px solid transparent !important;
        }

        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-size: 30px; z-index: 99; }

        /* Cor do DNA nos Envelopes */
        .stTabs:has(button:nth-of-type(1)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border-color: #A7E9FF !important; }
        .stTabs:has(button:nth-of-type(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border-color: #FFD1DC !important; }
        .stTabs:has(button:nth-of-type(3)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border-color: #A9DFBF !important; }

        </style>
    """, unsafe_allow_html=True)
