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

        /* Ativas das Mães (1: Azul, 2: Rosa, 3: Verde) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; transform: translateY(-30px) !important; color: white !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; transform: translateY(-30px) !important; color: white !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(3)[aria-selected="true"] { background: #2ECC71 !important; transform: translateY(-30px) !important; color: white !important; }

        /* --- 4. O CAIXOTÃO (PASTA MÃE) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 40px !important;
            border-radius: 0 40px 40px 40px !important;
            margin-top: -5px !important;
            border: 6px solid transparent !important;
        }

        /* Neon Reativo por Setor */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }

        /* --- 5. SUB-ABAS (AQUI ESTÁ A CORREÇÃO DE HERANÇA) --- */
        
        /* Regra para as sub-abas dentro do SETOR ROSA (Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { 
            background-color: #FF69B4 !important; 
            color: white !important;
            transform: translateY(-10px) !important;
        }

        /* Regra para as sub-abas dentro do SETOR VERDE (Apuração) */
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) .stTabs [aria-selected="true"] { 
            background-color: #2ECC71 !important; 
            color: white !important;
            transform: translateY(-10px) !important;
        }

        /* --- 6. ENVELOPES DE UPLOAD (📄) --- */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            margin: 25px 0 !important;
            position: relative !important;
            border: 2px solid transparent !important;
        }

        [data-testid="stFileUploader"]::before {
            content: "📄"; position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-size: 30px;
        }

        /* Envelopes ROSAS (Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stFileUploader"] { 
            background-color: #FFF0F5 !important; border-color: #FFD1DC !important; 
        }

        /* Envelopes VERDES (Apuração) */
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stFileUploader"] { 
            background-color: #F1FFF7 !important; border-color: #A9DFBF !important; 
        }

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

        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) div.stDownloadButton > button:hover { box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
