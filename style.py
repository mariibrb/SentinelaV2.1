import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO E CLIMA */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.5s ease; }

        div:has(#modulo-xml) .stApp { background: #F0F9FF !important; }
        div:has(#modulo-conformidade) .stApp { background: #FFF5F9 !important; }
        div:has(#modulo-apuracao) .stApp { background: #F5FFF9 !important; }

        /* =================================================================================
           2. MENU MASTER - BOTÕES QUE "AFUNDAM" E INDICAM O MÓDULO
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 25px; 
            padding: 40px 0 !important;
            overflow: visible !important;
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Estilo do Botão NÃO Selecionado (Fica "apagado" e flutuando) */
        [role="radiogroup"] label {
            background: #FFFFFF !important;
            border: 2px solid #DEE2E6 !important;
            border-radius: 15px !important; 
            padding: 15px 35px !important;
            min-width: 260px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 400;
            color: #ADB5BD !important;
            cursor: pointer !important;
            transition: all 0.2s ease-in-out;
            text-align: center;
            opacity: 0.6;
            box-shadow: 0 10px 15px rgba(0,0,0,0.05);
        }

        /* --- ESTADO ATIVO (QUANDO VOCÊ CLICA) --- */
        [role="radiogroup"] label[data-checked="true"] {
            opacity: 1 !important;
            font-weight: 800 !important;
            transform: scale(0.95) translateY(5px) !important; /* Efeito de botão apertado */
            box-shadow: inset 0 5px 10px rgba(0,0,0,0.2) !important;
            position: relative;
        }

        /* Seta indicadora embaixo do botão ativo */
        [role="radiogroup"] label[data-checked="true"]::after {
            content: "▼";
            position: absolute;
            bottom: -35px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 25px;
            animation: bounce 1s infinite;
        }

        @keyframes bounce { 0%, 100% { bottom: -35px; } 50% { bottom: -45px; } }

        /* 🟦 SELEÇÃO XML */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: #00BFFF !important;
            color: white !important;
            border: 4px solid #0088CC !important;
        }
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"]::after { color: #00BFFF; }

        /* 🟥 SELEÇÃO CONFORMIDADE */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: #FF69B4 !important;
            color: white !important;
            border: 4px solid #D6458F !important;
        }
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"]::after { color: #FF69B4; }

        /* 🟩 SELEÇÃO APURAÇÃO */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: #2ECC71 !important;
            color: white !important;
            border: 4px solid #27AE60 !important;
        }
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"]::after { color: #2ECC71; }

        /* =================================================================================
           3. ÁREA DE TRABALHO
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 30px !important;
            padding: 50px !important;
            border: 3px solid #DEE2E6;
            box-shadow: 0 30px 60px rgba(0,0,0,0.1);
            margin-top: 20px;
        }

        /* Envelopes Reativos Fortes */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border: 3px solid #00BFFF !important; background: rgba(0, 191, 255, 0.05) !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border: 3px solid #FF69B4 !important; background: rgba(255, 105, 180, 0.05) !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border: 3px solid #2ECC71 !important; background: rgba(46, 204, 113, 0.05) !important; }

        </style>
    """, unsafe_allow_html=True)
