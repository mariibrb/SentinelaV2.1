import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;900&family=Plus+Jakarta+Sans:wght@400;800&display=swap');

        /* 1. FUNDAÇÃO E CLIMA */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.5s ease; }

        /* Clima por módulo - Agora mais visível no fundo */
        div:has(#modulo-xml) .stApp { background-color: #E6F7FF !important; }
        div:has(#modulo-conformidade) .stApp { background-color: #FFF0F6 !important; }
        div:has(#modulo-apuracao) .stApp { background-color: #F6FFED !important; }

        /* =================================================================================
           2. MENU MASTER - ADEUS CINZA MUCHO!
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 20px; 
            padding: 40px 0 !important;
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Estilo Inativo (O cinza que vai sumir no clique) */
        [role="radiogroup"] label {
            background: #FFFFFF !important;
            border: 2px solid #DEE2E6 !important;
            border-radius: 15px !important; 
            padding: 18px 40px !important;
            min-width: 280px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        /* --- O NEON QUE VOCÊ QUERIA (FORÇANDO A COR) --- */

        /* AZUL XML */
        div:has(#modulo-xml) [role="radiogroup"] [data-testid="stWidgetLabel"] + div label[data-checked="true"],
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #00BFFF 0%, #0072FF 100%) !important;
            color: white !important;
            font-weight: 900 !important;
            transform: scale(1.08) translateY(-5px) !important;
            box-shadow: 0 10px 30px rgba(0, 191, 255, 0.6) !important;
            border: none !important;
        }

        /* ROSA CONFORMIDADE */
        div:has(#modulo-conformidade) [role="radiogroup"] [data-testid="stWidgetLabel"] + div label[data-checked="true"],
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%) !important;
            color: white !important;
            font-weight: 900 !important;
            transform: scale(1.08) translateY(-5px) !important;
            box-shadow: 0 10px 30px rgba(255, 105, 180, 0.6) !important;
            border: none !important;
        }

        /* VERDE APURAÇÃO */
        div:has(#modulo-apuracao) [role="radiogroup"] [data-testid="stWidgetLabel"] + div label[data-checked="true"],
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%) !important;
            color: white !important;
            font-weight: 900 !important;
            transform: scale(1.08) translateY(-5px) !important;
            box-shadow: 0 10px 30px rgba(46, 204, 113, 0.6) !important;
            border: none !important;
        }

        /* 3. ÁREA DE TRABALHO */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 35px !important;
            padding: 40px !important;
            border: 3px solid #DEE2E6;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        }

        </style>
    """, unsafe_allow_html=True)
