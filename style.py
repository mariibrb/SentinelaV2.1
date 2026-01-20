import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        /* Importação de Fonte Premium */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        /* Configuração Geral */
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
        }

        /* Título Principal */
        .titulo-principal {
            color: #1E1E1E;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 5px;
            letter-spacing: -1px;
        }

        /* Barra de Destaque (Verde para Versão 2.1) */
        .barra-laranja {
            width: 80px;
            height: 6px;
            background: #008000;
            border-radius: 10px;
            margin-bottom: 30px;
        }

        /* Estilo Pílula para o Selectbox (Lista Suspensa) */
        div[data-baseweb="select"] {
            border-radius: 50px !important; /* Formato de pílula */
            border: 1.5px solid #d1d1d1 !important;
            padding: 5px 15px !important;
            background-color: white !important;
            transition: all 0.3s ease;
        }

        div[data-baseweb="select"]:focus-within {
            border-color: #008000 !important;
            box-shadow: 0 0 0 1px #008000 !important;
        }

        /* Ajuste do Dropdown (Lista que abre) */
        ul[role="listbox"] {
            border-radius: 15px !important;
            margin-top: 10px !important;
        }

        /* Container de Status */
        .status-container {
            background-color: #f0f7f0;
            padding: 15px 20px;
            border-radius: 12px;
            border-left: 5px solid #008000;
            color: #2e4a2e;
            margin: 20px 0;
            font-size: 0.95rem;
        }

        /* Botão Principal */
        .stButton > button {
            width: 100%;
            background-color: #008000 !important;
            color: white !important;
            border-radius: 50px !important; /* Botão também tipo pílula */
            padding: 12px 25px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: transform 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,128,0,0.3);
        }

        /* Inputs de Arquivo */
        .stFileUploader {
            background-color: #ffffff;
            border: 1px dashed #008000;
            border-radius: 15px;
            padding: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
