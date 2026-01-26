import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;900&family=Plus+Jakarta+Sans:wght@400;800&display=swap');

        /* 1. FUNDAÇÃO E ESCONDER O PADRÃO */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.5s ease; }

        /* 2. MENU MASTER - O FIM DO CINZA BOROCOXÔ */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 20px; 
            padding: 40px 0 !important;
        }
        
        /* Esconde o círculo original do rádio */
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Estilo da Aba (Inativa) */
        [role="radiogroup"] label {
            background: #FFFFFF !important;
            border: 2px solid #DEE2E6 !important;
            border-radius: 15px 45px 0 0 !important; 
            padding: 15px 40px !important;
            min-width: 250px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.3s ease;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        /* --- PINTURA TOTAL E SOMBREADO BONITO (ATIVO) --- */

        /* 🟦 XML (AZUL) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: #00BFFF !important;
            color: white !important;
            border: none !important;
            transform: translateY(-10px) !important;
            box-shadow: 0 10px 30px rgba(0, 191, 255, 0.6) !important; /* SOMBREADO GLOW */
        }

        /* 🟥 CONFORMIDADE (ROSA) */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: #FF69B4 !important;
            color: white !important;
            border: none !important;
            transform: translateY(-10px) !important;
            box-shadow: 0 10px 30px rgba(255, 105, 180, 0.6) !important; /* SOMBREADO GLOW */
        }

        /* 🟩 APURAÇÃO (VERDE) */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: #2ECC71 !important;
            color: white !important;
            border: none !important;
            transform: translateY(-10px) !important;
            box-shadow: 0 10px 30px rgba(46, 204, 113, 0.6) !important; /* SOMBREADO GLOW */
        }

        /* 3. PAINEL E ENVELOPES */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 0 30px 30px 30px !important;
            padding: 40px !important;
            border: 2px solid #DEE2E6;
            margin-top: -2px;
        }

        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top: 10px solid #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top: 10px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top: 10px solid #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
