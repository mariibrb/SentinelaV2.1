import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO E SIDEBAR */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #DEE2E6 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #6C757D !important; font-size: 0.9rem !important; font-weight: 800; text-transform: uppercase; padding: 5px 0 !important; letter-spacing: 2px; }

        /* 2. MENU SUPERIOR (ABAS MASTER) - ESTILO ORIGINAL APROVADO */
        div.stButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #CED4DA 100%) !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 12px 35px 0 0 !important; 
            padding: 12px 25px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800;
            color: #6C757D !important;
            transition: all 0.3s ease;
        }

        /* --- IDENTIDADE VISUAL POR SETOR (MENU) --- */
        div:has(#modulo-xml) div.stHorizontalBlock > div:nth-child(1) button { border-top: 4px solid #00BFFF !important; color: #212529 !important; transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0, 191, 255, 0.3); }
        div:has(#modulo-amarelo) div.stHorizontalBlock > div:nth-child(2) button { border-top: 4px solid #FFD700 !important; color: #212529 !important; transform: translateY(-5px); box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3); }
        div:has(#modulo-conformidade) div.stHorizontalBlock > div:nth-child(3) button { border-top: 4px solid #FF69B4 !important; color: #212529 !important; transform: translateY(-5px); box-shadow: 0 5px 15px rgba(255, 105, 180, 0.3); }
        div:has(#modulo-apuracao) div.stHorizontalBlock > div:nth-child(4) button { border-top: 4px solid #2ECC71 !important; color: #212529 !important; transform: translateY(-5px); box-shadow: 0 5px 15px rgba(46, 204, 113, 0.3); }

        /* 3. ABAS INTERNAS (PASTINHAS) - CORES VOLTARAM */
        .stTabs [data-baseweb="tab"] { border-radius: 8px 25px 0 0 !important; font-weight: 700; margin-right: 5px; background: #F1F3F5 !important; }
        
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-amarelo) .stTabs [aria-selected="true"] { background: #FFD700 !important; color: #212529 !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; }

        /* 4. ÁREA DE UPLOAD (ENVELOPES) - FUNDO E BORDA REATIVOS */
        [data-testid="stFileUploader"] {
            padding: 45px 25px 25px 25px !important;
            border-radius: 15px !important;
            border: 2px dashed #ADB5BD !important;
            position: relative !important;
        }

        /* FUNDOS E BORDAS POR ZONA */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { background: #EBF9FF !important; border-color: #00BFFF !important; }
        div:has(#modulo-amarelo) [data-testid="stFileUploader"] { background: #FFFDEB !important; border-color: #FFD700 !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background: #FFF0F5 !important; border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background: #F1FFF7 !important; border-color: #2ECC71 !important; }

        /* BOTÃO BROWSE FILES (O ÚNICO CINZA NEUTRO) */
        [data-testid="stFileUploader"] section button {
            background-color: #6C757D !important; 
            color: white !important;
            border: none !important;
        }
        [data-testid="stFileUploader"] section button:hover { background-color: #495057 !important; }

        /* 5. PAINEL CENTRAL (CONTAINER BRANCO) */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 0 15px 15px 15px !important;
            padding: 30px !important;
            border: 1px solid #DEE2E6;
        }
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top: 8px solid #00BFFF !important; }
        div:has(#modulo-amarelo) [data-testid="stTabPanel"] { border-top: 8px solid #FFD700 !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top: 8px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top: 8px solid #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
