import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;900&family=Plus+Jakarta+Sans:wght@400;800&display=swap');

        /* 1. LIMPEZA GERAL */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: #F8F9FA !important; }

        /* 2. MENU MASTER - FORÇANDO A PINTURA NAS ABAS */
        [role="radiogroup"] { 
            display: flex !important; 
            justify-content: center !important; 
            gap: 20px !important; 
            padding: 40px 0 !important;
        }
        
        /* Mata a bolinha e o fundo padrão do Streamlit */
        [role="radiogroup"] label div[data-testid="stMarkdownContainer"] { color: inherit !important; }
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Estilo Base da Aba (Desligada) */
        [role="radiogroup"] label {
            background-color: #FFFFFF !important;
            border: 2px solid #DEE2E6 !important;
            border-radius: 15px 45px 0 0 !important; 
            padding: 15px 40px !important;
            min-width: 250px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600 !important;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            text-align: center !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
            display: block !important;
        }

        /* --- O BALDE DE TINTA (PINTURA TOTAL) --- */

        /* 🟦 AZUL (ANÁLISE XML) - SELECIONADO */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background-color: #00BFFF !important;
            background: #00BFFF !important;
            color: #FFFFFF !important;
            border: none !important;
            transform: translateY(-12px) !important;
            box-shadow: 0 10px 30px rgba(0, 191, 255, 0.7) !important;
        }

        /* 🟥 ROSA (CONFORMIDADE) - SELECIONADO */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background-color: #FF69B4 !important;
            background: #FF69B4 !important;
            color: #FFFFFF !important;
            border: none !important;
            transform: translateY(-12px) !important;
            box-shadow: 0 10px 30px rgba(255, 105, 180, 0.7) !important;
        }

        /* 🟩 VERDE (APURAÇÃO) - SELECIONADO */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background-color: #2ECC71 !important;
            background: #2ECC71 !important;
            color: #FFFFFF !important;
            border: none !important;
            transform: translateY(-12px) !important;
            box-shadow: 0 10px 30px rgba(46, 204, 113, 0.7) !important;
        }

        /* 3. PAINEL E ENVELOPES */
        [data-testid="stTabPanel"] {
            background-color: #FFFFFF !important;
            border-radius: 0 30px 30px 30px !important;
            padding: 40px !important;
            border: 2px solid #DEE2E6 !important;
            margin-top: -2px !important;
        }

        /* Vareta colorida no topo do painel */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top: 12px solid #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top: 12px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top: 12px solid #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
