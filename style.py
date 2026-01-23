import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* 1. FUNDAÇÃO - O RADIAL GRADIENT DA RIHANNA */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important; 
            color: #495057 !important; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase; 
            padding: 20px 0 !important; 
            text-shadow: 1px 1px 10px rgba(255, 255, 255, 0.9) !important; 
        }

        /* =================================================================================
           2. MENU MASTER NO TOPO (BOTÕES METALIZADOS GAMER)
        ================================================================================= */
        [role="radiogroup"] {
            display: flex;
            justify-content: center;
            gap: 25px;
            background: transparent;
            margin-bottom: 40px;
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* O BOTÃO METALIZADO (INATIVO) */
        [role="radiogroup"] label {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 20px !important;
            padding: 18px 40px !important;
            min-width: 250px;
            text-align: center;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            color: #495057 !important;
            cursor: pointer !important;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            display: flex; justify-content: center;
        }

        /* HOVER COM BRILHO DIAMANTE */
        [role="radiogroup"] label:hover {
            transform: translateY(-8px);
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2) !important;
        }

        /* --- BOTÕES ATIVOS (ACENDEM O NEON GAMER) --- */

        /* 🟦 XML NEON */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: #FFFFFF !important;
            border: 3px solid #00BFFF !important;
            color: #00BFFF !important;
            box-shadow: 0 0 30px rgba(0, 191, 255, 0.6), inset 0 0 10px rgba(0, 191, 255, 0.2) !important;
            transform: scale(1.1);
        }

        /* 🟥 CONFORMIDADE NEON */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: #FFFFFF !important;
            border: 3px solid #FF69B4 !important;
            color: #FF69B4 !important;
            box-shadow: 0 0 30px rgba(255, 105, 180, 0.6), inset 0 0 10px rgba(255, 105, 180, 0.2) !important;
            transform: scale(1.1);
        }

        /* 🟩 APURAÇÃO NEON */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: #FFFFFF !important;
            border: 3px solid #2ECC71 !important;
            color: #2ECC71 !important;
            box-shadow: 0 0 30px rgba(46, 204, 113, 0.6), inset 0 0 10px rgba(46, 204, 113, 0.2) !important;
            transform: scale(1.1);
        }

        /* =================================================================================
           3. PASTAS INTERNAS (O VISUAL DIAMANTE 💎)
        ================================================================================= */
        .stTabs [data-baseweb="tab-list"] { gap: 12px; border-bottom: none; padding-top: 20px; }

        .stTabs [data-baseweb="tab"] {
            height: 75px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #CED4DA 100%) !important;
            border-radius: 25px 60px 0 0 !important; /* CURVA SEXY RIHANNA */
            padding: 0px 50px !important;
            border: 2px solid #ADB5BD !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 800 !important;
            color: #6C757D !important;
            margin-right: 5px !important;
            transition: all 0.3s ease !important;
        }

        .stTabs [aria-selected="true"] {
            height: 85px !important;
            background: #FFFFFF !important;
            color: #212529 !important;
            border-top-width: 6px !important;
            transform: translateY(-8px) !important;
            box-shadow: 0 -10px 20px rgba(0,0,0,0.1) !important;
            z-index: 10;
        }

        /* CORES DAS PASTAS POR MÓDULO */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { border-top-color: #2ECC71 !important; }

        /* =================================================================================
           4. OS ENVELOPES BONITINHOS (VOLTARAM!) 📄
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 55px 40px 40px 40px !important;
            border-radius: 20px !important;
            margin: 30px 0 !important;
            position: relative !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #F8F9FA 100%) !important;
            border: 2px dashed #ADB5BD !important;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1) !important;
            transition: all 0.3s ease;
        }

        /* O ÍCONE DO ENVELOPE */
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 35px;
            z-index: 99;
            filter: drop-shadow(0 5px 5px rgba(0,0,0,0.1));
        }

        /* ENVELOPES COLORIDOS (MODO GAMER) */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; background-color: #F0F8FF !important; border-style: solid !important; border-top: 15px solid #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; background-color: #FFF0F5 !important; border-style: solid !important; border-top: 15px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #2ECC71 !important; background-color: #F0FFF4 !important; border-style: solid !important; border-top: 15px solid #2ECC71 !important; }

        /* =================================================================================
           5. CAIXOTÃO E BOTÕES
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border: 2px solid #DEE2E6;
            border-top: none; 
            border-radius: 0 30px 30px 30px !important;
            padding: 50px !important;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
            margin-top: -5px;
        }

        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* BOTÕES SHINE BRIGHT (SEM VERMELHO) */
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 15px !important;
            font-weight: 800 !important;
            text-transform: uppercase;
            height: 55px;
            width: 100%;
            transition: 0.3s;
        }
        
        div.stDownloadButton > button:hover { 
            transform: scale(1.02);
            color: white !important;
            background: #212529 !important;
        }

        </style>
    """, unsafe_allow_html=True)
