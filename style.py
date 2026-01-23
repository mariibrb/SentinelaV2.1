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
            padding: 0px 60px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.4rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
        }

        /* Ativas das Mães */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-30px); }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-30px); }
        .stTabs [data-baseweb="tab-list"] button:nth-child(3)[aria-selected="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-30px); }

        /* --- 4. O CAIXOTÃO (PASTA MÃE) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 40px !important;
            border-radius: 0 40px 40px 40px !important;
            margin-top: -5px !important;
            border: 6px solid transparent !important;
            min-height: 800px !important;
        }

        /* Neon Reativo por Bloco */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }

        /* --- 5. SUB-ABAS (HERDANDO A COR DA MÃE) --- */
        .stTabs .stTabs [aria-selected="true"] { transform: translateY(-12px) !important; color: white !important; }
        
        /* Se a Mãe 1 estiver ativa, as filhas são Azuis */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #00BFFF !important; }
        /* Se a Mãe 2 estiver ativa, as filhas são ROSAS (Incluindo o RET aqui) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #FF69B4 !important; }
        /* Se a Mãe 3 estiver ativa, as filhas são Verdes */
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #2ECC71 !important; }

        /* --- 6. ENVELOPES DE UPLOAD (📄) --- */
        [data-testid="stFileUploader"] {
            padding: 40px !important;
            border-radius: 20px !important;
            margin-bottom: 20px !important;
            position: relative !important;
            border: 2px solid transparent !important;
        }

        [data-testid="stFileUploader"]::before {
            content: "📄"; position: absolute; top: -25px; left: 50%; transform: translateX(-50%); font-size: 25px;
        }

        /* Cores dos Envelopes acompanhando o Bloco Mãe */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border-color: #A7E9FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border-color: #FFD1DC !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border-color: #A9DFBF !important; }

        /* --- 7. BOTÕES DE DOWNLOAD --- */
        div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 15px !important;
            font-weight: 800 !important;
            height: 55px !important;
            text-transform: uppercase !important;
        }

        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #00BFFF !important; border-color: #00BFFF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
