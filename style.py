import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 4px solid #FF69B4 !important;
            z-index: 999999 !important;
            box-shadow: 10px 0 30px rgba(0,0,0,0.1) !important;
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE PROFISSIONAL */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }
        
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER: SENTINELA 2.1 --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            margin-bottom: 5px;
            letter-spacing: -1.5px;
            text-transform: uppercase;
            line-height: 1;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }

        /* --- ABAS MESTRE (ESTILO CAPA DE FICHÁRIO METALIZADA) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important;
            background-color: transparent !important;
            padding: 20px 0 !important;
            align-items: flex-end;
        }

        /* Estilo Inativo (Metal Bronzeado Mocha) */
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 30px 80px 0 0 !important; /* Curva longa de divisória */
            margin-right: -25px !important; 
            padding: 0px 60px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 8px 0 15px rgba(0,0,0,0.1), inset 0 2px 5px rgba(255,255,255,0.5) !important;
        }

        /* --- EFEITO: ABRIU A PASTINHA (ABA ATIVA) --- */

        /* 🔵 PASTA XML ATIVA (AZUL CROMO) */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-22px) scale(1.05) !important;
            border-color: #00D1FF !important;
            border-bottom: 5px solid white !important; /* Visual de abertura */
            box-shadow: 0 -15px 30px rgba(0, 209, 255, 0.5), 0 10px 40px rgba(0, 209, 255, 0.2), inset 0 5px 10px rgba(255,255,255,0.8) !important;
            z-index: 100 !important;
        }

        /* 💗 PASTA FISCAL ATIVA (ROSA PINK GLOSS) */
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-22px) scale(1.05) !important;
            border-color: #FF69B4 !important;
            border-bottom: 5px solid white !important; /* Visual de abertura */
            box-shadow: 0 -15px 30px rgba(255, 105, 180, 0.5), 0 10px 40px rgba(255, 105, 180, 0.2), inset 0 5px 10px rgba(255,255,255,0.8) !important;
            z-index: 100 !important;
        }

        /* --- PAINEL INTERNO (O CONTEÚDO DA PASTA) --- */
        .stTabs .stTabs {
            background: rgba(255, 255, 255, 0.6) !important; /* Fundo que brilha */
            padding: 30px !important;
            border-radius: 0 40px 40px 40px !important;
            border: 3px solid #FFB6C1 !important;
            border-top: 6px solid #FF69B4 !important; /* Conexão com a capa rosa */
            box-shadow: inset 0 15px 25px rgba(0,0,0,0.05), 0 20px 40px rgba(0,0,0,0.05) !important;
            margin-top: -12px !important; /* Encaixe perfeito sob a aba mãe */
            animation: fadeIn 0.5s ease;
        }

        /* SUB-ABAS (AS FICHAS DENTRO DA PASTA) */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: #FFFFFF !important;
            border-radius: 15px 40px 0 0 !important;
            font-size: 1.1rem !important;
            color: #DB7093 !important;
            border: 1px solid #FFD1DC !important;
            margin-right: 5px !important;
            box-shadow: 3px 0 8px rgba(0,0,0,0.05) !important;
        }

        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFF0F5 0%, #FFB6C1 100%) !important;
            color: #C71585 !important;
            transform: translateY(-10px) !important;
            box-shadow: 0 10px 20px rgba(255, 182, 193, 0.8) !important; /* Glow Shine */
            border-bottom: 4px solid #FF69B4 !important;
        }

        /* BOTÕES MESTRE */
        .stButton > button {
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: white !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-weight: 700 !important;
            box-shadow: 0 8px 20px rgba(139, 90, 43, 0.3), inset 0 2px 5px rgba(255,255,255,0.4) !important;
            text-transform: uppercase;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
    """, unsafe_allow_html=True)
