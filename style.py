import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        /* Blindagem para esconder ícones e textos fantasmas */
        span[data-testid="stHeaderActionElements"], 
        .st-emotion-cache-10oheav, 
        #keyboard_double {
            display: none !important;
            visibility: hidden !important;
        }

        /* BOTÃO LARANJA METALIZADO REAL (O que você amou o brilho) */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(180deg, #FF9D26 0%, #FF6F00 50%, #E65C00 100%) !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 1px solid #FF8C00 !important;
            box-shadow: 
                inset 0 1px 0 rgba(255,255,255,0.4),
                0 4px 15px rgba(230, 92, 0, 0.4) !important;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
            transition: all 0.2s ease-in-out !important;
        }

        .stButton > button:hover {
            filter: brightness(1.15);
            transform: translateY(-1px);
            box-shadow: 
                inset 0 1px 0 rgba(255,255,255,0.6),
                0 6px 20px rgba(230, 92, 0, 0.5) !important;
        }

        .titulo-principal { color: #1E1E1E; font-size: 2.5rem; font-weight: 800; margin-bottom: 5px; }
        .barra-laranja { width: 80px; height: 6px; background-color: #FF6F00; border-radius: 10px; margin-bottom: 30px; }
        
        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #FF6F00;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
