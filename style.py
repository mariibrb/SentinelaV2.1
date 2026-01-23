import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #DEE2E6 100%) !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #6C757D !important; font-size: 1rem !important; font-weight: 800; text-transform: uppercase; padding: 5px 0 !important; letter-spacing: 2px; }

        /* =================================================================================
           2. MENU MASTER - PINTANDO AS ABAS POR INTEIRO (AGORA VOCÊ VAI ENXERGAR!)
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 15px; 
            padding-top: 40px !important; 
            overflow: visible !important;
        }
        
        /* Mata a bolinha original */
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Estilo Base da Aba (Desligada) */
        [role="radiogroup"] label {
            background: linear-gradient(180deg, #FFFFFF 0%, #CED4DA 100%) !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 15px 45px 0 0 !important; 
            padding: 12px 35px !important;
            min-width: 220px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            text-align: center;
        }

        /* ✨ BRILHO NO HOVER ✨ */
        [role="radiogroup"] label:hover {
            transform: translateY(-8px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 20%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 80%), linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoDiamond 1.5s infinite linear !important;
        }

        /* 🟦 AZUL (ANÁLISE XML) - QUANDO SELECIONADO */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: #00BFFF !important; /* COR SÓLIDA */
            color: white !important;
            transform: translateY(-20px) !important;
            box-shadow: 0 10px 25px rgba(0, 191, 255, 0.5) !important;
            border: none !important;
        }

        /* 🟥 ROSA (CONFORMIDADE) - QUANDO SELECIONADO */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: #FF69B4 !important; /* COR SÓLIDA */
            color: white !important;
            transform: translateY(-20px) !important;
            box-shadow: 0 10px 25px rgba(255, 105, 180, 0.5) !important;
            border: none !important;
        }

        /* 🟩 VERDE (APURAÇÃO) - QUANDO SELECIONADO */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: #2ECC71 !important; /* COR SÓLIDA */
            color: white !important;
            transform: translateY(-20px) !important;
            box-shadow: 0 10px 25px rgba(46, 204, 113, 0.5) !important;
            border: none !important;
        }

        /* =================================================================================
           3. ABAS FILHAS (AS DE DENTRO)
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 48px !important;
            background: #F1F3F5 !important;
            border-radius: 8px 25px 0 0 !important;
            padding: 0 20px !important;
            font-weight: 700;
            margin-right: 5px;
            color: #6C757D !important;
            transition: 0.3s;
        }
        
        /* Cor das pastinhas de dentro conforme o módulo */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-5px); }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-5px); }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-5px); }

        /* =================================================================================
           4. ENVELOPES LINDINHOS 📄
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 50px 30px 30px 30px !important;
            border-radius: 20px !important;
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            box-shadow: 0 15px 35px rgba(0,0,0,0.06) !important;
            position: relative !important;
            margin: 30px 0 !important;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -25px; left: 50%; transform: translateX(-50%); font-size: 35px; z-index: 99; }

        div:has(#modulo-xml) [data-testid="stFileUploader"] { background: linear-gradient(180deg, #EBF9FF 0%, #FFFFFF 100%) !important; border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%) !important; border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background: linear-gradient(180deg, #F1FFF7 0%, #FFFFFF 100%) !important; border-color: #2ECC71 !important; }

        /* 5. PAINEL */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 0 20px 20px 20px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
            border-top: 10px solid #DEE2E6;
        }
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #2ECC71 !important; }

        @keyframes brilhoDiamond { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
        
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            font-weight: 800 !important;
            text-transform: uppercase;
        }

        </style>
    """, unsafe_allow_html=True)
