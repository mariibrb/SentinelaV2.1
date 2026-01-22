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
            box-shadow: none !important;
            border: none !important;
        }

        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #495057 !important; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            padding: 20px 0 !important;
        }

        /* --- 3. ABAS MESTRE DIAMANTE --- */
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; 
            background: transparent !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            border: 2px solid #ADB5BD !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
        }

        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* --- 4. 📦 O CAIXOTÃO --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            border: 6px solid transparent !important;
        }

        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; }

        /* --- 5. 🎯 BOTÕES (Morte ao Vermelho) --- */
        div.stButton > button, 
        div.stDownloadButton > button, 
        button[kind="primary"] {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 15px !important;
            font-weight: 800 !important;
            height: 55px !important;
            width: 100% !important;
            text-transform: uppercase !important;
        }

        /* Hover reativo (Brilho sem mudar a cor) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div.stButton > button:hover,
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div.stDownloadButton > button:hover {
            box-shadow: 0 0 20px #00BFFF !important;
            border-color: #00BFFF !important;
        }

        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stButton > button:hover,
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stDownloadButton > button:hover {
            box-shadow: 0 0 20px #FF69B4 !important;
            border-color: #FF69B4 !important;
        }

        /* --- 9. ⛏️ ESTÉTICA DO GARIMPEIRO (METRICS) --- */
        [data-testid="stMetricValue"] {
            color: #495057 !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
        }

        [data-testid="stMetricLabel"] {
            color: #6C757D !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
        }

        div[data-testid="metric-container"] {
            background-color: #F8F9FA !important;
            border-radius: 15px !important;
            padding: 15px !important;
            border: 1px solid #DEE2E6 !important;
        }

        /* --- 6. UPLOADER --- */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
        }

        </style>
    """, unsafe_allow_html=True)
