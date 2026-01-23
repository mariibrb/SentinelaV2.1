import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA E BASE (GLOBAL)
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. ESTILO "DIAMANTE" (PADRÃO PARA TODAS AS ABAS)
        ================================================================================= */
        /* Aqui definimos a forma e a cor base (Prata) para que fiquem lindas por padrão */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #E9ECEF 100%) !important;
            border-radius: 20px 20px 0 0 !important; 
            padding: 0px 40px !important;
            border: 1px solid #CED4DA !important;
            border-bottom: none !important;
            font-size: 1.4rem !important;
            font-weight: 700 !important;
            color: #6C757D !important; /* Cinza quando inativo */
            transition: all 0.3s ease !important;
        }

        /* Hover Metalizado */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            color: #212529 !important;
            background: linear-gradient(0deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1) !important;
        }

        /* MÃES ATIVAS (Destaque Maior) */
        .stTabs > div > [data-baseweb="tab-list"] > button[aria-selected="true"] {
            height: 85px !important; /* Fica maior que as outras */
            background: #FFFFFF !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            box-shadow: 0 -10px 20px rgba(0,0,0,0.05) !important;
            border-top: 5px solid !important; /* A cor da borda virá nas regras abaixo */
        }

        /* FILHAS ATIVAS (Destaque Menor) */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: #FFFFFF !important;
            color: #212529 !important;
            border-bottom: 4px solid !important; /* Sublinhado colorido */
        }

        /* =================================================================================
           3. LÓGICA DE CORES "NEON" (BLINDADA)
           O seletor :not([data-testid="stTabPanel"] .stTabs) garante que só olhamos para as Mães
        ================================================================================= */

        /* 🟦 MUNDO AZUL (Se a Mãe 1 estiver ativa) */
        /* O seletor abaixo diz: "Encontre a TAB MÃE onde o botão 1 está ativo" */
        .stTabs:not([data-testid="stTabPanel"] .stTabs):has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            
            /* Pinta o Topo da Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(1) { border-top-color: #00BFFF !important; color: #00BFFF !important; }
            
            /* Pinta o Texto e Sublinhado de QUALQUER filha */
            [data-testid="stTabPanel"] [data-baseweb="tab"][aria-selected="true"] { color: #00BFFF !important; border-bottom-color: #00BFFF !important; }
            
            /* Pinta o Painel e Envelopes */
            > [data-testid="stTabPanel"] { border-top: 5px solid #00BFFF !important; box-shadow: 0 0 30px rgba(0, 191, 255, 0.15) !important; }
            [data-testid="stFileUploader"] { background-color: #F0F8FF !important; border: 1px dashed #00BFFF !important; }
            div.stDownloadButton > button { border-color: #00BFFF !important; color: #00BFFF !important; }
            div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; }
        }

        /* 🟥 MUNDO ROSA (Se a Mãe 2 estiver ativa) */
        .stTabs:not([data-testid="stTabPanel"] .stTabs):has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            
            /* Pinta o Topo da Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(2) { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
            
            /* Pinta o Texto e Sublinhado de QUALQUER filha (Incluindo RET) */
            [data-testid="stTabPanel"] [data-baseweb="tab"][aria-selected="true"] { color: #FF69B4 !important; border-bottom-color: #FF69B4 !important; }
            
            /* Pinta o Painel e Envelopes */
            > [data-testid="stTabPanel"] { border-top: 5px solid #FF69B4 !important; box-shadow: 0 0 30px rgba(255, 105, 180, 0.15) !important; }
            [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 1px dashed #FF69B4 !important; }
            div.stDownloadButton > button { border-color: #FF69B4 !important; color: #FF69B4 !important; }
            div.stDownloadButton > button:hover { background: #FF69B4 !important; color: white !important; }
        }

        /* 🟩 MUNDO VERDE (Se a Mãe 3 estiver ativa) */
        /* Graças ao ":not", essa regra NUNCA vai ser ativada por uma sub-aba 3 (como o RET) */
        .stTabs:not([data-testid="stTabPanel"] .stTabs):has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            
            /* Pinta o Topo da Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(3) { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }
            
            /* Pinta o Texto e Sublinhado de QUALQUER filha */
            [data-testid="stTabPanel"] [data-baseweb="tab"][aria-selected="true"] { color: #2ECC71 !important; border-bottom-color: #2ECC71 !important; }
            
            /* Pinta o Painel e Envelopes */
            > [data-testid="stTabPanel"] { border-top: 5px solid #2ECC71 !important; box-shadow: 0 0 30px rgba(46, 204, 113, 0.15) !important; }
            [data-testid="stFileUploader"] { background-color: #F0FFF4 !important; border: 1px dashed #2ECC71 !important; }
            div.stDownloadButton > button { border-color: #2ECC71 !important; color: #2ECC71 !important; }
            div.stDownloadButton > button:hover { background: #2ECC71 !important; color: white !important; }
        }

        /* =================================================================================
           4. ACABAMENTOS GERAIS
        ================================================================================= */
        /* O Caixotão */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 40px !important;
            border-radius: 0 30px 30px 30px !important;
            margin-top: -10px !important;
            border: 1px solid #DEE2E6; /* Borda padrão se não houver cor ativa */
        }
        
        /* Envelopes (Definição Global) - GARANTIA QUE NÃO SOMEM */
        [data-testid="stFileUploader"] {
            padding: 40px 20px 20px 20px !important;
            border-radius: 15px !important;
            margin: 20px 0 !important;
            position: relative !important;
            transition: all 0.3s ease !important;
        }
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute; top: -25px; left: 50%; transform: translateX(-50%); font-size: 28px; z-index: 99;
        }
        
        /* Botão Padrão */
        div.stDownloadButton > button {
            background: white !important;
            border-radius: 10px !important;
            font-weight: 800 !important;
            height: 50px !important;
            width: 100% !important;
            text-transform: uppercase !important;
            transition: 0.3s ease !important;
        }

        </style>
    """, unsafe_allow_html=True)
