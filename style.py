import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO GERAL */
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.8s ease-in-out !important; }

        /* 2. MENU SUPERIOR (MANTIDO) */
        div.stButton > button {
            color: white !important;
            border-radius: 15px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            height: 75px !important;
            text-transform: uppercase;
        }

        /* 3. ISOLAMENTO TOTAL DA ZONA AZUL (GARIMPEIRO) */
        /* Esta regra diz: SE estivermos no módulo XML, force TUDO do uploader para cinza */
        
        div:has(#modulo-xml) [data-testid="stFileUploader"] {
            border: 2px dashed #ADB5BD !important; /* Borda Cinza */
            background: #F8F9FA !important; /* Fundo Neutro */
        }

        div:has(#modulo-xml) [data-testid="stFileUploader"] section button {
            background-color: #6C757D !important; /* Botão Cinza Chumbo */
            color: white !important;
            border: none !important;
            box-shadow: none !important;
        }

        div:has(#modulo-xml) [data-testid="stFileUploader"] section button:hover {
            background-color: #495057 !important;
        }

        div:has(#modulo-xml) [data-testid="stFileUploader"] svg {
            fill: #6C757D !important; /* Ícone Cinza */
        }

        /* 4. AS OUTRAS ZONAS CONTINUAM COM SUAS REGRAS INDEPENDENTES */
        /* Rosa */
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; }
        /* Verde */
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #2ECC71 !important; }

        /* 5. ABAS INTERNAS (MANTENDO SUA LÓGICA DE CORES) */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; }

        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(10px);
            border-radius: 25px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
        }
        </style>
    """, unsafe_allow_html=True)
