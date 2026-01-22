import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. SIDEBAR BOUTIQUE --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 5px solid #FF69B4 !important;
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

        /* --- 2. TÍTULO NEON SHINE --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            text-shadow: 0 0 15px rgba(255, 105, 180, 0.4);
        }

        /* --- 3. ABAS MÃE (PASTAS METALIZADAS) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px !important;
            padding: 40px 0 !important;
            align-items: flex-end;
        }

        /* Inativas (Metal Bronze) */
        .stTabs [data-baseweb="tab"] {
            height: 90px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 40px 110px 0 0 !important; 
            margin-right: -35px !important;
            padding: 0px 75px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.7rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 10px 0 20px rgba(0,0,0,0.15), inset 0 2px 5px rgba(255,255,255,0.8) !important;
        }

        /* 🔵 MÃE 1: ANALISE XML (AZUL GLOSS) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #00D1FF !important;
            /* GLITTER SHINE AZUL */
            box-shadow: 0 0 20px #00D1FF, 0 0 50px #00D1FF, 0 0 100px rgba(0, 209, 255, 0.4), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* 💗 MÃE 2: CONFORMIDADE DOMINIO (ROSA GLOSS) */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #FF1493 !important;
            /* GLITTER SHINE ROSA */
            box-shadow: 0 0 20px #FF1493, 0 0 50px #FF1493, 0 0 100px rgba(255, 20, 147, 0.4), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* --- 4. CAIXOTE BRANCO (GAVETA ABERTA COM BORDAS NEON) --- */
        
        /* CAIXOTE XML (AZUL) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.85) !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            border: 4px solid #00D1FF !important;
            border-top: 8px solid #00BFFF !important;
            margin-top: -20px !important;
            box-shadow: 0 15px 50px rgba(0, 209, 255, 0.3) !important;
        }

        /* CAIXOTE FISCAL (ROSA) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.85) !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            border: 4px solid #FFB6C1 !important;
            border-top: 8px solid #FF69B4 !important;
            margin-top: -20px !important;
            box-shadow: 0 15px 50px rgba(255, 105, 180, 0.3) !important;
        }

        /* --- 5. 💗 SUB-ABAS (DNA ROSA IGUAL À MÃE) --- */
        
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 65px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #E8DCCB 100%) !important;
            border-radius: 20px 55px 0 0 !important;
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            border: 1px solid #D8C7B1 !important;
            margin-right: -10px !important;
        }

        /* REGRA ABSOLUTA POR NOME (DETERMINANDO AS CORES QUE VOCÊ QUER) */
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("ICMS/IPI"))[aria-selected="true"],
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("Difal/st"))[aria-selected="true"],
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("RET"))[aria-selected="true"],
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("Pis/cofins"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            background-color: #FF69B4 !important; /* Trava anti-azul */
            color: white !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #FF1493 !important;
            border-bottom: 5px solid white !important;
            /* GLOW NEON FILHA */
            box-shadow: 0 0 20px #FF1493, 0 0 40px rgba(255, 20, 147, 0.6), inset 0 3px 10px rgba(255,255,255,0.7) !important;
        }

        /* FORÇA TEXTO BRANCO NAS ATIVAS */
        .stTabs .stTabs button[aria-selected="true"] div {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
