import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO COM CLIMA REATIVO */
        [data-testid="stSidebar"] { background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        
        /* Fundo base */
        .stApp { transition: background 0.5s ease; }

        /* MUDANÇA DE CLIMA POR MÓDULO (O segredo da separação) */
        div:has(#modulo-xml) .stApp { background: radial-gradient(circle at top right, #EBF9FF 0%, #DEE2E6 100%) !important; }
        div:has(#modulo-conformidade) .stApp { background: radial-gradient(circle at top right, #FFF0F5 0%, #DEE2E6 100%) !important; }
        div:has(#modulo-apuracao) .stApp { background: radial-gradient(circle at top right, #F1FFF7 0%, #DEE2E6 100%) !important; }

        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #6C757D !important; font-size: 0.9rem !important; font-weight: 800; text-transform: uppercase; padding: 5px 0 !important; letter-spacing: 2px; }

        /* =================================================================================
           2. MENU MASTER - ESTILO "FLUXO DE TRABALHO"
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 20px; 
            padding: 30px 10px !important; 
            background: rgba(255,255,255,0.3);
            border-radius: 20px;
            margin: 20px 0;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        [role="radiogroup"] label {
            background: #FFFFFF !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 15px !important; 
            padding: 15px 30px !important;
            min-width: 250px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800;
            color: #ADB5BD !important;
            cursor: pointer !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-align: center;
            box-shadow: 0 4px 0px #ADB5BD; /* Efeito 3D de botão */
        }

        /* ESTADOS ATIVOS COM IDENTIFICAÇÃO ABSOLUTA */
        
        /* 🟦 AZUL (XML) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: #00BFFF !important;
            color: white !important;
            border-color: #0088CC !important;
            box-shadow: 0 0 20px rgba(0, 191, 255, 0.4), 0 6px 0px #0088CC !important;
            transform: translateY(-5px);
        }

        /* 🟥 ROSA (CONFORMIDADE) */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: #FF69B4 !important;
            color: white !important;
            border-color: #D6458F !important;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.4), 0 6px 0px #D6458F !important;
            transform: translateY(-5px);
        }

        /* 🟩 VERDE (APURAÇÃO) */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: #2ECC71 !important;
            color: white !important;
            border-color: #27AE60 !important;
            box-shadow: 0 0 20px rgba(46, 204, 113, 0.4), 0 6px 0px #27AE60 !important;
            transform: translateY(-5px);
        }

        /* =================================================================================
           3. BANNER DE STATUS (A BÚSSOLA)
        ================================================================================= */
        [data-testid="stTabPanel"]::before {
            display: block;
            text-align: center;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 10px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 800;
            font-size: 1.2rem;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        div:has(#modulo-xml) [data-testid="stTabPanel"]::before { 
            content: "🚀 MODO: GARIMPO E ANÁLISE DE XML"; 
            color: #00BFFF; background: rgba(0, 191, 255, 0.1); border: 1px solid #00BFFF;
        }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"]::before { 
            content: "🏢 MODO: CONFORMIDADE E RELATÓRIOS"; 
            color: #FF69B4; background: rgba(255, 105, 180, 0.1); border: 1px solid #FF69B4;
        }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"]::before { 
            content: "✅ MODO: APURAÇÃO FINAL DE TRIBUTOS"; 
            color: #2ECC71; background: rgba(46, 204, 113, 0.1); border: 1px solid #2ECC71;
        }

        /* 4. ENVELOPES E PAINEL */
        .stTabs [data-baseweb="tab"] { border-radius: 8px 25px 0 0 !important; font-weight: 700; margin-right: 5px; }
        
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 20px !important;
            padding: 40px !important;
            border: 2px solid #DEE2E6;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        }

        /* Envelopes Reativos */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { background: #F0F9FF !important; border: 2px solid #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background: #FFF5F9 !important; border: 2px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background: #F5FFF9 !important; border: 2px solid #2ECC71 !important; }

        </style>
    """, unsafe_allow_html=True)
