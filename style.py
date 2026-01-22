import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* LIMPEZA TOTAL DO TOPO */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
            height: 0px !important;
            padding: 0px !important;
            margin: 0px !important;
        }
        
        /* FUNDO OFF-WHITE QUENTE */
        .stApp {
            background-color: #FDFBF9 !important; 
        }

        /* AJUSTE DO CONTEÚDO */
        .block-container { padding-top: 1.5rem !important; }
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* --- O NOVO CABEÇALHO DESIGNER --- */
        .titulo-principal { 
            color: #5D3A1A; 
            font-size: 3rem; 
            font-weight: 800; 
            margin-bottom: 0px;
            letter-spacing: -1px;
            background: linear-gradient(90deg, #5D3A1A, #A67B5B);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* BARRA DESIGNER (EFEITO PÍLULA) */
        .barra-marsala { 
            width: 120px; 
            height: 8px; 
            background: linear-gradient(90deg, #FF69B4, #A67B5B); 
            border-radius: 50px; 
            margin-bottom: 40px;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
        }

        /* CARD DE VIDRO PARA O TÍTULO (OPCIONAL NO HTML) */
        .header-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            padding: 20px 40px;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 20px 40px rgba(93, 58, 26, 0.08);
            margin-bottom: 40px;
            display: inline-block;
        }

        /* --- ABAS ARREDONDADAS E METALIZADAS --- */
        .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #E6D5C3 !important; 
            border-radius: 20px 20px 20px 20px !important; /* Arredondado total */
            padding: 10px 35px !important;
            margin-right: 10px !important;
            font-size: 18px !important; 
            font-weight: 600 !important;
            color: #5D3A1A !important;
            transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1) !important;
            border: 1px solid rgba(255,255,255,0.5) !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) scale(1.02) !important;
            background: #F0E2D3 !important;
            color: #3E2511 !important;
            box-shadow: 0 15px 30px rgba(255, 105, 180, 0.25) !important;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #A67B5B 0%, #5D3A1A 100%) !important;
            color: #FFFFFF !important;
            font-weight: 800 !important;
            box-shadow: 0 10px 25px rgba(93, 58, 26, 0.3) !important;
            border: 2px solid #FF69B4 !important; /* Borda Pink de Destaque */
        }

        /* --- BOTÕES "PÍLULA" LUXO --- */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(135deg, #A67B5B 0%, #5D3A1A 100%) !important;
            color: #FFFFFF !important;
            border-radius: 100px !important; /* Estilo Pílula moderna */
            padding: 15px 30px !important;
            font-weight: 700 !important;
            border: none !important;
            box-shadow: 0 10px 20px rgba(93, 58, 26, 0.2), inset 0 2px 2px rgba(255,255,255,0.2) !important;
            transition: all 0.3s ease !important;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 15px 30px rgba(255, 105, 180, 0.4) !important; /* Brilho Pink Glow */
            filter: brightness(1.1) !important;
        }

        /* CONTAINER DE STATUS DESIGNER */
        .status-container {
            background: white;
            padding: 20px;
            border-radius: 25px;
            border-left: 10px solid #FF69B4;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
            border-top: 1px solid #f0f0f0;
        }
        </style>
    """, unsafe_allow_html=True)
