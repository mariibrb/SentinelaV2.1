import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
        }

        .titulo-principal {
            color: #1E1E1E;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 5px;
        }

        /* Barra com Degradê Metalizado */
        .barra-laranja {
            width: 80px;
            height: 6px;
            background: linear-gradient(90deg, #FF8C00 0%, #FF4500 100%);
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
        }

        /* Input de Empresa em Formato Pílula */
        div[data-baseweb="select"], 
        div[data-baseweb="select"] > div,
        div[data-baseweb="select"] [role="combobox"] {
            border-radius: 50px !important;
            border: 1px solid #d1d1d1 !important;
        }

        div[data-baseweb="select"] [data-testid="stSelectboxVirtualFocusContainer"] {
            padding-left: 15px !important;
        }

        /* Botão com Efeito Laranja Metalizado Degradê */
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(145deg, #ff8a00, #e65c00) !important;
            color: white !important;
            border-radius: 50px !important;
            font-weight: 600 !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(230, 92, 0, 0.3), inset 0 -2px 5px rgba(0,0,0,0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            background: linear-gradient(145deg, #ff9d26, #ff6a00) !important;
            box-shadow: 0 6px 20px rgba(230, 92, 0, 0.4) !important;
            transform: translateY(-1px);
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
