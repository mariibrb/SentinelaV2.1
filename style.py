import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

        /* RESET TOTAL DO VISUAL "WINDOWS XP" */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* FUNDO DE ESTÚDIO (SUAVE E MODERNO) */
        .stApp {
            background: radial-gradient(circle at top left, #FDFBF9 0%, #F5EFE6 100%) !important;
        }

        .block-container { padding-top: 2rem !important; }
        
        /* FONTE DE GRIFE (JAKARTA SANS) */
        html, body, [class*="st-"] { 
            font-family: 'Plus Jakarta Sans', sans-serif !important; 
        }

        /* --- O TÍTULO "APPLE STYLE" --- */
        .titulo-principal { 
            color: #3D2B1F; 
            font-size: 3.5rem; 
            font-weight: 800; 
            margin-bottom: -10px;
            letter-spacing: -2px;
            background: linear-gradient(135deg, #5D3A1A 0%, #A67B5B 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 5px 10px rgba(93, 58, 26, 0.1));
        }

        /* BARRA DE LUXO (PÍLULA NEUMÓRFICA) */
        .barra-marsala { 
            width: 100px; 
            height: 10px; 
            background: #FF69B4; 
            border-radius: 50px; 
            margin-bottom: 50px;
            box-shadow: 0 10px 20px rgba(255, 105, 180, 0.3), inset 0 2px 4px rgba(255, 255, 255, 0.5);
        }

        /* --- EXTERMINANDO O QUADRADO AO REDOR DAS ABAS --- */
        /* Remove a linha de fundo e a borda da caixa das abas */
        .stTabs [data-baseweb="tab-border"] {
            display: none !important;
        }
        
        /* Garante que o container das abas seja invisível */
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important;
            background-color: transparent !important;
            border-style: none !important;
            padding: 10px 0px !important;
        }

        /* --- ABAS PÍLULA (DESIGN LIMPO) --- */
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: rgba(230, 213, 195, 0.4) !important;
            border-radius: 30px !important; 
            padding: 0px 35px !important;
            font-size: 16px !important; 
            font-weight: 600 !important;
            color: #5B4D42 !important;
            /* Remove bordas que o Streamlit força */
            border: 1px solid rgba(255, 255, 255, 0.6) !important;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.02), inset 2px 2px 5px rgba(255,255,255,0.7) !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) scale(1.05) !important;
            background: white !important;
            color: #FF69B4 !important;
            box-shadow: 0 15px 30px rgba(255, 105, 180, 0.2) !important;
        }

        .stTabs [aria-selected="true"] {
            background: #3D2B1F !important;
            color: white !important;
            font-weight: 700 !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(61, 43, 31, 0.4) !important;
        }

        /* --- BOTÕES "3D LUXO" --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #A67B5B, #5D3A1A) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 18px 30px !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            letter-spacing: 1px;
            border: 2px solid rgba(255, 105, 180, 0.3) !important; 
            box-shadow: 8px 8px 20px rgba(0,0,0,0.1), inset 0 2px 4px rgba(255,255,255,0.2) !important;
            transition: all 0.3s ease-in-out !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: scale(1.03) !important;
            box-shadow: 0 20px 40px rgba(255, 105, 180, 0.4) !important; 
            border-color: #FF69B4 !important;
        }

        /* --- CONTAINER DE STATUS --- */
        .status-container {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(15px);
            padding: 25px;
            border-radius: 35px;
            border-left: 12px solid #FF69B4;
            box-shadow: 15px 15px 40px rgba(0,0,0,0.03);
            border-top: 1px solid rgba(255,255,255,0.8);
        }

        /* CARD DE INFORMAÇÕES */
        [data-testid="stMetric"] {
            background: white !important;
            padding: 20px !important;
            border-radius: 30px !important;
            box-shadow: 10px 10px 30px rgba(0,0,0,0.02) !important;
            border: 1px solid #f0f0f0 !important;
        }

        [data-testid="stMetricValue"] {
            color: #3D2B1F !important;
            font-weight: 800 !important;
        }
        </style>
    """, unsafe_allow_html=True)
