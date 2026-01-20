import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* Impede comportamentos estranhos na Sidebar ao passar o mouse */
        [data-testid="stSidebar"] section {
            background-color: #fdfdfd;
        }

        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
        }

        .titulo-principal {
            color: #1E1E1E;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .barra-laranja {
            width: 80px;
            height: 6px;
            background: linear-gradient(90deg, #FF8C00 0%, #FF4500 100%);
            border-radius: 10px;
            margin-bottom: 30px;
        }

        /* Botão Laranja Metalizado Degradê - Estabilizado */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #ff8a00, #e65c00) !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 600 !important;
            border: none !important;
            box-shadow: 0 4px 10px rgba(230, 92, 0, 0.2) !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: none !important; /* Remove transição que causa erro no mouse */
        }

        /* Hover simplificado para não gerar keyboard_double */
        .stButton > button:hover, .stDownloadButton > button:hover {
            background: #e65c00 !important;
            border: none !important;
            color: white !important;
        }

        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #eee;
            border-left: 5px solid #FF6F00;
            margin: 15px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
