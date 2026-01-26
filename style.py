import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO E CABEÇALHO */
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { transition: background 0.8s ease-in-out !important; }

        /* 2. MENU SUPERIOR (BOTÕES DE MÓDULO) - TEXTO EM CINZA CHUMBO POR PADRÃO */
        div.stButton > button {
            color: #6C757D !important; 
            background-color: #FFFFFF !important; 
            border: 1px solid #DEE2E6 !important;
            border-radius: 15px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            height: 75px !important;
            text-transform: uppercase;
            opacity: 0.8;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        /* 3. BLOCOS DE CORES POR ZONA (ACIONAMENTO) */

        /* --- 🟦 ZONA AZUL (GARIMPEIRO) --- */
        div:has(#modulo-xml) .stApp { background: radial-gradient(circle at top right, #D6F2FF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-xml) div.stHorizontalBlock > div:nth-child(1) button { 
            background: #00BFFF !important; 
            color: white !important; 
            opacity: 1 !important; 
            transform: scale(1.1) translateY(-5px) !important; 
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.6), 0 0 40px rgba(0, 191, 255, 0.4) !important; 
            border: 3px solid #FFFFFF !important; 
        }
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; }
        
        /* AJUSTE MESTRE: Botão Browse Files na Zona Azul (Fundo Azul + Borda Branca Neon) */
        div:has(#modulo-xml) [data-testid="stFileUploader"] section button {
            background-color: #00BFFF !important; 
            color: white !important; 
            border: 3px solid #FFFFFF !important; /* CONTORNO BRANCO NEON */
            font-weight: 700 !important;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.6), 0 0 25px rgba(0, 191, 255, 0.4) !important;
            transform: scale(1.02) !important;
        }
        div:has(#modulo-xml) [data-testid="stFileUploader"] svg { fill: #00BFFF !important; }
        div:has(#modulo-xml) [data-testid="stFileUploader"] section div div { color: #00BFFF !important; font-weight: 600; }

        /* --- 🟨 ZONA AMARELA (CONCILIADOR) --- */
        div:has(#modulo-amarelo) .stApp { background: radial-gradient(circle at top right, #FFF9C4 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-amarelo) div.stHorizontalBlock > div:nth-child(2) button { 
            background: #FFD700 !important; 
            color: #424242 !important; 
            opacity: 1 !important; 
            transform: scale(1.1) translateY(-5px) !important; 
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.8), 0 0 40px rgba(255, 215, 0, 0.5) !important; 
            border: 3px solid #FFFFFF !important; 
        }
        div:has(#modulo-amarelo) .stTabs [aria-selected="true"] { background: #FFD700 !important; color: #424242 !important; }

        /* --- 🟥 ZONA ROSA (AUDITOR) --- */
        div:has(#modulo-conformidade) .stApp { background: radial-gradient(circle at top right, #FFDEEF 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-conformidade) div.stHorizontalBlock > div:nth-child(3) button { 
            background: #FF69B4 !important; 
            color: white !important; 
            opacity: 1 !important; 
            transform: scale(1.1) translateY(-5px) !important; 
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.6), 0 0 40px rgba(255, 105, 180, 0.4) !important; 
            border: 3px solid #FFFFFF !important; 
        }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; }

        /* --- 🟩 ZONA VERDE (ESPELHO) --- */
        div:has(#modulo-apuracao) .stApp { background: radial-gradient(circle at top right, #DFFFEA 0%, #F8F9FA 100%) !important; }
        div:has(#modulo-apuracao) div.stHorizontalBlock > div:nth-child(4) button { 
            background: #2ECC71 !important; 
            color: white !important; 
            opacity: 1 !important; 
            transform: scale(1.1) translateY(-5px) !important; 
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.6), 0 0 40px rgba(46, 204, 113, 0.4) !important; 
            border: 3px solid #FFFFFF !important; 
        }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; }

        /* 4. REGRA GERAL UPLOADER (PADRÃO CINZA PARA OUTRAS ZONAS) */
        [data-testid="stFileUploader"] section button {
            background-color: #6C757D !important;
            color: white !important;
            border: none !important;
            box-shadow: none !important;
            transform: none !important;
        }
        [data-testid="stFileUploader"] section button:hover { background-color: #495057 !important; }
        [data-testid="stFileUploader"] svg { fill: #6C757D !important; }
        [data-testid="stFileUploader"] section div div { color: #6C757D !important; }

        /* 5. SIDEBAR - AJUSTE CINZA CHUMBO */
        [data-testid="stSidebar"] .stButton > button {
            color: #6C757D !important;
            background-color: transparent !important;
            border: 1px solid #CED4DA !important;
            height: auto !important;
            padding: 8px 15px !important;
            font-size: 14px !important;
            opacity: 1 !important;
        }

        /* 6. PAINÉIS E ABAS INTERNAS */
        [data-testid="stTabPanel"] {
            background: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(10px);
            border-radius: 25px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px 30px 0 0 !important;
            font-weight: 700;
            color: #ADB5BD !important;
            background: rgba(255,255,255,0.5) !important;
        }
        [data-testid="stFileUploader"] {
            border-radius: 20px !important;
            background: #FFFFFF !important;
            padding: 30px !important;
        }
        </style>
    """, unsafe_allow_html=True)
