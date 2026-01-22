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
            box-shadow: 15px 0 40px rgba(255, 105, 180, 0.2) !important;
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
            text-transform: uppercase;
            line-height: 1;
            text-shadow: 0 0 20px rgba(255, 105, 180, 0.3); /* Brilho no título */
        }

        /* --- SISTEMA DE PASTAS (ABAS MÃE) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px !important;
            background-color: transparent !important;
            padding: 40px 0 !important;
            align-items: flex-end;
        }

        /* Aba Mãe Inativa (Aspecto de Papelão/Metal Fosco) */
        .stTabs [data-baseweb="tab"] {
            height: 90px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 40px 100px 0 0 !important; /* Curva de pasta bem exagerada */
            margin-right: -30px !important;
            padding: 0px 70px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.7rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 10px 0 20px rgba(0,0,0,0.1) !important;
        }

        /* --- 💡 O NEON MAIS ACESO (ABAS MÃE ATIVAS) --- */

        /* 🔵 PASTINHA XML ATIVA (NEON AZUL ELÉTRICO) */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-30px) scale(1.1) !important; /* Pulo gigante */
            border-color: #00D1FF !important;
            /* NEON EXPLOSIVO */
            box-shadow: 0 0 20px #00D1FF, 0 0 40px #00D1FF, 0 0 80px rgba(0, 209, 255, 0.6), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* 💗 PASTINHA FISCAL ATIVA (NEON ROSA SHOCK) */
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-30px) scale(1.1) !important; /* Pulo gigante */
            border-color: #FF1493 !important;
            /* NEON EXPLOSIVO */
            box-shadow: 0 0 20px #FF1493, 0 0 40px #FF1493, 0 0 80px rgba(255, 20, 147, 0.6), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* --- HIERARQUIA: SUB-PASTINHAS (DENTRO DA MÃE) --- */
        .stTabs .stTabs {
            background: rgba(255, 255, 255, 0.8) !important;
            padding: 40px !important;
            border-radius: 0 50px 50px 50px !important;
            border: 4px solid #FF69B4 !important; /* Borda grossa neon */
            margin-top: -20px !important; /* Encaixe total na mãe */
            box-shadow: 0 0 50px rgba(255, 105, 180, 0.3) !important; /* Brilho que sai de dentro da pasta */
        }

        /* Fichas menores de Sub-pastas */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #FDFDFD !important;
            border-radius: 20px 50px 0 0 !important;
            font-size: 1.2rem !important;
            color: #DB7093 !important;
            border: 1px solid #FFD1DC !important;
            margin-right: 5px !important;
            box-shadow: none !important;
        }

        /* SUB-PASTA ATIVA (FOCO TOTAL) */
        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFD1DC 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-15px) !important;
            box-shadow: 0 0 30px #FF69B4 !important; /* Neon na sub-aba */
            border-bottom: 5px solid white !important;
        }

        /* BOTÃO ADM COM PULSO NEON */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #D4145A) !important;
            color: white !important;
            box-shadow: 0 0 30px rgba(255, 20, 147, 0.7) !important;
            font-weight: 800 !important;
            border-radius: 50px !important;
            border: 2px solid white !important;
        }
        </style>
    """, unsafe_allow_html=True)
