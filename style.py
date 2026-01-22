import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. FUNDO E SIDEBAR --- */
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

        /* --- 2. ABAS MESTRE (EFEITO DIAMANTE) --- */
        .stTabs { overflow: visible !important; }
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; 
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
        }

        /* Ativas Mães */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { 
            background: #00BFFF !important; color: white !important; transform: translateY(-30px) !important;
        }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { 
            background: #FF69B4 !important; color: white !important; transform: translateY(-30px) !important;
        }

        /* --- 3. 📦 O CAIXOTÃO PRINCIPAL (PASTA) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            min-height: 700px !important;
            overflow: visible !important;
            border: 6px solid transparent !important;
        }

        /* Neon Boate Sombreado */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border-color: #00D1FF !important;
            box-shadow: 0 0 30px #00D1FF, 0 0 80px rgba(0, 209, 255, 0.4) !important;
        }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border-color: #FF69B4 !important;
            box-shadow: 0 0 30px #FF69B4, 0 0 80px rgba(255, 105, 180, 0.4) !important;
        }

        /* --- 4. 📄 ÁREA DE AUDITORIA (ILHA BRANCA EM DESTAQUE) --- */
        /* Esta regra cria o fundo branco que voce pediu para a parte de auditoria */
        div.stExpander, div.element-container:has(h1, h2, h3), .stDataFrame {
            background-color: white !important;
            padding: 30px !important;
            border-radius: 30px !important;
            border: 1px solid #E8DCCB !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
            margin-top: 20px !important;
        }

        /* --- 5. SUB-ABAS INTERNAS --- */
        .stTabs .stTabs [data-baseweb="tab-list"] {
            padding: 10px 0 30px 0 !important;
            overflow: visible !important;
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F8F9FA !important;
            border-radius: 15px 45px 0 0 !important;
        }

        /* Sub-abas Ativas */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        </style>
    """, unsafe_allow_html=True)
