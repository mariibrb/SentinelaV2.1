import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA BASE & TITULO
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. GLOBAL: ENVELOPES (PARA NUNCA MAIS SUMIR)
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 15px !important;
            border-top: 15px solid #FFFFFF !important; /* Topo branco */
            box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA; /* Cor base de segurança */
            transition: all 0.3s ease !important;
        }
        
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute;
            top: -28px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 32px;
            z-index: 99;
        }

        /* =================================================================================
           3. VISUAL "RIHANNA" (AS PASTAS DIAMANTE)
        ================================================================================= */
        
        /* Forma da Aba (A Pasta Escolar Assimétrica) */
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important; /* Prata */
            border-radius: 35px 90px 0 0 !important; /* A CURVA DA PASTA */
            padding: 0px 60px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.5rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
            transition: all 0.3s ease !important;
            margin-right: 5px !important;
        }

        /* Brilho Shine Bright (Hover) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-8px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
            border-color: #868E96 !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* Abas Selecionadas (Sobem) */
        .stTabs > div > [data-baseweb="tab-list"] > button[aria-selected="true"] {
            transform: translateY(-20px) !important;
            color: white !important; /* A cor de fundo virá dos módulos abaixo */
            border: none !important;
        }

        /* =================================================================================
           4. SEPARAÇÃO DE MÓDULOS (A BLINDAGEM VISUAL)
           Aqui definimos cada "Mundo" separadamente.
        ================================================================================= */

        /* ---------------------------------------------------------------------
           🟦 MÓDULO 1: ANÁLISE XML (AZUL)
           --------------------------------------------------------------------- */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            
            /* Pinta a Aba Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(1) { background: #00BFFF !important; }
            
            /* O CAIXOTÃO (PAINEL) VIRA UMA ZONA AZUL */
            > [data-testid="stTabPanel"] {
                border: 4px solid #00BFFF !important;
                box-shadow: 0 0 40px rgba(0, 191, 255, 0.2), inset 0 0 50px rgba(0, 191, 255, 0.05) !important;
            }

            /* Todas as filhas aqui dentro são Azuis */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #00BFFF !important; color: white !important; }
            
            /* Envelope Azul */
            [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px dashed #00BFFF !important; }
            
            /* Botão Azul */
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #00BFFF !important; border-color: #00BFFF !important; }
        }

        /* ---------------------------------------------------------------------
           🟥 MÓDULO 2: CONFORMIDADE (ROSA) - O REINO DO RET
           --------------------------------------------------------------------- */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            
            /* Pinta a Aba Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(2) { background: #FF69B4 !important; }
            
            /* O CAIXOTÃO VIRA UMA ZONA ROSA */
            > [data-testid="stTabPanel"] {
                border: 4px solid #FF69B4 !important;
                box-shadow: 0 0 40px rgba(255, 105, 180, 0.2), inset 0 0 50px rgba(255, 105, 180, 0.05) !important;
            }

            /* Todas as filhas aqui dentro são Rosas (Inclusive a 3ª/RET) */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #FF69B4 !important; color: white !important; }
            
            /* Envelope Rosa */
            [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px dashed #FF69B4 !important; }
            
            /* Botão Rosa */
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; }
        }

        /* ---------------------------------------------------------------------
           🟩 MÓDULO 3: APURAÇÃO (VERDE)
           --------------------------------------------------------------------- */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            
            /* Pinta a Aba Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-child(3) { background: #2ECC71 !important; }
            
            /* O CAIXOTÃO VIRA UMA ZONA VERDE */
            > [data-testid="stTabPanel"] {
                border: 4px solid #2ECC71 !important;
                box-shadow: 0 0 40px rgba(46, 204, 113, 0.2), inset 0 0 50px rgba(46, 204, 113, 0.05) !important;
            }

            /* Todas as filhas aqui dentro são Verdes */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #2ECC71 !important; color: white !important; }
            
            /* Envelope Verde */
            [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px dashed #2ECC71 !important; }
            
            /* Botão Verde */
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; }
        }

        /* =================================================================================
           5. ACABAMENTOS FINAIS
        ================================================================================= */
        
        /* O Caixotão (Base Branca) */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -10px !important;
            min-height: 800px !important;
        }

        /* Sub-abas (Filhas) Inativas - Prata Menor */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F1F3F5 !important;
            border-radius: 15px 45px 0 0 !important;
            padding: 0 30px !important;
            transform: none !important; /* Sem pular */
        }

        /* Botões Prateados (Exterminando o Vermelho) */
        div.stButton > button, div.stDownloadButton > button {
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            color: #495057 !important;
            border: 2px solid #ADB5BD !important;
            border-radius: 15px !important;
            font-weight: 800 !important;
            height: 55px !important;
            width: 100% !important;
            text-transform: uppercase !important;
            box-shadow: none !important;
            transition: 0.3s ease !important;
        }

        </style>
    """, unsafe_allow_html=True)
