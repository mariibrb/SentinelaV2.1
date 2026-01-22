import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. ESTRUTURA GERAL --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 5px solid #FF69B4 !important;
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }

        /* --- 2. ABAS MESTRE DIAMANTE --- */
        .stTabs { overflow: visible !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; 
            overflow: visible !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 70px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
        }

        /* Ativas */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; transform: translateY(-30px) !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; transform: translateY(-30px) !important; }

        /* --- 3. 📦 O CAIXOTÃO (PASTA MÃE) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            border: 6px solid transparent !important;
        }

        /* Neon Bloom no Caixotão */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border-color: #00D1FF !important;
            box-shadow: 0 0 30px #00D1FF, 0 0 80px rgba(0, 209, 255, 0.4) !important;
        }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border-color: #FF69B4 !important;
            box-shadow: 0 0 30px #FF69B4, 0 0 80px rgba(255, 105, 180, 0.4) !important;
        }

        /* --- 4. ✉️ EFEITO ENVELOPE (ÁREA DE UPLOAD) --- */
        [data-testid="stFileUploader"] {
            background-color: #FCF9F5 !important; /* Cor de papel craft clarinho */
            padding: 40px !important;
            border-radius: 10px 10px 40px 40px !important; /* Curva de envelope no fundo */
            border: 1px solid #E8DCCB !important;
            border-top: 15px solid #FDFDFD !important; /* A aba do envelope */
            box-shadow: 
                0 15px 35px rgba(0,0,0,0.08), 
                inset 0 -10px 20px rgba(232, 220, 203, 0.3) !important;
            margin: 20px 0 !important;
            position: relative;
        }

        /* Detalhe do lacre do envelope */
        [data-testid="stFileUploader"]::before {
            content: "📂";
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 25px;
            background: white;
            border-radius: 50%;
            padding: 5px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        /* --- 5. 📄 ÁREA DE AUDITORIA (ILHA BRANCA) --- */
        div.stExpander, div.element-container:has(h1, h2, h3), .stDataFrame {
            background-color: white !important;
            padding: 30px !important;
            border-radius: 20px !important;
            border: 1px solid #f0f0f0 !important;
            box-shadow: 0 5px 25px rgba(0,0,0,0.03) !important;
        }

        /* Sub-abas */
        .stTabs .stTabs [data-baseweb="tab-list"] { padding: 0 0 30px 0 !important; }
        .stTabs .stTabs [data-baseweb="tab"] { height: 60px !important; border-radius: 15px 45px 0 0 !important; }

        </style>
    """, unsafe_allow_html=True)
