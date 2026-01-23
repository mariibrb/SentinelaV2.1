import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO RIHANNA COM BRILHO RADIAL */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #FFFFFF 0%, #DEE2E6 100%) !important; }
        
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important; 
            color: #495057 !important; 
            font-size: 3.5rem; 
            font-weight: 800; 
            text-transform: uppercase; 
            text-shadow: 0 0 15px rgba(255, 255, 255, 1), 2px 2px 5px rgba(0,0,0,0.1) !important; 
        }

        /* =================================================================================
           2. MENU MASTER (PASTAS COM GLITTER E ELEVAÇÃO)
        ================================================================================= */
        [role="radiogroup"] { display: flex; justify-content: center; gap: 15px; margin-bottom: 30px; }
        [role="radiogroup"] label > div:first-child { display: none !important; }

        [role="radiogroup"] label {
            background: linear-gradient(135deg, #FFFFFF 0%, #E9ECEF 50%, #CFD4D9 100%) !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 15px 50px 0 0 !important; 
            padding: 15px 30px !important;
            min-width: 230px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        /* ✨ EFEITO GLITTER / SHINE BRIGHT NO HOVER ✨ */
        [role="radiogroup"] label:hover {
            transform: translateY(-12px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 20%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 80%), 
                        radial-gradient(circle, rgba(255,255,255,0.2) 0%, rgba(0,0,0,0) 100%),
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoDiamond 1.5s infinite linear !important;
            color: #212529 !important;
        }

        @keyframes brilhoDiamond { 
            0% { background-position: 200% 0; } 
            100% { background-position: -200% 0; } 
        }

        /* 🟦 SELEÇÃO AZUL NEON (INTEIRA) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #00BFFF 0%, #0072FF 100%) !important;
            color: white !important;
            border: none !important;
            transform: translateY(-18px) scale(1.05) !important;
            box-shadow: 0 15px 35px rgba(0, 191, 255, 0.6) !important;
        }

        /* 🟥 SELEÇÃO ROSA GLAMOUR (INTEIRA) */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%) !important;
            color: white !important;
            border: none !important;
            transform: translateY(-18px) scale(1.05) !important;
            box-shadow: 0 15px 35px rgba(255, 20, 147, 0.6) !important;
        }

        /* 🟩 SELEÇÃO VERDE GAMER (INTEIRA) */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%) !important;
            color: white !important;
            border: none !important;
            transform: translateY(-18px) scale(1.05) !important;
            box-shadow: 0 15px 35px rgba(46, 204, 113, 0.6) !important;
        }

        /* =================================================================================
           3. ABAS INTERNAS (COLORIDAS E BRILHANTES)
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 12px 40px 0 0 !important;
            border: 1px solid #ADB5BD !important;
            font-weight: 700;
            color: #6C757D !important;
            margin-right: 8px;
            transition: 0.3s ease;
        }

        /* ABA ATIVA (COR SÓLIDA E BRILHANTE) */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-8px); box-shadow: 0 5px 15px rgba(0,191,255,0.3); }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-8px); box-shadow: 0 5px 15px rgba(255,105,180,0.3); }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-8px); box-shadow: 0 5px 15px rgba(46,204,113,0.3); }

        /* =================================================================================
           4. O ENVELOPE MÁGICO (STAYING SHINY) 📄
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 55px 35px 35px 35px !important;
            border-radius: 20px !important;
            border: 2px dashed #ADB5BD !important;
            background: #FFFFFF !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.08) !important;
            position: relative !important;
            margin: 30px 0 !important;
        }

        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute; top: -30px; left: 50%; transform: translateX(-50%);
            font-size: 38px; z-index: 99;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
        }

        /* Degradês Suaves nos Envelopes */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { background: linear-gradient(180deg, #EBF9FF 0%, #FFFFFF 100%) !important; border-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%) !important; border-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { background: linear-gradient(180deg, #F1FFF7 0%, #FFFFFF 100%) !important; border-color: #2ECC71 !important; }

        /* =================================================================================
           5. CAIXOTÃO E BOTÕES SHINE
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 0 30px 30px 30px !important;
            padding: 45px !important;
            border: 1px solid #DEE2E6;
            box-shadow: 0 20px 50px rgba(0,0,0,0.05);
            border-top: 10px solid #DEE2E6;
        }

        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #2ECC71 !important; }

        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 12px !important;
            font-weight: 800 !important;
            text-transform: uppercase;
            transition: 0.3s;
            border: 1px solid #ADB5BD;
        }
        div.stButton > button:hover { 
            transform: scale(1.03); 
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            background: linear-gradient(45deg, #FFFFFF, #E9ECEF) !important;
        }

        </style>
    """, unsafe_allow_html=True)
