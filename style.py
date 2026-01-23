import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA BASE (FUNDAÇÃO)
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. FORMATO PASTA RETRO (📂) - O CHARME DO APP
        ================================================================================= */
        
        /* AQUI CONSERTAMOS O CORTE NO TOPO */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px !important;
            padding-top: 25px !important; /* RESPIRO PARA O PULO NÃO CORTAR */
            padding-bottom: 0px !important;
        }

        /* O DESIGN DA PASTA MANILHA */
        .stTabs [data-baseweb="tab"] {
            height: 75px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #E9ECEF 100%) !important;
            /* O SEGREDO DO RETRO: Canto esquerdo arredondado, direito descendo suave */
            border-radius: 15px 60px 0 0 !important; 
            padding: 0px 40px !important;
            border: 1px solid #ADB5BD !important;
            border-bottom: none !important; /* Conecta com o papel */
            font-size: 1.4rem !important;
            font-weight: 700 !important;
            color: #6C757D !important;
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55) !important; /* Pulo elástico */
            margin-right: 2px !important;
        }

        /* BRILHO E MOVIMENTO */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-8px) !important; /* Pula mais alto */
            background: #FFFFFF !important;
            color: #212529 !important;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1) !important;
            z-index: 99 !important; /* Fica na frente das outras */
        }

        /* ABAS ATIVAS (MÃES) - Ficam firmes no topo */
        .stTabs > div > [data-baseweb="tab-list"] > button[aria-selected="true"] {
            transform: translateY(-10px) !important;
            background: #FFFFFF !important;
            color: #212529 !important;
            font-weight: 900 !important;
            border-top-width: 5px !important; /* Indicador de cor no topo */
            z-index: 100 !important;
        }

        /* =================================================================================
           3. MÓDULOS BLINDADOS (CORES E SEPARAÇÃO)
        ================================================================================= */

        /* 🟦 MÓDULO 1: ANÁLISE XML (AZUL) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            /* Detalhe na Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(1) { border-top-color: #00BFFF !important; color: #00BFFF !important; }
            
            /* Caixotão Azulado */
            > [data-testid="stTabPanel"] {
                border-top: 5px solid #00BFFF !important;
                background: linear-gradient(180deg, #F0F8FF 0%, #FFFFFF 50%) !important;
                box-shadow: 0 10px 40px rgba(0, 191, 255, 0.15) !important;
            }
            
            /* Filhas Azuis */
            [data-testid="stTabPanel"] button[aria-selected="true"] { color: #00BFFF !important; border-bottom: 3px solid #00BFFF !important; }
            
            /* Elementos Azuis */
            [data-testid="stFileUploader"] { border: 2px dashed #00BFFF !important; background-color: #F5FBFF !important; }
            div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; }
        }

        /* 🟥 MÓDULO 2: CONFORMIDADE (ROSA) - CASA DO RET */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            /* Detalhe na Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(2) { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
            
            /* Caixotão Rosado */
            > [data-testid="stTabPanel"] {
                border-top: 5px solid #FF69B4 !important;
                background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 50%) !important;
                box-shadow: 0 10px 40px rgba(255, 105, 180, 0.15) !important;
            }
            
            /* Filhas Rosas (RET incluso) */
            [data-testid="stTabPanel"] button[aria-selected="true"] { color: #FF69B4 !important; border-bottom: 3px solid #FF69B4 !important; }
            
            /* Elementos Rosas */
            [data-testid="stFileUploader"] { border: 2px dashed #FF69B4 !important; background-color: #FFF5F8 !important; }
            div.stDownloadButton > button:hover { background: #FF69B4 !important; color: white !important; }
        }

        /* 🟩 MÓDULO 3: APURAÇÃO (VERDE) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            /* Detalhe na Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(3) { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }
            
            /* Caixotão Esverdeado */
            > [data-testid="stTabPanel"] {
                border-top: 5px solid #2ECC71 !important;
                background: linear-gradient(180deg, #F0FFF4 0%, #FFFFFF 50%) !important;
                box-shadow: 0 10px 40px rgba(46, 204, 113, 0.15) !important;
            }
            
            /* Filhas Verdes */
            [data-testid="stTabPanel"] button[aria-selected="true"] { color: #2ECC71 !important; border-bottom: 3px solid #2ECC71 !important; }
            
            /* Elementos Verdes */
            [data-testid="stFileUploader"] { border: 2px dashed #2ECC71 !important; background-color: #F1FFF5 !important; }
            div.stDownloadButton > button:hover { background: #2ECC71 !important; color: white !important; }
        }

        /* =================================================================================
           4. ACABAMENTOS GERAIS
        ================================================================================= */
        
        /* O Caixotão Base (Papel) */
        [data-testid="stTabPanel"] {
            background: #FFFFFF;
            padding: 50px !important;
            border-radius: 0 30px 30px 30px !important;
            margin-top: -10px !important; /* Cola na aba */
            border: 1px solid #DEE2E6;
            min-height: 800px !important;
        }

        /* Sub-abas Inativas (Pastinhas menores) */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            border-radius: 10px 40px 0 0 !important; /* Curva mais suave nas filhas */
            padding: 0 30px !important;
            transform: none !important;
            background: #F8F9FA !important;
        }

        /* ENVELOPES (GLOBAL) */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 15px !important;
            border-top: 15px solid #FFFFFF !important;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -28px; left: 50%; transform: translateX(-50%); font-size: 32px; z-index: 99; }

        /* BOTÕES PRATEADOS (SEM VERMELHO) */
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

        </style>
    """, unsafe_allow_html=True)
