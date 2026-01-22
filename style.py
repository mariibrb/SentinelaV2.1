import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* LIMPEZA TOTAL DO TOPO (SIDEBAR E APP) */
        header, .st-emotion-cache-18ni7ap, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"],
        button[title="View keyboard shortcuts"] {
            display: none !important;
            visibility: hidden !important;
            height: 0px !important;
            padding: 0px !important;
            margin: 0px !important;
        }
        
        /* AJUSTE PARA O CONTEÚDO NÃO SUBIR DEMAIS */
        .block-container { padding-top: 2rem !important; }
        .st-emotion-cache-6qob1r { padding-top: 0px !important; }

        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

        /* TÍTULOS */
        .titulo-principal { color: #1E1E1E; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-marsala { width: 80px; height: 6px; background: linear-gradient(90deg, #A12B2B, #6B1B1B); border-radius: 10px; margin-bottom: 30px; }

        /* ABAS METALIZADAS COM BRILHO (RESTAURADO) */
        .stTabs [data-baseweb="tab"] {
            height: 70px !important;
            background: #f0f2f6 !important;
            border-radius: 15px 15px 0px 0px !important;
            padding: 10px 40px !important;
            font-size: 20px !important; 
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.1) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, #D44D4D 0%, #A12B2B 50%, #801818 100%) !important;
            color: white !important;
            font-weight: 800 !important;
            box-shadow: 0 -5px 15px rgba(161, 43, 43, 0.4) !important;
        }

        /* BOTÕES LUXO COM BRILHO NO HOVER (RESTAURADO) */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #D44D4D 0%, #A12B2B 50%, #801818 100%) !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 1px solid #801818 !important;
            box-shadow: inset 0 2px 3px rgba(255,255,255,0.4), 0 4px 10px rgba(0,0,0,0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(161, 43, 43, 0.5) !important;
            filter: brightness(1.3) !important;
        }

        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #A12B2B;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
