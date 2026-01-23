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

        /* --- 2. 🚫 TÍTULO LIMPO --- */
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

        /* --- 3. ABAS MESTRE DIAMANTE (MODELO RIHANNA) --- */
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
            transition: all 0.3s ease !important;
            position: relative !important;
            overflow: hidden !important;
        }

        /* ✨ O BRILHO METALIZADO DIAMANTE (HOVER) ✨ */
        .stTabs [data-baseweb="tab"]:hover {
            background: linear-gradient(
                70deg, 
                rgba(255,255,255,0) 30%, 
                rgba(255,255,255,0.8) 50%, 
                rgba(255,255,255,0) 70%
            ), linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.2s infinite linear !important;
            transform: translateY(-8px) scale(1.02) !important;
            box-shadow: 0 15px 30px rgba(0,0,0,0.15) !important;
            color: #000000 !important;
            border-color: #FFFFFF !important;
        }

        @keyframes brilhoMetalico {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }

        /* Elevação das Mães Selecionadas */
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] { 
            transform: translateY(-30px) !important; 
            color: white !important; 
        }

        /* DNA das Mães - CORES FIXAS */
        .stTabs [data-baseweb="tab-list"] button:nth-of-type(1)[aria-selected="true"] { background: #00BFFF !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-of-type(2)[aria-selected="true"] { background: #FF69B4 !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-of-type(3)[aria-selected="true"] { background: #2ECC71 !important; }

        /* --- 4. 📦 O CAIXOTÃO (PASTA MÃE) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            border: 6px solid transparent !important;
            min-height: 800px !important;
            overflow: visible !important;
        }

        /* Neon Setorizado Reativo ao DNA */
        .stTabs:has(button:nth-of-type(1)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
        .stTabs:has(button:nth-of-type(2)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
        .stTabs:has(button:nth-of-type(3)[aria-selected="true"]) [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }

        /* --- 5. SUB-ABAS (A LÓGICA DE ONTEM QUE FUNCIONA) --- */
        .stTabs .stTabs [data-baseweb="tab-list"] { padding: 0 0 30px 0 !important; }
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F1F3F5 !important;
            border-radius: 15px 45px 0 0 !important;
        }

        .stTabs .stTabs button[aria-selected="true"] { transform: translateY(-12px) !important; color: white !important; }
        
        /* HERANÇA POR BLOCO MÃE (DNA PURO) */
        /* Se a Mãe 1 estiver ativa -> Filha Azul */
        .stTabs:has(button:nth-of-type(1)[aria-selected="true"]) .stTabs [aria-selected="true"] { background-color: #00BFFF !important; }
        
        /* Se a Mãe 2 estiver ativa -> Filha Rosa (TUDO, inclusive o RET) */
        .stTabs:has(button:nth-of-type(2)[aria-selected="true"]) .stTabs [aria-selected="true"] { background-color: #FF69B4 !important; }
        
        /* Se a Mãe 3 estiver ativa -> Filha Verde */
        .stTabs:has(button:nth-of-type(3)[aria-selected="true"]) .stTabs [aria-selected="true"] { background-color: #2ECC71 !important; }

        /* --- 6. ✉️ ENVELOPE COM ÍCONE 📄 --- */
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

        /* Cor dos Envelopes acompanhando o PAI */
        .stTabs:has(button:nth-of-type(1)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border-color: #A7E9FF !important; }
        .stTabs:has(button:nth-of-type(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border-color: #FFD1DC !important; }
        .stTabs:has(button:nth-of-type(3)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border-color: #A9DFBF !important; }

        </style>
    """, unsafe_allow_html=True)
