import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');

        /* 1. FUNDAÇÃO RIHANNA */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #ADB5BD !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; text-shadow: 1px 1px 10px rgba(255, 255, 255, 0.9) !important; }

        /* =================================================================================
           2. MENU MASTER (AS PASTAS QUE SE ELEVAM)
        ================================================================================= */
        [role="radiogroup"] { display: flex; justify-content: center; gap: 15px; margin-bottom: 20px; }
        [role="radiogroup"] label > div:first-child { display: none !important; }

        [role="radiogroup"] label {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 15px 50px 0 0 !important; 
            padding: 15px 30px !important;
            min-width: 220px;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800;
            color: #6C757D !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }

        /* EFEITO SHINE AO PASSAR O MOUSE */
        [role="radiogroup"] label:hover {
            transform: translateY(-10px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
        }

        /* ABA ATIVA (COLORIDA E ALTA) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-15px) !important; border: none !important; box-shadow: 0 10px 20px rgba(0, 191, 255, 0.3) !important; }
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-15px) !important; border: none !important; box-shadow: 0 10px 20px rgba(255, 105, 180, 0.3) !important; }
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-15px) !important; border: none !important; box-shadow: 0 10px 20px rgba(46, 204, 113, 0.3) !important; }

        /* =================================================================================
           3. O ENVELOPE QUE VOCÊ AMOU (RESTAURADO) 📄
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 55px 35px 35px 35px !important;
            border-radius: 20px !important;
            border: 2px dashed #ADB5BD !important;
            background-color: #FFFFFF !important;
            box-shadow: 0 15px 35px rgba(0,0,0,0.08) !important; /* Aquele sombreado de objeto real */
            position: relative !important;
            margin: 30px 0 !important;
            transition: all 0.3s ease !important;
        }

        /* O ÍCONE 📄 QUE PARECE UM SELO NO TOPO */
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 35px;
            z-index: 99;
            filter: drop-shadow(0 4px 4px rgba(0,0,0,0.1));
        }

        /* AS CORES PASTÉIS DO ENVELOPE (ORIGINAIS) */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { 
            background: linear-gradient(180deg, #EBF9FF 0%, #FFFFFF 100%) !important; 
            border-color: #00BFFF !important; 
        }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { 
            background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%) !important; 
            border-color: #FF69B4 !important; 
        }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { 
            background: linear-gradient(180deg, #F1FFF7 0%, #FFFFFF 100%) !important; 
            border-color: #2ECC71 !important; 
        }

        /* =================================================================================
           4. ABAS INTERNAS (COLORIDAS INTEIRAS)
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 55px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 10px 35px 0 0 !important;
            border: 1px solid #ADB5BD !important;
            font-weight: 700;
            margin-right: 5px;
            transition: 0.3s;
        }
        
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; transform: translateY(-8px) !important; border: none !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF69B4 !important; color: white !important; transform: translateY(-8px) !important; border: none !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #2ECC71 !important; color: white !important; transform: translateY(-8px) !important; border: none !important; }

        /* =================================================================================
           5. FINALIZAÇÃO
        ================================================================================= */
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border-radius: 0 30px 30px 30px !important;
            padding: 40px !important;
            border: 1px solid #DEE2E6;
            box-shadow: 0 10px 30px rgba(0,0,0,0.04);
            border-top: 8px solid #DEE2E6;
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
        }
        div.stButton > button:hover, div.stDownloadButton > button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }

        </style>
    """, unsafe_allow_html=True)
