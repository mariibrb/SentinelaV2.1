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

        .barra-laranja {
            width: 80px;
            height: 6px;
            background: #FF6F00;
            border-radius: 10px;
            margin-bottom: 30px;
        }

        /* Correção completa para o formato pílula em todas as camadas */
        div[data-baseweb="select"], 
        div[data-baseweb="select"] > div,
        div[data-baseweb="select"] [role="combobox"] {
            border-radius: 50px !important;
            border: 1px solid #d1d1d1 !important;
        }

        /* Ajuste do preenchimento interno para não cortar o texto */
        div[data-baseweb="select"] [data-testid="stSelectboxVirtualFocusContainer"] {
            padding-left: 15px !important;
        }

        .status-container {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #FF6F00;
            margin: 20px 0;
        }

        .stButton > button {
            width: 100%;
            background-color: #FF6F00 !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }
        </style>
    """, unsafe_allow_html=True)
