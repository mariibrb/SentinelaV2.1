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
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }

        /* --- TÍTULO --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase;
        }

        /* --- ABAS MÃE --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px !important;
            padding: 40px 0 !important;
            align-items: flex-end;
        }

        /* Inativas */
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
        }

        /* ABA MÃE 1 (XML) - AZUL */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #00D1FF !important;
            box-shadow: 0 0 50px rgba(0, 209, 255, 0.5) !important;
        }

        /* ABA MÃE 2 (CONFORMIDADE) - ROSA */
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            color: white !important;
            transform: translateY(-25px) scale(1.08) !important;
            border-color: #FF1493 !important;
            box-shadow: 0 0 50px rgba(255, 105, 180, 0.6) !important;
        }

        /* --- 📦 CAIXOTE BRANCO --- */
        .stTabs .stTabs {
            background: rgba(255, 255, 255, 0.85) !important;
            padding: 40px !important;
            border-radius: 0 60px 60px 60px !important;
            border: 4px solid #FFB6C1 !important;
            margin-top: -20px !important;
        }

        /* --- 💗 A REGRA QUE VOCÊ MANDOU CRIAR (POR NOME) --- */
        
        /* Esta regra caça o texto dentro do botão. Se achar o nome, aplica o ROSA */
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("ICMS"))[aria-selected="true"],
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("Difal"))[aria-selected="true"],
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("RET"))[aria-selected="true"],
        .stTabs .stTabs [data-baseweb="tab"]:has(div:contains("Pis"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF69B4 100%) !important;
            background-color: #FF69B4 !important;
            color: white !important;
            transform: translateY(-15px) scale(1.05) !important;
            border: 2px solid #FF1493 !important;
            border-bottom: 5px solid white !important;
            box-shadow: 0 0 25px #FF1493, 0 0 50px rgba(255, 20, 147, 0.6) !important;
        }

        /* Força o texto de todas elas a ser branco quando selecionado */
        .stTabs .stTabs button[aria-selected="true"] div {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
