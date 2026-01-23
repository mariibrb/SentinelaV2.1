import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA BASE (RIHANNA EDITION)
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. ABAS DIAMANTE (TODAS PRATEADAS - FIM DA BRIGA DE CORES)
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 80px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 25px 25px 0 0 !important; 
            padding: 0px 50px !important;
            border: 1px solid #ADB5BD !important;
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: #6C757D !important;
            transition: all 0.3s ease !important;
        }
        
        /* Brilho no Hover */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            background: linear-gradient(0deg, #FFFFFF 0%, #E9ECEF 100%) !important;
            color: #212529 !important;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1) !important;
        }

        /* Abas Ativas (Mães e Filhas) - Visual "Clean" */
        .stTabs [aria-selected="true"] {
            background: #FFFFFF !important;
            color: #212529 !important;
            border-bottom: none !important;
            font-weight: 900 !important;
            transform: translateY(-5px) !important;
            box-shadow: 0 -5px 10px rgba(0,0,0,0.05) !important;
        }

        /* Mães (Topo) - Um pouco maiores */
        .stTabs > div > [data-baseweb="tab-list"] > button { height: 90px !important; font-size: 1.6rem !important; }

        /* =================================================================================
           3. A MÁGICA DO "AMBIENTE" (CHAMELEON PANEL)
           Aqui pintamos o FUNDO DA TELA (Painel) dependendo da aba mãe.
        ================================================================================= */

        /* --- MUNDO AZUL (ANÁLISE XML) --- */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            
            /* A Aba Mãe ganha um detalhe Azul */
            > div > [data-baseweb="tab-list"] > button:nth-child(1) { border-top: 6px solid #00BFFF !important; color: #00BFFF !important; }
            
            /* O PAINEL INTEIRO FICA AZULADO */
            > [data-testid="stTabPanel"] {
                background: linear-gradient(180deg, #F0F8FF 0%, #FFFFFF 100%) !important; /* Azul Bebê degradê */
                border: 2px solid #00BFFF !important;
                box-shadow: 0 0 50px rgba(0, 191, 255, 0.2) !important;
            }

            /* As filhas ativas ganham texto Azul */
            [data-testid="stTabPanel"] [aria-selected="true"] { color: #00BFFF !important; border-bottom: 3px solid #00BFFF !important; }
            
            /* Envelope Azul */
            [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 1px dashed #00BFFF !important; }
            div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; }
        }

        /* --- MUNDO ROSA (CONFORMIDADE) --- */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            
            /* A Aba Mãe ganha um detalhe Rosa */
            > div > [data-baseweb="tab-list"] > button:nth-child(2) { border-top: 6px solid #FF69B4 !important; color: #FF69B4 !important; }
            
            /* O PAINEL INTEIRO FICA ROSADO */
            > [data-testid="stTabPanel"] {
                background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%) !important; /* Rosa Bebê degradê */
                border: 2px solid #FF69B4 !important;
                box-shadow: 0 0 50px rgba(255, 105, 180, 0.2) !important;
            }

            /* As filhas ativas ganham texto Rosa (RET resolvido!) */
            [data-testid="stTabPanel"] [aria-selected="true"] { color: #FF69B4 !important; border-bottom: 3px solid #FF69B4 !important; }
            
            /* Envelope Rosa */
            [data-testid="stFileUploader"] { background-color: #FFF5F8 !important; border: 1px dashed #FF69B4 !important; }
            div.stDownloadButton > button:hover { background: #FF69B4 !important; color: white !important; }
        }

        /* --- MUNDO VERDE (APURAÇÃO) --- */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            
            /* A Aba Mãe ganha um detalhe Verde */
            > div > [data-baseweb="tab-list"] > button:nth-child(3) { border-top: 6px solid #2ECC71 !important; color: #2ECC71 !important; }
            
            /* O PAINEL INTEIRO FICA ESVERDEADO */
            > [data-testid="stTabPanel"] {
                background: linear-gradient(180deg, #F0FFF4 0%, #FFFFFF 100%) !important; /* Verde Menta degradê */
                border: 2px solid #2ECC71 !important;
                box-shadow: 0 0 50px rgba(46, 204, 113, 0.2) !important;
            }

            /* As filhas ativas ganham texto Verde */
            [data-testid="stTabPanel"] [aria-selected="true"] { color: #2ECC71 !important; border-bottom: 3px solid #2ECC71 !important; }
            
            /* Envelope Verde */
            [data-testid="stFileUploader"] { background-color: #F1FFF5 !important; border: 1px dashed #2ECC71 !important; }
            div.stDownloadButton > button:hover { background: #2ECC71 !important; color: white !important; }
        }

        /* =================================================================================
           4. ACABAMENTOS GERAIS
        ================================================================================= */
        /* O Caixotão Base */
        [data-testid="stTabPanel"] {
            background: #FFFFFF; /* Padrão */
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -10px !important;
            min-height: 800px !important;
        }

        /* Envelopes (Global) */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 15px !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA;
            transition: 0.3s;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-size: 30px; z-index: 99; }

        /* Botões Prateados (Matando o Vermelho) */
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
