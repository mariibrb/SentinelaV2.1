import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Plus+Jakarta+Sans:wght@300;700&display=swap');

        /* 1. FUNDO SPACE GAMER */
        [data-testid="stSidebar"] { 
            background-color: #050A0E !important; 
            border-right: 2px solid #1E262E !important; 
        }
        header, [data-testid="stHeader"] { display: none !important; }
        
        .stApp { 
            background: radial-gradient(circle at center, #0D1117 0%, #010409 100%) !important; 
            color: #E6EDF3 !important;
        }

        /* TÍTULO CYBERPUNK MIÚDO */
        .titulo-principal { 
            font-family: 'Orbitron', sans-serif !important; 
            color: #00D1FF !important; 
            font-size: 1rem !important; 
            font-weight: 900; 
            text-transform: uppercase; 
            letter-spacing: 5px;
            text-shadow: 0 0 10px #00D1FF;
            padding: 10px 0 !important;
        }

        /* =================================================================================
           2. MENU MASTER - BOTÕES GAMER RGB
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 20px; 
            padding-top: 30px !important; 
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Botão Estado "Standby" (Inativo) */
        [role="radiogroup"] label {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 5px 25px 5px 25px !important; /* Corte Angular Gamer */
            padding: 12px 30px !important;
            min-width: 220px; 
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 700;
            color: #484F58 !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            backdrop-filter: blur(10px);
            text-transform: uppercase;
        }

        /* Hover com Glow */
        [role="radiogroup"] label:hover {
            border-color: rgba(255, 255, 255, 0.5) !important;
            color: white !important;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
            transform: translateY(-5px);
        }

        /* 🟦 MÓDULO XML - BLUE NEON */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #00D1FF 0%, #004DFF 100%) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 0 30px rgba(0, 209, 255, 0.6), inset 0 0 10px rgba(255,255,255,0.5) !important;
            transform: translateY(-10px) scale(1.05);
        }

        /* 🟥 MÓDULO CONFORMIDADE - PINK NEON */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #FF00E5 0%, #7000FF 100%) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 0 30px rgba(255, 0, 229, 0.6), inset 0 0 10px rgba(255,255,255,0.5) !important;
            transform: translateY(-10px) scale(1.05);
        }

        /* 🟩 MÓDULO APURAÇÃO - GREEN NEON */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #00FF94 0%, #008F53 100%) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 0 30px rgba(0, 255, 148, 0.6), inset 0 0 10px rgba(255,255,255,0.5) !important;
            transform: translateY(-10px) scale(1.05);
        }

        /* =================================================================================
           3. ABAS FILHAS - PASTINHAS SCI-FI
        ================================================================================= */
        .stTabs [data-baseweb="tab-list"] { background: transparent !important; gap: 10px; }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px 10px 0 0 !important;
            color: #8B949E !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 700;
        }

        /* Aba Interna Ativa - Brilhando conforme o módulo */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00D1FF !important; color: white !important; box-shadow: 0 -5px 15px rgba(0, 209, 255, 0.3); border: none !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF00E5 !important; color: white !important; box-shadow: 0 -5px 15px rgba(255, 0, 229, 0.3); border: none !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #00FF94 !important; color: white !important; box-shadow: 0 -5px 15px rgba(0, 255, 148, 0.3); border: none !important; }

        /* =================================================================================
           4. O ENVELOPE DE UPLOAD - DESIGN DE HARDWARE 🦾
        ================================================================================= */
        [data-testid="stFileUploader"] {
            background: rgba(13, 17, 23, 0.8) !important;
            border: 2px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 20px !important;
            padding: 50px !important;
            position: relative !important;
            box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
        }

        /* Holograma do Ícone */
        [data-testid="stFileUploader"]::before {
            content: "💿"; 
            position: absolute; top: -25px; left: 50%; transform: translateX(-50%);
            font-size: 40px; z-index: 99;
            filter: drop-shadow(0 0 10px rgba(0, 209, 255, 0.8));
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float { 0% { transform: translate(-50%, 0px); } 50% { transform: translate(-50%, -10px); } 100% { transform: translate(-50%, 0px); } }

        /* Cores Neon nos Envelopes */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00D1FF !important; box-shadow: 0 0 20px rgba(0, 209, 255, 0.15); }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF00E5 !important; box-shadow: 0 0 20px rgba(255, 0, 229, 0.15); }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #00FF94 !important; box-shadow: 0 0 20px rgba(0, 255, 148, 0.15); }

        /* =================================================================================
           5. CAIXOTÃO E BOTÕES
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: rgba(13, 17, 23, 0.6) !important;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0 20px 20px 20px !important;
            padding: 40px !important;
            border-top: 5px solid rgba(255,255,255,0.1);
        }

        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00D1FF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF00E5 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #00FF94 !important; }

        /* Botões Gamer */
        div.stButton > button, div.stDownloadButton > button {
            background: #161B22 !important;
            color: white !important;
            border: 1px solid #30363D !important;
            border-radius: 8px !important;
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 800 !important;
            height: 50px;
            transition: 0.2s;
        }
        div.stButton > button:hover {
            background: #21262D !important;
            border-color: #8B949E !important;
            box-shadow: 0 0 15px rgba(255,255,255,0.1);
        }

        </style>
    """, unsafe_allow_html=True)
