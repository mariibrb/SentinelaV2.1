import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDO DO APP (ÚNICA PARTE REATIVA) */
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.8s ease-in-out !important; }

        div:has(#modulo-xml) .stApp { background: radial-gradient(circle at top right, #D6F2FF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-amarelo) .stApp { background: radial-gradient(circle at top right, #FFF9C4 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-conformidade) .stApp { background: radial-gradient(circle at top right, #FFDEEF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-apuracao) .stApp { background: radial-gradient(circle at top right, #DFFFEA 0%, #F8F9FA 100%) !important; }

        /* 2. MENU SUPERIOR (BOTÕES) */
        div.stButton > button {
            color: white !important;
            border: none !important;
            border-radius: 15px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            height: 75px !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            text-transform: uppercase;
            opacity: 0.6 !important;
        }

        /* ESTADOS ATIVOS DO MENU - BRILHO BRANCO */
        div:has(#modulo-xml) div.stHorizontalBlock > div:nth-child(1) button,
        div:has(#modulo-amarelo) div.stHorizontalBlock > div:nth-child(2) button,
        div:has(#modulo-conformidade) div.stHorizontalBlock > div:nth-child(3) button,
        div:has(#modulo-apuracao) div.stHorizontalBlock > div:nth-child(4) button {
            opacity: 1 !important;
            transform: scale(1.1) translateY(-5px) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.9) !important;
            border: 3px solid #FFFFFF !important;
        }

        /* 3. NEUTRALIZAÇÃO TOTAL DA ÁREA DE UPLOAD (SOLUÇÃO DEFINITIVA) */
        
        /* Força a borda pontilhada para cinza neutro */
        [data-testid="stFileUploader"] {
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            border-radius: 20px !important;
        }

        /* Força o botão "Browse files" para cinza escuro, removendo cores do setor */
        [data-testid="stFileUploader"] section button {
            background-color: #6C757D !important;
            color: #FFFFFF !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* Garante que o hover do botão de upload não acenda colorido */
        [data-testid="stFileUploader"] section button:hover {
            background-color: #495057 !important;
            color: #FFFFFF !important;
        }

        /* Remove brilhos (glows) coloridos que vazam para dentro do uploader */
        [data-testid="stFileUploader"] * {
            box-shadow: none !important;
            text-decoration: none !important;
        }

        /* 4. ABAS E PAINÉIS */
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px 30px 0 0 !important;
            font-weight: 700;
            background: rgba(255,255,255,0.5) !important;
        }

        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(10px);
            border-radius: 25px !important;
            border: 1px solid #DEE2E6;
        }
        </style>
    """, unsafe_allow_html=True)
