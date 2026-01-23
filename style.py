import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* 1. FUNDAÇÃO */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 1px solid #CED4DA !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: #F4F6F9 !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 2px 2px 0px #FFFFFF !important; }

        /* =================================================================================
           2. MENU FLUTUANTE (DOCK) - TRANSFORMANDO O RADIO EM BOTÕES
        ================================================================================= */
        [role="radiogroup"] {
            flex-direction: row;
            justify-content: center;
            background: transparent;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        /* Esconde a bolinha do radio button */
        [role="radiogroup"] label > div:first-child { display: none !important; }
        
        /* O Botão do Menu (Inativo) */
        [role="radiogroup"] label {
            background: #FFFFFF !important;
            border: 1px solid #CED4DA !important;
            border-radius: 12px !important;
            padding: 15px 30px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700 !important;
            color: #6C757D !important;
            cursor: pointer !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
            transition: all 0.3s ease !important;
            min-width: 200px;
            text-align: center;
            display: flex;
            justify-content: center;
        }

        /* Hover no Menu */
        [role="radiogroup"] label:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.1) !important;
            color: #212529 !important;
            border-color: #ADB5BD !important;
        }

        /* O Botão do Menu (ATIVO) - Fica "Aceso" com a cor do módulo */
        [role="radiogroup"] label[data-checked="true"] {
            background: #FFFFFF !important;
            font-weight: 800 !important;
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(0,0,0,0.1) !important;
        }

        /* =================================================================================
           3. MÓDULOS DE COR (SEPARAÇÃO TOTAL)
           Aqui pintamos o Menu e as Abas baseado no módulo ativo
        ================================================================================= */

        /* 🟦 MÓDULO XML (AZUL) */
        /* Pinta o botão do menu */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] { border: 2px solid #00BFFF !important; color: #00BFFF !important; }
        
        /* Pinta as Abas Internas (Pastas) */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] {
            border-top-color: #00BFFF !important;
            color: #00BFFF !important;
        }
        /* Pinta o Envelope e Botões */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border: 2px dashed #00BFFF !important; background: #F0F8FF !important; }
        div:has(#modulo-xml) div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; }


        /* 🟥 MÓDULO CONFORMIDADE (ROSA) */
        /* Pinta o botão do menu */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] { border: 2px solid #FF69B4 !important; color: #FF69B4 !important; }
        
        /* Pinta as Abas Internas (Pastas) */
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] {
            border-top-color: #FF69B4 !important;
            color: #FF69B4 !important;
        }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border: 2px dashed #FF69B4 !important; background: #FFF0F5 !important; }


        /* 🟩 MÓDULO APURAÇÃO (VERDE) */
        /* Pinta o botão do menu */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] { border: 2px solid #2ECC71 !important; color: #2ECC71 !important; }
        
        /* Pinta as Abas Internas (Pastas) */
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] {
            border-top-color: #2ECC71 !important;
            color: #2ECC71 !important;
        }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border: 2px dashed #2ECC71 !important; background: #F0FFF4 !important; }


        /* =================================================================================
           4. DESIGN DAS PASTAS SUSPENSAS (RETRO SQUARE)
        ================================================================================= */
        
        /* O Visor (Aba) */
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #E9ECEF !important;
            border-radius: 8px 8px 0 0 !important; /* Quadradinho */
            padding: 0px 30px !important;
            border: 1px solid #CED4DA !important;
            border-bottom: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 1.1rem !important;
            color: #ADB5BD !important;
            margin-right: 2px !important;
            transform: translateY(5px) !important;
        }

        /* O Visor Ativo */
        .stTabs [aria-selected="true"] {
            transform: translateY(2px) !important; /* Cola no painel */
            height: 60px !important;
            background: #FFFFFF !important;
            color: #212529 !important;
            font-weight: 800 !important;
            border-top-width: 6px !important; /* A cor vem do módulo acima */
            border-bottom: none !important;
            z-index: 100;
        }

        /* 5. ACABAMENTOS */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border: 1px solid #DEE2E6;
            border-top: 6px solid #DEE2E6; /* Cor base */
            border-radius: 0 0 15px 15px !important;
            margin-top: -2px !important;
            padding: 40px !important;
        }
        
        /* Cor da Vareta do Painel por Módulo */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top-color: #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top-color: #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top-color: #2ECC71 !important; }

        /* Envelopes (Global) */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 8px !important;
            border: 1px dashed #ADB5BD;
            background-color: white;
            margin: 15px 0 !important;
            position: relative !important;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -15px; left: 20px; font-size: 24px; z-index: 99; }

        /* Botões Sólidos */
        div.stButton > button, div.stDownloadButton > button {
            background: #FFFFFF !important;
            color: #495057 !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 6px !important;
            text-transform: uppercase;
            font-weight: 700 !important;
            box-shadow: 0 2px 0 #ADB5BD !important;
        }
        </style>
    """, unsafe_allow_html=True)
