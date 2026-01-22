import streamlit st

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

        /* --- ABA MÃE ATIVA: NEON EXTREMO --- */

        /* 🔵 ABA 1 (XML): AZUL NEON */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #00D1FF !important;
            box-shadow: 0 0 20px #00D1FF, 0 0 50px #00D1FF, 0 0 100px rgba(0, 209, 255, 0.4), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* 💗 ABA 2 (CONFORMIDADE): ROSA NEON */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #FF1493 !important;
            box-shadow: 0 0 20px #FF1493, 0 0 50px #FF1493, 0 0 100px rgba(255, 20, 147, 0.4), inset 0 5px 15px rgba(255,255,255,0.9) !important;
            z-index: 100 !important;
        }

        /* --- 📦 O CAIXOTE BRANCO COM BORDA NEON (PADRONIZADO) --- */

        /* Aplica a base branca para todas as abas */
        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.85) !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -20px !important;
            box-shadow: inset 0 20px 40px rgba(0,0,0,0.05) !important;
            border: 4px solid transparent !important;
        }

        /* CAIXOTE DA ANÁLISE XML (Contorno Azul) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 4px solid #00D1FF !important;
            border-top: 8px solid #00BFFF !important;
            box-shadow: 0 15px 50px rgba(0, 209, 255, 0.3) !important;
        }

        /* CAIXOTE DA CONFORMIDADE (Contorno Rosa) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 4px solid #FFB6C1 !important;
            border-top: 8px solid #FF69B4 !important;
            box-shadow: 0 15px 50px rgba(255, 105, 180, 0.3) !important;
        }

        /* --- SUB-ABAS (SÓ NO FISCAL) --- */
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #FDFDFD !important;
            border-radius: 20px 55px 0 0 !important;
            font-size: 1.2rem !important;
            color: #DB7093 !important;
            border: 1px solid #FFD1DC !important;
            margin-right: 5px !important;
        }

        .stTabs .stTabs [aria-selected="true"] {
            background: linear-gradient(145deg, #FFD1DC 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-12px) !important;
            box-shadow: 0 0 25px #FF69B4 !important;
            border-bottom: 5px solid white !important;
        }
        </style>
    """, unsafe_allow_html=True)
