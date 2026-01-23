import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* 1. FUNDAÇÃO */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 1px solid #CED4DA !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: #F4F6F9 !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 2px 2px 0px #FFFFFF !important; }

        /* 2. ENVELOPES GLOBAIS (NUNCA SOMEM) */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 8px !important;
            border-top: 0px !important;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #FFFFFF;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -15px; left: 20px; font-size: 24px; z-index: 99; }

        /* 3. DESIGN DAS PASTAS SUSPENSAS (ABAS) */
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px !important;
            padding-top: 20px !important; /* Espaço pro visor */
            border-bottom: 2px solid #DEE2E6 !important; /* Trilho */
            padding-bottom: 0px !important;
        }

        /* O VISOR (Aba Inativa) */
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #E9ECEF !important; /* Cor de papel pardo */
            border-radius: 10px 10px 0 0 !important; /* Canto de plástico */
            padding: 0px 30px !important;
            border: 1px solid #CED4DA !important;
            border-bottom: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 1.1rem !important;
            color: #ADB5BD !important;
            margin-right: 2px !important;
            transform: translateY(5px) !important; /* Afundado */
        }

        /* O VISOR ATIVO (Sobe e Ganha Cor) */
        .stTabs [aria-selected="true"] {
            transform: translateY(2px) !important; /* Cola no trilho */
            height: 60px !important;
            background: #FFFFFF !important;
            color: #212529 !important;
            font-weight: 800 !important;
            border-top-width: 6px !important; /* A cor vem do módulo abaixo */
            border-bottom: none !important;
            z-index: 100;
        }

        /* 4. MÓDULOS DE COR (AQUI A MÁGICA ACONTECE) */
        /* O CSS procura a DIV ID que colocamos no código */

        /* 🟦 MÓDULO XML (AZUL) */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] {
            border-top-color: #00BFFF !important;
            color: #00BFFF !important;
        }
        div:has(#modulo-xml) [data-testid="stFileUploader"] {
            border: 2px dashed #00BFFF !important;
            background: #F0F8FF !important;
        }
        div:has(#modulo-xml) div.stDownloadButton > button:hover {
            background: #00BFFF !important; color: white !important;
        }

        /* 🟥 MÓDULO CONFORMIDADE (ROSA) */
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] {
            border-top-color: #FF69B4 !important;
            color: #FF69B4 !important;
        }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] {
            border: 2px dashed #FF69B4 !important;
            background: #FFF0F5 !important;
        }
        /* O RET vai ficar Rosa automaticamente */

        /* 🟩 MÓDULO APURAÇÃO (VERDE) */
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] {
            border-top-color: #2ECC71 !important;
            color: #2ECC71 !important;
        }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] {
            border: 2px dashed #2ECC71 !important;
            background: #F0FFF4 !important;
        }

        /* 5. ACABAMENTOS */
        /* O CORPO DA PASTA */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-left: 1px solid #DEE2E6;
            border-right: 1px solid #DEE2E6;
            border-bottom: 1px solid #DEE2E6;
            border-top: 6px solid #DEE2E6; /* Cor padrão, o JS pinta se precisar */
            border-radius: 0 0 15px 15px !important;
            margin-top: -2px !important;
            padding: 40px !important;
        }
        
        /* Cor da Vareta por Módulo */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #2ECC71 !important; }

        /* Botões Sólidos */
        div.stButton > button, div.stDownloadButton > button {
            background: #FFFFFF !important;
            color: #495057 !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 6px !important;
            text-transform: uppercase;
            font-weight: 700 !important;
            box-shadow: 0 2px 0 #ADB5BD !important;
        }
        </style>
    """, unsafe_allow_html=True)
