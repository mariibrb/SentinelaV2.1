import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. FUNDO E SIDEBAR --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 5px solid #FF69B4 !important;
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }

        /* --- 2. ABAS MESTRE (AS ETIQUETAS) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important;
            padding: 40px 0 0 20px !important;
            position: relative !important;
            z-index: 10 !important; /* Fica acima da pasta */
        }

        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 25px 70px 0 0 !important; 
            border: 2px solid #A67B5B !important;
            font-size: 1.4rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
            margin-bottom: -4px !important; /* Encaixe cirúrgico */
        }

        /* --- 3. 💗 O CAIXOTÃO "PASTA" (ENGLOBA TUDO) --- */
        /* Esta é a regra que cria a moldura branca gigante que voce viu no print */
        [data-testid="stTabPanel"] {
            background: white !important;
            border-radius: 30px 60px 60px 60px !important;
            padding: 50px !important;
            margin-top: -5px !important; /* Cola na aba mãe */
            position: relative !important;
            z-index: 1 !important;
            min-height: 800px !important;
        }

        /* 🔵 BORDA SOMBREADA AZUL (Setor XML) */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #00D1FF !important;
            box-shadow: 0 0 35px rgba(0, 209, 255, 0.5), 0 20px 80px rgba(0,0,0,0.1) !important;
        }

        /* 💗 BORDA SOMBREADA ROSA (Setor Conformidade) */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #FF69B4 !important;
            box-shadow: 0 0 35px rgba(255, 105, 180, 0.5), 0 20px 80px rgba(0,0,0,0.1) !important;
        }

        /* --- 4. SUB-ABAS DENTRO DA PASTA (FOTO) --- */
        /* Forçamos elas a aparecerem dentro do caixote branco */
        .stTabs .stTabs [data-baseweb="tab-list"] {
            padding: 0 0 40px 0 !important;
            margin-top: 10px !important;
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: #F8F9FA !important;
            border-radius: 15px 40px 0 0 !important;
            font-size: 1.1rem !important;
            border: 1px solid #E8DCCB !important;
        }

        /* Cores Ativas por Setor */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* --- 5. CAMPOS DE UPLOAD --- */
        [data-testid="stFileUploader"] {
            background: #FFFFFF !important;
            border: 2px dashed #D8C7B1 !important;
            border-radius: 20px !important;
            padding: 25px !important;
        }

        </style>
    """, unsafe_allow_html=True)
