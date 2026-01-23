import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDO SPACE GAMER PROFUNDO */
        [data-testid="stSidebar"] { background-color: #050A0E !important; border-right: 2px solid #1E262E !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        
        .stApp { 
            background: radial-gradient(circle at center, #10141B 0%, #010409 100%) !important; 
            color: #FFFFFF !important;
        }

        /* TÍTULO CYBERPUNK */
        .titulo-principal { 
            font-family: 'Orbitron', sans-serif !important; 
            color: #00D1FF !important; 
            font-size: 1rem !important; 
            font-weight: 900; 
            text-transform: uppercase; 
            letter-spacing: 5px;
            text-shadow: 0 0 10px #00D1FF, 0 0 20px #00D1FF;
            padding: 10px 0 !important;
        }

        /* =================================================================================
           2. MENU MASTER - BOTÕES TOTALMENTE COLORIDOS (NEON FILL)
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 15px; 
            padding-top: 30px !important; 
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Estilo Base Inativo (Vidro Fumê) */
        [role="radiogroup"] label {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 10px 30px 5px 30px !important; 
            padding: 15px 35px !important;
            min-width: 240px; 
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 700;
            color: #8B949E !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            text-align: center;
        }

        /* 🟦 XML - AZUL ELÉTRICO PREENCHIDO */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #00D1FF 0%, #004DFF 100%) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 0 35px rgba(0, 209, 255, 0.8), inset 0 0 15px rgba(255,255,255,0.4) !important;
            transform: translateY(-15px) scale(1.05);
        }

        /* 🟥 CONFORMIDADE - ROSA MAGENTA PREENCHIDO */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #FF00E5 0%, #7000FF 100%) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 0 35px rgba(255, 0, 229, 0.8), inset 0 0 15px rgba(255,255,255,0.4) !important;
            transform: translateY(-15px) scale(1.05);
        }

        /* 🟩 APURAÇÃO - VERDE TÓXICO PREENCHIDO */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #00FF94 0%, #008F53 100%) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 0 35px rgba(0, 255, 148, 0.8), inset 0 0 15px rgba(255,255,255,0.4) !important;
            transform: translateY(-15px) scale(1.05);
        }

        /* =================================================================================
           3. ABAS FILHAS - PASTINHAS QUE BRILHAM
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: rgba(255, 255, 255, 0.07) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px 30px 0 0 !important;
            color: #C9D1D9 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 700;
            margin-right: 10px;
        }

        /* Pintura das Abas Internas (Preenchimento) */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00D1FF !important; color: #000 !important; box-shadow: 0 0 20px #00D1FF; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF00E5 !important; color: #000 !important; box-shadow: 0 0 20px #FF00E5; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #00FF94 !important; color: #000 !important; box-shadow: 0 0 20px #00FF94; }

        /* =================================================================================
           4. ENVELOPE DE UPLOAD - EFEITO CRISTAL COLORIDO 📄
        ================================================================================= */
        [data-testid="stFileUploader"] {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 2px dashed rgba(255, 255, 255, 0.2) !important;
            border-radius: 20px !important;
            padding: 50px !important;
            position: relative !important;
            backdrop-filter: blur(10px);
        }

        [data-testid="stFileUploader"]::before {
            content: "🚀"; 
            position: absolute; top: -30px; left: 50%; transform: translateX(-50%);
            font-size: 45px; z-index: 99;
            animation: pulse 2s infinite;
        }
        @keyframes pulse { 0% { opacity: 0.7; transform: translateX(-50%) scale(1); } 50% { opacity: 1; transform: translateX(-50%) scale(1.1); } 100% { opacity: 0.7; transform: translateX(-50%) scale(1); } }

        /* Envelopes Coloridos por Dentro */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { background: rgba(0, 209, 255, 0.05) !important; border-color: #00D1FF !important; border-style: solid; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background: rgba(255, 0, 229, 0.05) !important; border-color: #FF00E5 !important; border-style: solid; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background: rgba(0, 255, 148, 0.05) !important; border-color: #00FF94 !important; border-style: solid; }

        /* =================================================================================
           5. CAIXOTÃO E BOTÕES SHINE
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: rgba(13, 17, 23, 0.8) !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0 25px 25px 25px !important;
            padding: 40px !important;
            border-top: 8px solid !important; /* Vareta colorida */
        }

        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00D1FF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF00E5 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #00FF94 !important; }

        /* Botões de Ação (Gamer Pro) */
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(135deg, #1E262E 0%, #0D1117 100%) !important;
            color: #FFFFFF !important;
            border: 2px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px !important;
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 800 !important;
            height: 55px;
            text-shadow: 0 0 5px rgba(255,255,255,0.5);
            transition: 0.3s;
        }
        div.stButton > button:hover {
            border-color: #FFFFFF !important;
            box-shadow: 0 0 20px rgba(255,255,255,0.2);
            transform: scale(1.02);
        }

        /* DOWNLOAD BUTTONS COLORIDOS */
        div.stDownloadButton > button { border-color: #00FF94 !important; color: #00FF94 !important; }

        </style>
    """, unsafe_allow_html=True)
