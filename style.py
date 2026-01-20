import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* Reset para evitar fantasmas visuais */
        div[data-testid="stSidebar"] * {
            transition: none !important;
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

        /* Estilo do Seletor (Pílula) */
        div[data-baseweb="select"] {
            border-radius: 50px !important;
        }

        /* Botão Laranja Metalizado Degradê corrigido */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #ff8a00, #e65c00) !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 600 !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(230, 92, 0, 0.3) !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            /* Removida a transição complexa que causava o erro ao passar o mouse */
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            filter: brightness(1.1);
            box-shadow: 0 6px 20px rgba(230, 92, 0, 0.4) !important;
        }

        .status-container {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #FF6F00;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)
