import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;900&family=Plus+Jakarta+Sans:wght@400;800&display=swap');

        /* 1. FUNDAÇÃO E CLIMA */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.5s ease; }

        /* Cores de fundo mais presentes para contraste */
        div:has(#modulo-xml) .stApp { background: #E6F7FF !important; }
        div:has(#modulo-conformidade) .stApp { background: #FFF0F6 !important; }
        div:has(#modulo-apuracao) .stApp { background: #F6FFED !important; }

        /* =================================================================================
           2. MENU MASTER - BOTÕES VIBRANTES (NEON MODE)
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 20px; 
            padding: 50px 0 !important;
            overflow: visible !important;
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Estilo Inativo (O "xoxinho" que fica apagado) */
        [role="radiogroup"] label {
            background: #FFFFFF !important;
            border: 2px solid #CED4DA !important;
            border-radius: 12px !important; 
            padding: 20px 40px !important;
            min-width: 280px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600;
            color: #ADB5BD !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            opacity: 0.7;
        }

        /* --- O PULO DO GATO: BOTÃO ATIVO VIBRANTE --- */
        [role="radiogroup"] label[data-checked="true"] {
            opacity: 1 !important;
            color: white !important;
            font-weight: 900 !important;
            transform: scale(1.1) translateY(-10px) !important; /* Eleva e aumenta */
            z-index: 99;
        }

        /* 🟦 XML NEON */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #00BFFF 0%, #0072FF 100%) !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(0, 191, 255, 0.6), 0 0 10px rgba(0, 191, 255, 0.3) !important;
        }

        /* 🟥 CONFORMIDADE NEON */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%) !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(255, 105, 180, 0.6), 0 0 10px rgba(255, 105, 180, 0.3) !important;
        }

        /* 🟩 APURAÇÃO NEON */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%) !important;
            border: none !important;
            box-shadow: 0 15px 35px rgba(46, 204, 113, 0.6), 0 0 10px rgba(46, 204, 113, 0.3) !important;
        }

        /* Seta Indicadora Vibrante */
        [role="radiogroup"] label[data-checked="true"]::after {
            content: "▲";
            position: absolute;
            bottom: -50px;
            left: 50%;
            transform: translateX(-50%) rotate(180deg);
            font-size: 30px;
            text-shadow: 0 0 15px currentColor;
            animation: bounce 1s infinite;
        }
        
        @keyframes bounce { 0%, 100% { transform: translateX(-50%) rotate(180deg) translateY(0); } 50% { transform: translateX(-50%) rotate(180deg) translateY(10px); } }

        /* =================================================================================
           3. ÁREA DE TRABALHO E ENVELOPES
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 50px !important;
            border: 4px solid #DEE2E6;
            box-shadow: 0 40px 80px rgba(0,0,0,0.1);
        }

        /* Envelopes Vibrantes */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border: 4px solid #00BFFF !important; box-shadow: 0 0 20px rgba(0, 191, 255, 0.2) !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border: 4px solid #FF69B4 !important; box-shadow: 0 0 20px rgba(255, 105, 180, 0.2) !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border: 4px solid #2ECC71 !important; box-shadow: 0 0 20px rgba(46, 204, 113, 0.2) !important; }

        </style>
    """, unsafe_allow_html=True)
