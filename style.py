import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Plus+Jakarta+Sans:wght@400;600&display=swap');

        /* 1. FUNDAÇÃO */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 1px solid #CED4DA !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: #F4F6F9 !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 2px 2px 0px #FFFFFF !important; }

        /* =================================================================================
           2. O MENU DE NAVEGAÇÃO "NA CARA" (SEM BOLINHAS)
        ================================================================================= */
        
        /* Container do Menu */
        [role="radiogroup"] {
            display: flex;
            justify-content: center;
            gap: 15px;
            width: 100%;
            background: transparent;
            margin-bottom: 20px;
        }

        /* 🚫 MATA A BOLINHA */
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* O BOTÃO (ESTADO NORMAL/DESLIGADO) */
        [role="radiogroup"] label {
            background: #FFFFFF !important;
            border: 2px solid #E9ECEF !important;
            border-radius: 12px !important;
            padding: 15px 20px !important;
            min-width: 200px;
            text-align: center;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700 !important;
            color: #ADB5BD !important; /* Cinza apagado */
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* HOVER GERAL (Aumenta um pouquinho) */
        [role="radiogroup"] label:hover {
            transform: translateY(-3px);
            border-color: #CED4DA !important;
            color: #6C757D !important;
        }

        /* =================================================================================
           3. A EXPLOSÃO DE CORES (IDENTIDADE POR POSIÇÃO)
           Aqui dizemos: "Se o 1º botão estiver marcado, pinte de AZUL", etc.
        ================================================================================= */

        /* 🟦 BOTÃO 1 (XML) - QUANDO ATIVO */
        [role="radiogroup"] label:nth-of-type(1)[data-checked="true"] {
            background-color: #00BFFF !important; /* AZULÃO */
            border-color: #00BFFF !important;
            color: white !important;
            box-shadow: 0 10px 25px rgba(0, 191, 255, 0.4) !important;
            transform: scale(1.05);
        }

        /* 🟥 BOTÃO 2 (CONFORMIDADE) - QUANDO ATIVO */
        [role="radiogroup"] label:nth-of-type(2)[data-checked="true"] {
            background-color: #FF69B4 !important; /* ROSÃO */
            border-color: #FF69B4 !important;
            color: white !important;
            box-shadow: 0 10px 25px rgba(255, 105, 180, 0.4) !important;
            transform: scale(1.05);
        }

        /* 🟩 BOTÃO 3 (APURAÇÃO) - QUANDO ATIVO */
        [role="radiogroup"] label:nth-of-type(3)[data-checked="true"] {
            background-color: #2ECC71 !important; /* VERDÃO */
            border-color: #2ECC71 !important;
            color: white !important;
            box-shadow: 0 10px 25px rgba(46, 204, 113, 0.4) !important;
            transform: scale(1.05);
        }

        /* =================================================================================
           4. REFLEXO NO PAINEL (O AMBIENTE REAGE)
           Usamos os IDs que colocamos no app.py para pintar as bordas
        ================================================================================= */

        /* 🟦 CENÁRIO AZUL */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { border-top-color: #00BFFF !important; color: #00BFFF !important; }
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border: 2px dashed #00BFFF !important; background: #F0F8FF !important; }
        div:has(#modulo-xml) div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; }
        /* Vareta do Painel */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top: 6px solid #00BFFF !important; }

        /* 🟥 CENÁRIO ROSA */
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border: 2px dashed #FF69B4 !important; background: #FFF0F5 !important; }
        div:has(#modulo-conformidade) div.stDownloadButton > button:hover { background: #FF69B4 !important; color: white !important; }
        /* Vareta do Painel */
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top: 6px solid #FF69B4 !important; }

        /* 🟩 CENÁRIO VERDE */
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border: 2px dashed #2ECC71 !important; background: #F0FFF4 !important; }
        div:has(#modulo-apuracao) div.stDownloadButton > button:hover { background: #2ECC71 !important; color: white !important; }
        /* Vareta do Painel */
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top: 6px solid #2ECC71 !important; }

        /* =================================================================================
           5. ACABAMENTOS (PASTAS E ENVELOPES)
        ================================================================================= */
        
        /* ENVELOPE GIGANTE (Nunca some) */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 10px !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #FFFFFF;
            border: 2px dashed #CED4DA; /* Padrão */
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -18px; left: 20px; font-size: 28px; z-index: 99; }

        /* PASTINHAS QUADRADAS (Retrô) */
        .stTabs [data-baseweb="tab-list"] { gap: 5px; border-bottom: 2px solid #DEE2E6; padding-top: 15px; }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #E9ECEF !important;
            border-radius: 8px 8px 0 0 !important;
            padding: 0 25px !important;
            border: 1px solid #CED4DA !important;
            border-bottom: none !important;
            color: #ADB5BD !important;
            font-weight: 600 !important;
        }

        /* PASTINHA ATIVA */
        .stTabs [aria-selected="true"] {
            background: #FFFFFF !important;
            color: #212529 !important;
            font-weight: 800 !important;
            border-top: 6px solid !important; /* Cor vem do cenário acima */
            height: 60px !important;
            transform: translateY(2px) !important;
            z-index: 10;
        }

        /* CAIXOTÃO BRANCO */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            border: 1px solid #DEE2E6;
            border-top: none; /* A borda colorida vem do "has" acima */
            border-radius: 0 0 10px 10px !important;
            padding: 40px !important;
        }

        /* BOTÕES GERAIS SÓLIDOS */
        div.stButton > button, div.stDownloadButton > button {
            background: #FFFFFF !important;
            color: #495057 !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            box-shadow: 0 2px 0 #ADB5BD !important;
        }
        </style>
    """, unsafe_allow_html=True)
