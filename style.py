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

        /* --- TÍTULO DESIGNER --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }

        /* --- SISTEMA DE PASTAS (ABAS MÃE) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px !important;
            background-color: transparent !important;
            padding: 40px 0 !important;
            align-items: flex-end;
        }

        /* Aba Inativa: Metal Bronzeado Mocha */
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

        /* --- 💡 ABAS MÃE ATIVAS: NEON EXTREMO --- */

        /* 🔵 ABA 1 (XML): AZUL CROMADO + GLOW */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #00D1FF !important;
            box-shadow: 0 0 20px #00D1FF, 0 0 50px #00D1FF, 0 0 100px rgba(0, 209, 255, 0.4), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* 💗 ABA 2 (CONFORMIDADE): ROSA PINK GLOSS + GLOW */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #FF1493 !important;
            box-shadow: 0 0 20px #FF1493, 0 0 50px #FF1493, 0 0 100px rgba(255, 20, 147, 0.4), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* --- 📦 INTERIOR DA CAIXA BRANCA (GAVETA) --- */
        .stTabs .stTabs {
            background: rgba(255, 255, 255, 0.85) !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            border: 4px solid #FFB6C1 !important; /* CONEXÃO COM A MÃE ROSA */
            margin-top: -20px !important;
            box-shadow: 0 10px 60px rgba(255, 105, 180, 0.3), inset 0 20px 40px rgba(0,0,0,0.05) !important;
        }

        /* --- 💗 SUB-ABAS (FILHAS): CONFIGURAÇÃO IDÊNTICA À MÃE --- */
        
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 75px !important; /* Altura generosa para o layout gamer */
            background: linear-gradient(180deg, #FDFDFD 0%, #E8DCCB 100%) !important; /* Metalizado Mocha suave inativo */
            border-radius: 25px 65px 0 0 !important; /* Curva miniatura da mãe */
            font-size: 1.3rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            border: 1px solid #D8C7B1 !important;
            margin-right: -10px !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 5px 0 10px rgba(0,0,0,0.1) !important;
        }

        /* SUB-ABA ATIVA: CLONE DA CONFORMIDADE (ROSA NEON + SHINE) */
        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important; /* MESMO GRADIENTE DA MÃE */
            color: white !important;
            transform: translateY(-15px) scale(1.05) !important; /* "Pulo" e Escala Gamer */
            border-color: #FF1493 !important;
            /* MESMO BRILHO EXPLOSIVO DA MÃE: */
            box-shadow: 0 0 20px #FF1493, 0 0 45px rgba(255, 20, 147, 0.6), inset 0 3px 8px rgba(255,255,255,0.7) !important;
            z-index: 10 !important;
            border-bottom: 5px solid white !important;
        }

        /* BOTÃO ADM */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #D4145A) !important;
            color: white !important;
            box-shadow: 0 0 20px rgba(255, 20, 147, 0.5) !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
        }
        </style>
    """, unsafe_allow_html=True)
