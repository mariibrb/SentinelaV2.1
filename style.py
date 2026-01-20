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

        /* BOTÃO LARANJA METALIZADO REAL */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            /* Degradê de 3 tons para efeito de curvatura metálica */
            background: linear-gradient(180deg, #FF9D26 0%, #FF6F00 50%, #E65C00 100%) !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            border: 1px solid #FF8C00 !important;
            
            /* Sombra interna para o efeito metalizado 'glossy' */
            box-shadow: 
                inset 0 1px 0 rgba(255,255,255,0.4),
                0 4px 15px rgba(230, 92, 0, 0.4) !important;
            
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
            transition: all 0.2s ease-in-out !important;
        }

        /* Efeito de brilho ao passar o mouse sem quebrar o layout */
        .stButton > button:hover {
            filter: brightness(1.15);
            transform: translateY(-1px);
            box-shadow: 
                inset 0 1px 0 rgba(255,255,255,0.6),
                0 6px 20px rgba(230, 92, 0, 0.5) !important;
        }

        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border-left: 6px solid #FF6F00;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
