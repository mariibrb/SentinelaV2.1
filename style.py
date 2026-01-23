import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA E FUNDO (DO CÓDIGO DE ONTEM)
        ================================================================================= */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            background-color: #E9ECEF !important; 
            border-right: 5px solid #FF69B4 !important;
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; 
        }

        /* TÍTULO LIMPO */
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal),
        div[data-testid="stVerticalBlock"] > div:first-child,
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

        /* =================================================================================
           2. ABAS MESTRE DIAMANTE (VISUAL RIHANNA)
        ================================================================================= */
        .stTabs { overflow: visible !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; 
            overflow: visible !important;
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
            transition: 0.3s ease !important;
        }
        
        /* O BRILHO SHINE (HOVER) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-8px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* ATIVAS DAS MÃES (CORE) */
        /* Mãe 1: Azul */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; transform: translateY(-30px) !important; color: white !important; }
        /* Mãe 2: Rosa */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; transform: translateY(-30px) !important; color: white !important; }
        /* Mãe 3: Verde (NOVO) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(3)[aria-selected="true"] { background: #2ECC71 !important; transform: translateY(-30px) !important; color: white !important; }

        /* =================================================================================
           3. O CAIXOTÃO E NEON (PAINEL)
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            border: 6px solid transparent !important;
            min-height: 800px !important;
            overflow: visible !important;
        }

        /* Neon Azul */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF, 0 0 80px rgba(0, 209, 255, 0.4) !important; }
        /* Neon Rosa */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4, 0 0 80px rgba(255, 105, 180, 0.4) !important; }
        /* Neon Verde (NOVO) */
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71, 0 0 80px rgba(46, 204, 113, 0.4) !important; }

        /* =================================================================================
           4. SUB-ABAS SETORIZADAS (PASTAS)
        ================================================================================= */
        .stTabs .stTabs [data-baseweb="tab-list"] { padding: 0 0 30px 0 !important; }
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F1F3F5 !important;
            border-radius: 15px 45px 0 0 !important;
        }
        .stTabs .stTabs [aria-selected="true"] { transform: translateY(-12px) !important; color: white !important; }

        /* LÓGICA DE CORES (AQUI O RET FICA SEGURO) */
        /* Se a mãe é 1 -> Filho é Azul */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #00BFFF !important; }
        /* Se a mãe é 2 -> Filho é Rosa */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #FF69B4 !important; }
        /* Se a mãe é 3 -> Filho é Verde */
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) .stTabs [aria-selected="true"] { background: #2ECC71 !important; }

        /* =================================================================================
           5. ENVELOPES (ELES NÃO PODEM SUMIR)
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            border-top: 18px solid #FDFDFD !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA; /* Cor de segurança */
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-size: 30px; z-index: 99; }

        /* Cores dos Envelopes */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px solid #A7E9FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px solid #A9DFBF !important; }

        /* =================================================================================
           6. ÁREA DE AUDITORIA E BOTÕES (MATANDO O VERMELHO)
        ================================================================================= */
        div.stExpander, div.element-container:has(h1, h2, h3), .stDataFrame {
            background-color: white !important;
            padding: 30px !important;
            border-radius: 20px !important;
            box-shadow: 0 5px 25px rgba(0,0,0,0.03) !important;
            border: 1px solid #E9ECEF !important;
        }

        /* 🔴 O EXTERMINADOR DE BOTÕES VERMELHOS 🔴 */
        /* Aqui eu pego TANTO o botão de download QUANTO os botões normais (stButton) */
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 15px !important;
            font-weight: 800 !important;
            height: 55px !important;
            width: 100% !important;
            text-transform: uppercase !important;
            box-shadow: none !important;
            transition: 0.3s ease !important;
        }

        /* HOVER POR SETOR (NEON NO BOTÃO) */
        /* Azul */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div.stDownloadButton > button:hover,
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div.stButton > button:hover { 
            box-shadow: 0 0 20px #00BFFF !important; border-color: #00BFFF !important; 
        }
        /* Rosa */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stDownloadButton > button:hover,
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stButton > button:hover { 
            box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; 
        }
        /* Verde */
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) div.stDownloadButton > button:hover,
        .stTabs:has(button:nth-child(3)[aria-selected="true"]) div.stButton > button:hover { 
            box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; 
        }

        </style>
    """, unsafe_allow_html=True)
