import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* Remove todas as transições de CSS para eliminar o erro visual */
        * {
            transition: none !important;
            transition-duration: 0s !important;
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
            background-color: #FF6F00;
            border-radius: 10px;
            margin-bottom: 30px;
        }

        /* Botão Laranja Sólido (Estilo Pílula) - Sem degradê para evitar erros */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background-color: #FF6F00 !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 600 !important;
            border: none !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 10px 20px !important;
        }

        /* Hover simples sem animação */
        .stButton > button:hover, .stDownloadButton > button:hover {
            background-color: #E65C00 !important;
            color: white !important;
        }

        .status-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #f0f0f0;
            border-left: 5px solid #FF6F00;
            margin: 15px 0;
        }
        </style>
    """, unsafe_allow_html=True)
