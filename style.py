import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Plus+Jakarta+Sans:wght@400;600&display=swap');

        /* 1. FUNDAÇÃO */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 1px solid #CED4DA !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: #F4F6F9 !important; }
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 900; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 2px 2px 0px #FFFFFF !important; }

        /* =================================================================================
           2. O FIM DAS BOLOTINHAS (TRANSFORMAÇÃO TOTAL DO MENU)
        ================================================================================= */
        
        /* 1. Esconde a bolinha original do Streamlit */
        [role="radiogroup"] label > div:first-child { 
            display: none !important; 
        }

        /* 2. O Container do Menu (A Régua) */
        [role="radiogroup"] {
            display: flex;
            justify-content: center;
            gap: 15px;
            background: #FFFFFF;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            margin-bottom: 30px;
            border: 1px solid #DEE2E6;
        }

        /* 3. O Botão (Label) - Aparência Inativa */
        [role="radiogroup"] label {
            background-color: #F8F9FA !important;
            border: 2px solid #E9ECEF !important;
            border-radius: 10px !important;
            padding: 15px 40px !important; /* Botão Gordo */
            font-family: 'Montserrat', sans-serif !important;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            color: #ADB5BD !important; /* Texto cinza claro */
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            text-align: center;
            min-width: 220px; /* Largura fixa para todos */
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Hover no Botão */
        [role="radiogroup"] label:hover {
            transform: translateY(-3px);
            background-color: #E9ECEF !important;
            color: #495057 !important;
        }

        /* =================================================================================
           3. CORES ATIVAS (AQUI VOCÊ SABE ONDE ESTÁ)
           Usamos o seletor div:has(...) para iluminar o botão certo
        ================================================================================= */

        /* 🟦 SE O MÓDULO FOR XML (AZUL) */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background-color: #00BFFF !important; /* Fundo Azul */
            border-color: #00BFFF !important;
            color: white !important; /* Texto Branco */
            box-shadow: 0 8px 20px rgba(0, 191, 255, 0.4) !important; /* Brilho Neon */
            transform: scale(1.05);
        }
        /* Pinta a borda do container principal também */
        div:has(#modulo-xml) [role="radiogroup"] { border-bottom: 5px solid #00BFFF !important; }


        /* 🟥 SE O MÓDULO FOR CONFORMIDADE (ROSA) */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background-color: #FF69B4 !important; /* Fundo Rosa */
            border-color: #FF69B4 !important;
            color: white !important; /* Texto Branco */
            box-shadow: 0 8px 20px rgba(255, 105, 180, 0.4) !important; /* Brilho Neon */
            transform: scale(1.05);
        }
        /* Pinta a borda do container principal também */
        div:has(#modulo-conformidade) [role="radiogroup"] { border-bottom: 5px solid #FF69B4 !important; }


        /* 🟩 SE O MÓDULO FOR APURAÇÃO (VERDE) */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background-color: #2ECC71 !important; /* Fundo Verde */
            border-color: #2ECC71 !important;
            color: white !important; /* Texto Branco */
            box-shadow: 0 8px 20px rgba(46, 204, 113, 0.4) !important; /* Brilho Neon */
            transform: scale(1.05);
        }
        /* Pinta a borda do container principal também */
        div:has(#modulo-apuracao) [role="radiogroup"] { border-bottom: 5px solid #2ECC71 !important; }


        /* =================================================================================
           4. VISUAL DAS ABAS INTERNAS (PASTAS RETRÔ)
        ================================================================================= */
        .stTabs [data-baseweb="tab-list"] {
            gap: 5px !important;
            padding-top: 15px !important;
            border-bottom: none !important;
        }

        /* Aba Inativa (Visor de Pasta) */
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #E9ECEF !important;
            border-radius: 8px 8px 0 0 !important;
            padding: 0px 30px !important;
            border: 1px solid #CED4DA !important;
            border-bottom: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            color: #6C757D !important;
            margin-right: 2px !important;
            transition: all 0.2s ease !important;
        }

        /* Aba Ativa (Sobe e Ganha Cor do Módulo) */
        .stTabs [aria-selected="true"] {
            background: #FFFFFF !important;
            font-weight: 800 !important;
            border-top-width: 5px !important; /* A cor vem dos blocos abaixo */
            transform: translateY(-2px) !important;
            box-shadow: 0 -3px 10px rgba(0,0,0,0.05) !important;
            z-index: 10;
        }

        /* Aplicação das Cores nas Abas Internas */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { border-top-color: #00BFFF !important; color: #00BFFF !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }

        /* =================================================================================
           5. CAIXOTÃO E ENVELOPES (ACABAMENTOS)
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 40px !important;
            border-radius: 0 10px 10px 10px !important;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05) !important;
            border: 1px solid #DEE2E6;
        }

        /* Cor da Borda do Painel por Módulo */
        div:has(#modulo-xml) [data-testid="stTabPanel"] { border-top: 4px solid #00BFFF !important; }
        div:has(#modulo-conformidade) [data-testid="stTabPanel"] { border-top: 4px solid #FF69B4 !important; }
        div:has(#modulo-apuracao) [data-testid="stTabPanel"] { border-top: 4px solid #2ECC71 !important; }

        /* Envelopes (Nunca Somem) */
        [data-testid="stFileUploader"] {
            padding: 30px !important;
            border-radius: 10px !important;
            margin: 20px 0 !important;
            position: relative !important;
            background-color: #FFFFFF;
            border: 2px dashed #CED4DA;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -18px; left: 20px; font-size: 26px; z-index: 99; }

        /* Cores dos Envelopes por Módulo */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; background: #F0F8FF !important; }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF69B4 !important; background: #FFF0F5 !important; }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #2ECC71 !important; background: #F0FFF4 !important; }

        /* Botões Gerais */
        div.stButton > button, div.stDownloadButton > button {
            background: white !important;
            color: #495057 !important;
            border: 1px solid #ADB5BD !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            box-shadow: 0 2px 0 #ADB5BD !important;
        }
        </style>
    """, unsafe_allow_html=True)
