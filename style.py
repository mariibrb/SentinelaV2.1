import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO RIHANNA */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; text-shadow: 1px 1px 10px rgba(255, 255, 255, 0.9) !important; }

        /* =================================================================================
           2. MENU MASTER (PASTAS QUE SE ELEVAM E BRILHAM)
        ================================================================================= */
        [role="radiogroup"] { display: flex; justify-content: center; gap: 15px; margin-bottom: 20px; }
        [role="radiogroup"] label > div:first-child { display: none !important; }

        [role="radiogroup"] label {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 15px 50px 0 0 !important; 
            padding: 15px 30px !important;
            min-width: 220px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }

        /* EFEITO SHINE BRIGHT NO HOVER */
        [role="radiogroup"] label:hover {
            transform: translateY(-10px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
        }

        /* PASTAS ATIVAS (COLORIDAS INTEIRAS) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-15px) !important; box-shadow: 0 10px 25px rgba(0, 191, 255, 0.4) !important; border: none !important; }
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-15px) !important; box-shadow: 0 10px 25px rgba(255, 105, 180, 0.4) !important; border: none !important; }
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-15px) !important; box-shadow: 0 10px 25px rgba(46, 204, 113, 0.4) !important; border: none !important; }

        /* =================================================================================
           3. ABAS INTERNAS (PASTINHAS QUE SE ELEVAM)
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 10px 35px 0 0 !important;
            border: 1px solid #ADB5BD !important;
            border-bottom: none !important;
            font-weight: 700;
            margin-right: 5px;
            transition: 0.3s;
        }
        
        /* ABA FILHA ATIVA */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-8px) !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-8px) !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-8px) !important; }

        /* =================================================================================
           4. OS ENVELOPES LINDINHOS DE ONTEM (RESTAURADOS) 📄
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 50px 30px 30px 30px !important;
            border-radius: 15px !important;
            border: 2px dashed #ADB5BD !important;
            background-color: #FFFFFF !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
            position: relative !important;
            margin: 25px 0 !important;
        }

        /* O ÍCONE NO TOPO DO ENVELOPE */
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 30px;
            z-index: 99;
        }

        /* CORES DOS ENVELOPES (SUAVES E LINDINHAS) */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border-color: #2ECC71 !important; }

        /* =================================================================================
           5. ACABAMENTOS FINAIS
        ================================================================================= */
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 0 30px 30px 30px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
            border-top: 10px solid #DEE2E6;
            box-shadow: 0 15px 40px rgba(0,0,0,0.05);
        }

        /* Varetas de cor */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #2ECC71 !important; }

        /* BOTÕES METALIZADOS */
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 12px !important;
            font-weight: 800 !important;
            text-transform: uppercase;
            transition: 0.3s;
        }
        div.stButton > button:hover, div.stDownloadButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        </style>
    """, unsafe_allow_html=True)
