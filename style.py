import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. ESTRUTURA E FUNDO --- */
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
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal),
        .element-container:has(.titulo-principal) {
            background-color: transparent !important;
            background: transparent !important;
            box-shadow: none !important;
            border: none !important;
        }

        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #495057 !important; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            background: transparent !important;
            padding: 20px 0 !important;
            text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important;
        }

        /* --- 3. ABAS MESTRE --- */
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; 
            background: transparent !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 70px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
        }

        /* Cores Ativas das Abas Mãe */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* --- 4. PAINEL DAS ABAS (O CAIXOTÃO) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            border: 6px solid transparent !important;
            min-height: 800px !important;
        }

        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }

        /* --- 5. BOTÕES ESTILIZADOS --- */
        div.stButton > button {
            width: 100% !important;
            border-radius: 15px !important;
            height: 60px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            transition: all 0.3s ease !important;
            border: 2px solid #ADB5BD !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
        }

        /* Hover dos Botões baseado na aba ativa */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div.stButton > button:hover {
            background: #00BFFF !important;
            color: white !important;
            box-shadow: 0 0 20px rgba(0, 191, 255, 0.6) !important;
            border-color: transparent !important;
        }

        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stButton > button:hover {
            background: #FF69B4 !important;
            color: white !important;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.6) !important;
            border-color: transparent !important;
        }

        /* Botões de Download (st.download_button) */
        div.stDownloadButton > button {
            background: #495057 !important;
            color: white !important;
            border: none !important;
            height: 50px !important;
        }

        /* --- 6. UPLOADER (ENVELOPE) --- */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            border-top: 18px solid #FDFDFD !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
        }

        </style>
    """, unsafe_allow_html=True)
