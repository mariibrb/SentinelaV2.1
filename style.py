import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO CHUMBO CLARO/PRATEADO */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #DEE2E6 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #6C757D !important; font-size: 0.9rem !important; font-weight: 800; text-transform: uppercase; padding: 5px 0 !important; letter-spacing: 2px; }

        /* =================================================================================
           2. MENU MASTER - ABAS COM FLAG DE LED (BOLINHA INTERNA)
        ================================================================================= */
        [role="radiogroup"] { display: flex; justify-content: center; gap: 12px; padding-top: 30px !important; overflow: visible !important; }
        
        /* Remove a bolinha original do Streamlit */
        [role="radiogroup"] label > div:first-child { display: none !important; }

        [role="radiogroup"] label {
            background: linear-gradient(180deg, #FFFFFF 0%, #CED4DA 100%) !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 12px 35px 0 0 !important; 
            padding: 12px 25px !important;
            min-width: 200px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.3s ease;
            text-align: center;
            display: flex; align-items: center; justify-content: center; gap: 10px;
        }

        /* --- CRIAÇÃO DO FLAG (BOLINHA DE LED) --- */
        [role="radiogroup"] label::before {
            content: "";
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #ADB5BD; /* Cor desligada */
            transition: 0.3s;
        }

        /* ELEVAÇÃO E BRILHO NO SELECIONADO */
        [role="radiogroup"] label[data-checked="true"] {
            transform: translateY(-10px) !important;
            background: #FFFFFF !important;
            color: #212529 !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
            border-bottom: none !important;
        }

        /* --- PINTANDO O LED POR MÓDULO --- */

        /* 🟦 LED AZUL (XML) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"]::before {
            background: #00BFFF !important;
            box-shadow: 0 0 10px #00BFFF, 0 0 20px #00BFFF !important;
        }
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] { border-top: 4px solid #00BFFF !important; }

        /* 🟥 LED ROSA (CONFORMIDADE) */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"]::before {
            background: #FF69B4 !important;
            box-shadow: 0 0 10px #FF69B4, 0 0 20px #FF69B4 !important;
        }
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] { border-top: 4px solid #FF69B4 !important; }

        /* 🟩 LED VERDE (APURAÇÃO) */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"]::before {
            background: #2ECC71 !important;
            box-shadow: 0 0 10px #2ECC71, 0 0 20px #2ECC71 !important;
        }
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] { border-top: 4px solid #2ECC71 !important; }

        /* =================================================================================
           3. RESTANTE DO VISUAL (ENVELOPES E PAINEL)
        ================================================================================= */
        .stTabs [data-baseweb="tab"] { border-radius: 8px 25px 0 0 !important; font-weight: 700; margin-right: 5px; }
        
        /* Envelopes Lindinhos Restaurados */
        [data-testid="stFileUploader"] {
            padding: 45px 25px 25px 25px !important;
            border-radius: 15px !important;
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            position: relative !important;
            margin: 20px 0 !important;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -22px; left: 50%; transform: translateX(-50%); font-size: 32px; z-index: 99; }

        div:has(#modulo-xml) [data-testid="stFileUploader"] { background: #EBF9FF !important; border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background: #FFF0F5 !important; border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background: #F1FFF7 !important; border-color: #2ECC71 !important; }

        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 0 15px 15px 15px !important;
            padding: 30px !important;
            border: 1px solid #DEE2E6;
            border-top: 8px solid #DEE2E6;
        }
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
