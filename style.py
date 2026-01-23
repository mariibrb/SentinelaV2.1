import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* 1. FUNDAÇÃO */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }

        /* =================================================================================
           2. MENU MASTER NO TOPO (BOTÕES DE PRATA)
           Transforma o st.radio em barras de metal que acendem
        ================================================================================= */
        [role="radiogroup"] {
            display: flex;
            justify-content: center;
            gap: 20px;
            background: transparent;
            margin-bottom: 30px;
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* BOTÃO INATIVO (BARRINHA DE PRATA) */
        [role="radiogroup"] label {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important; /* O Padrão Rihanna */
            border: 2px solid #ADB5BD !important;
            border-radius: 15px !important;
            padding: 15px 30px !important;
            min-width: 200px;
            text-align: center;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700 !important;
            color: #495057 !important;
            cursor: pointer !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease !important;
            display: flex; justify-content: center;
        }

        /* HOVER COM BRILHO */
        [role="radiogroup"] label:hover {
            transform: translateY(-5px);
            background: linear-gradient(0deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.8) !important;
        }

        /* --- BOTÕES ATIVOS (ACENDEM O NEON) --- */

        /* 🟦 XML ATIVO */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: #FFFFFF !important;
            border-color: #00BFFF !important;
            color: #00BFFF !important;
            font-weight: 900 !important;
            box-shadow: 0 0 25px rgba(0, 191, 255, 0.5) !important; /* Neon Azul */
            transform: scale(1.05);
        }

        /* 🟥 CONFORMIDADE ATIVO */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: #FFFFFF !important;
            border-color: #FF69B4 !important;
            color: #FF69B4 !important;
            font-weight: 900 !important;
            box-shadow: 0 0 25px rgba(255, 105, 180, 0.5) !important; /* Neon Rosa */
            transform: scale(1.05);
        }

        /* 🟩 APURAÇÃO ATIVO */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: #FFFFFF !important;
            border-color: #2ECC71 !important;
            color: #2ECC71 !important;
            font-weight: 900 !important;
            box-shadow: 0 0 25px rgba(46, 204, 113, 0.5) !important; /* Neon Verde */
            transform: scale(1.05);
        }

        /* =================================================================================
           3. PASTAS INTERNAS (O VISUAL DIAMANTE VOLTOU 💎)
           Agora as abas de dentro (ICMS, RET) são pastas brilhantes
        ================================================================================= */
        
        .stTabs [data-baseweb="tab-list"] { gap: 10px; border-bottom: none; padding-top: 20px; }

        /* A PASTA DIAMANTE (Inativa) */
        .stTabs [data-baseweb="tab"] {
            height: 65px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #CED4DA 100%) !important; /* Prata mais escuro */
            border-radius: 20px 50px 0 0 !important; /* O formato assimétrico chique */
            padding: 0px 40px !important;
            border: 1px solid #ADB5BD !important;
            border-bottom: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 700 !important;
            color: #6C757D !important;
            margin-right: 5px !important;
            transition: all 0.3s ease !important;
        }

        /* BRILHO ANIMADO (SHINE BRIGHT) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
            color: #212529 !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* A PASTA ATIVA (Branca, Alta e com a Cor do Módulo) */
        .stTabs [aria-selected="true"] {
            height: 75px !important; /* Sobe mais que as outras */
            background: #FFFFFF !important;
            color: #212529 !important;
            font-weight: 800 !important;
            border-top: 5px solid !important; /* A cor vem do módulo abaixo */
            transform: translateY(-5px) !important;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1) !important;
            z-index: 10;
        }

        /* CORES DAS PASTAS INTERNAS */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { border-top-color: #00BFFF !important; color: #00BFFF !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }

        /* =================================================================================
           4. CAIXOTÃO E ENVELOPES
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border: 1px solid #ADB5BD;
            border-top: none; 
            border-radius: 0 20px 20px 20px !important;
            padding: 50px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        }

        /* Bordas Coloridas do Painel */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top: 5px solid #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top: 5px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top: 5px solid #2ECC71 !important; }

        /* ENVELOPES (SEMPRE VISÍVEIS E PRATEADOS) */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 15px !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA !important;
            border: 2px dashed #ADB5BD !important; /* Prata padrão */
            transition: all 0.3s ease;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -25px; left: 50%; transform: translateX(-50%); font-size: 30px; z-index: 99; }

        /* Cores dos Envelopes por Módulo */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; background: #F0F8FF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; background: #FFF0F5 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #2ECC71 !important; background: #F0FFF4 !important; }

        /* BOTÕES GERAIS (PRATA DIAMANTE - SEM VERMELHO) */
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 10px !important;
            font-weight: 800 !important;
            text-transform: uppercase;
            box-shadow: none !important;
            height: 50px;
        }
        
        /* Hover dos Botões com Cor do Módulo */
        div:has(#modulo-xml) div.stDownloadButton > button:hover { border-color: #00BFFF !important; box-shadow: 0 0 15px #00BFFF !important; }
        div:has(#modulo-conformidade) div.stDownloadButton > button:hover { border-color: #FF69B4 !important; box-shadow: 0 0 15px #FF69B4 !important; }
        div:has(#modulo-apuracao) div.stDownloadButton > button:hover { border-color: #2ECC71 !important; box-shadow: 0 0 15px #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
