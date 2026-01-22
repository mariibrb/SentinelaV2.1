import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. SIDEBAR E FUNDO MOCHA --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 5px solid #FF69B4 !important;
            z-index: 999999 !important;
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }

        /* --- 2. ABAS MESTRE (ETIQUETAS DA PASTA) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        /* Lista de abas principais */
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px !important;
            padding: 40px 0 0 0 !important; /* Colado na pasta abaixo */
            align-items: flex-end;
            z-index: 2 !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 80px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 30px 80px 0 0 !important; 
            margin-right: -25px !important;
            padding: 0px 60px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.5rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
        }

        /* Cor da Etiqueta Ativa */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; color: white !important; }

        /* --- 3. 📦 O CAIXOTÃO GIGANTE (A PASTA ABERTA) --- */
        /* Esta regra força o painel a subir e "abraçar" as sub-abas */
        [data-testid="stTabPanel"] {
            background: white !important;
            padding: 60px 40px 40px 40px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important; /* Encaixe perfeito com a aba mãe */
            min-height: 700px !important;
            position: relative !important;
            z-index: 1 !important;
        }

        /* --- 4. BORDAS NEON SOMBREADAS (IGUAL À FOTO) --- */
        
        /* Zona XML: Tudo Azul */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #00D1FF !important;
            box-shadow: 0 0 30px rgba(0, 209, 255, 0.4), 0 20px 80px rgba(0, 0, 0, 0.1) !important;
        }

        /* Zona Conformidade: Tudo Rosa */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border: 6px solid #FF69B4 !important;
            box-shadow: 0 0 30px rgba(255, 105, 180, 0.4), 0 20px 80px rgba(0, 0, 0, 0.1) !important;
        }

        /* --- 5. SUB-ABAS (MORANDO DENTRO DA PASTA) --- */
        /* Localizadas no topo do caixotão branco */
        .stTabs .stTabs [data-baseweb="tab-list"] {
            padding: 0 0 30px 0 !important;
            background: transparent !important;
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: #F8F9FA !important;
            border-radius: 15px 40px 0 0 !important;
            font-size: 1.1rem !important;
            border: 1px solid #E8DCCB !important;
        }

        /* Sub-aba Ativa Azul */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #00BFFF !important;
            color: white !important;
            border-color: #00D1FF !important;
        }

        /* Sub-aba Ativa Rosa */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #FF69B4 !important;
            color: white !important;
            border-color: #FF69B4 !important;
        }

        /* --- 6. CAIXA DE UPLOAD LIMPA --- */
        [data-testid="stFileUploader"] {
            background: #FDFDFD !important;
            border: 2px dashed #D8C7B1 !important;
            border-radius: 25px !important;
            padding: 30px !important;
        }

        </style>
    """, unsafe_allow_html=True)
