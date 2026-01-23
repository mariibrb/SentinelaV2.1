import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* 1. BASE E FUNDO RIHANNA */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important; 
            color: #495057 !important; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase; 
            text-shadow: 1px 1px 10px rgba(255, 255, 255, 0.9) !important; 
        }

        /* =================================================================================
           2. MENU MASTER (BOTÕES METALIZADOS COM BRILHO)
        ================================================================================= */
        [role="radiogroup"] { display: flex; justify-content: center; gap: 20px; margin-bottom: 30px; }
        [role="radiogroup"] label > div:first-child { display: none !important; }

        [role="radiogroup"] label {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 12px !important;
            padding: 12px 25px !important;
            min-width: 200px;
            text-align: center;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700;
            color: #495057 !important;
            cursor: pointer !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease !important;
        }

        /* EFEITO SHINE AO PASSAR O MOUSE */
        [role="radiogroup"] label:hover {
            transform: translateY(-5px);
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
        }

        /* ESTADOS ATIVOS (CORES APROVADAS) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] { border: 3px solid #00BFFF !important; background: #FFFFFF !important; color: #00BFFF !important; box-shadow: 0 0 20px rgba(0, 191, 255, 0.4) !important; }
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] { border: 3px solid #FF69B4 !important; background: #FFFFFF !important; color: #FF69B4 !important; box-shadow: 0 0 20px rgba(255, 105, 180, 0.4) !important; }
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] { border: 3px solid #2ECC71 !important; background: #FFFFFF !important; color: #2ECC71 !important; box-shadow: 0 0 20px rgba(46, 204, 113, 0.4) !important; }

        /* =================================================================================
           3. ABAS PASTINHA (DEGRADÊ NEON GAMER)
        ================================================================================= */
        .stTabs [data-baseweb="tab-list"] { gap: 8px; border-bottom: none; }
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 8px 30px 0 0 !important; /* Visual de pasta escolar */
            border: 1px solid #ADB5BD !important;
            border-bottom: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600;
            color: #6C757D !important;
            transition: 0.3s;
        }

        .stTabs [aria-selected="true"] {
            background: #FFFFFF !important;
            transform: translateY(-4px) !important;
            border-top: 5px solid !important;
            font-weight: 800 !important;
        }

        /* CORES DAS ABAS POR MÓDULO */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { border-top-color: #00BFFF !important; color: #00BFFF !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }

        /* =================================================================================
           4. ENVELOPES BONITINHOS (TONS PASTÉIS APROVADOS)
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 40px 25px 25px 25px !important;
            border-radius: 12px !important;
            position: relative !important;
            border: 2px dashed #CED4DA;
            background-color: #FFFFFF;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -20px; left: 20px; font-size: 26px; z-index: 99; }

        /* CORES DOS ENVELOPES */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { background-color: #F0F8FF !important; border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background-color: #FFF5F8 !important; border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background-color: #F0FFF4 !important; border-color: #2ECC71 !important; }

        /* =================================================================================
           5. BOTÕES E ANIMAÇÕES
        ================================================================================= */
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 10px !important;
            font-weight: 800 !important;
            text-transform: uppercase;
            transition: 0.3s;
        }

        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border: 1px solid #DEE2E6;
            border-radius: 0 12px 12px 12px !important;
            padding: 35px !important;
            margin-top: -1px;
            border-top: 4px solid #DEE2E6;
        }

        /* Vareta colorida por módulo */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
