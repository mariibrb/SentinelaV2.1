import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA BASE
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 1px solid #CED4DA !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: #F4F6F9 !important; } /* Fundo de escritório neutro */
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 2px 2px 0px #FFFFFF !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. O VISUAL "SEPARADOR DE PASTA SUSPENSA" (O SEGREDO)
        ================================================================================= */
        
        /* Ajuste para a aba "correr" no trilho */
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px !important;
            padding-top: 20px !important; /* Espaço para o visor subir */
            padding-bottom: 0px !important;
            border-bottom: 2px solid #DEE2E6 !important; /* O "Trilho" do arquivo */
        }

        /* O VISOR INATIVO (A etiqueta lá no fundo) */
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #E9ECEF !important; /* Cor de papel pardo/neutro */
            /* O FORMATO DO VISOR DE PLÁSTICO: Cantos arredondados no topo */
            border-radius: 10px 10px 0 0 !important; 
            padding: 0px 30px !important;
            border: 1px solid #CED4DA !important;
            border-bottom: none !important;
            
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 1.2rem !important;
            font-weight: 600 !important;
            color: #ADB5BD !important; /* Texto apagadinho */
            transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
            margin-right: 2px !important;
            transform: translateY(5px) !important; /* Fica "afundada" */
            box-shadow: inset 0 -5px 10px rgba(0,0,0,0.02);
        }

        /* Hover: O visor tenta subir */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(0px) !important;
            background: #F8F9FA !important;
            color: #495057 !important;
        }

        /* O VISOR ATIVO (MÃE) - PUXADO PARA CIMA */
        .stTabs > div > [data-baseweb="tab-list"] > button[aria-selected="true"] {
            transform: translateY(2px) !important; /* Cola na linha de baixo */
            height: 65px !important; /* Cresce */
            background: #FFFFFF !important;
            color: #212529 !important;
            font-weight: 800 !important;
            font-size: 1.4rem !important;
            border: 1px solid #CED4DA !important;
            border-bottom: none !important; /* Funde com a pasta */
            border-top-width: 6px !important; /* A TARJA COLORIDA DO VISOR */
            z-index: 100 !important;
            box-shadow: 0 -3px 8px rgba(0,0,0,0.05) !important;
        }

        /* =================================================================================
           3. OS MÓDULOS (A COR DA PASTA E DO VISOR)
        ================================================================================= */

        /* 🟦 MÓDULO 1: ANÁLISE XML (AZUL) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            /* Tarja do Visor */
            > div > [data-baseweb="tab-list"] > button:nth-child(1) { border-top-color: #00BFFF !important; color: #00BFFF !important; }
            
            /* O CORPO DA PASTA SUSPENSA */
            > [data-testid="stTabPanel"] {
                border-top: 6px solid #00BFFF !important; /* A Vareta Azul */
                background: linear-gradient(180deg, #F5FBFF 0%, #FFFFFF 100%) !important;
            }
            
            /* Sub-abas e Elementos Azuis */
            [data-testid="stTabPanel"] button[aria-selected="true"] { 
                color: #00BFFF !important; 
                border-bottom: 2px solid #00BFFF !important; 
                background: rgba(0, 191, 255, 0.05) !important;
            }
            [data-testid="stFileUploader"] { border: 1px dashed #00BFFF !important; background-color: #F0F8FF !important; }
            div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; border-color: #00BFFF !important; }
        }

        /* 🟥 MÓDULO 2: CONFORMIDADE (ROSA) - CASA DO RET */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            /* Tarja do Visor */
            > div > [data-baseweb="tab-list"] > button:nth-child(2) { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
            
            /* O CORPO DA PASTA SUSPENSA */
            > [data-testid="stTabPanel"] {
                border-top: 6px solid #FF69B4 !important; /* A Vareta Rosa */
                background: linear-gradient(180deg, #FFF5F8 0%, #FFFFFF 100%) !important;
            }
            
            /* Sub-abas e Elementos Rosas */
            [data-testid="stTabPanel"] button[aria-selected="true"] { 
                color: #FF69B4 !important; 
                border-bottom: 2px solid #FF69B4 !important;
                background: rgba(255, 105, 180, 0.05) !important;
            }
            [data-testid="stFileUploader"] { border: 1px dashed #FF69B4 !important; background-color: #FFF0F5 !important; }
            div.stDownloadButton > button:hover { background: #FF69B4 !important; color: white !important; border-color: #FF69B4 !important; }
        }

        /* 🟩 MÓDULO 3: APURAÇÃO (VERDE) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            /* Tarja do Visor */
            > div > [data-baseweb="tab-list"] > button:nth-child(3) { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }
            
            /* O CORPO DA PASTA SUSPENSA */
            > [data-testid="stTabPanel"] {
                border-top: 6px solid #2ECC71 !important; /* A Vareta Verde */
                background: linear-gradient(180deg, #F1FFF5 0%, #FFFFFF 100%) !important;
            }
            
            /* Sub-abas e Elementos Verdes */
            [data-testid="stTabPanel"] button[aria-selected="true"] { 
                color: #2ECC71 !important; 
                border-bottom: 2px solid #2ECC71 !important;
                background: rgba(46, 204, 113, 0.05) !important;
            }
            [data-testid="stFileUploader"] { border: 1px dashed #2ECC71 !important; background-color: #F1FFF7 !important; }
            div.stDownloadButton > button:hover { background: #2ECC71 !important; color: white !important; border-color: #2ECC71 !important; }
        }

        /* =================================================================================
           4. ACABAMENTOS DO ARQUIVO
        ================================================================================= */
        
        /* O CORPO DA PASTA (ONDE VÃO OS DOCUMENTOS) */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            /* Cantos inferiores arredondados como pasta */
            border-radius: 0 0 15px 15px !important; 
            margin-top: -2px !important; /* Gruda na aba */
            border-left: 1px solid #DEE2E6;
            border-right: 1px solid #DEE2E6;
            border-bottom: 1px solid #DEE2E6;
            min-height: 800px !important;
            box-shadow: 0 5px 20px rgba(0,0,0,0.03);
        }

        /* Sub-abas (Pastinhas Internas menores) */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] {
            height: 45px !important;
            border-radius: 8px 8px 0 0 !important;
            padding: 0 20px !important;
            transform: none !important;
            background: transparent !important;
            border: none !important;
            color: #6C757D !important;
            font-size: 1rem !important;
        }
        /* Sub-aba ativa (Só o texto destaca) */
        [data-testid="stTabPanel"] .stTabs [aria-selected="true"] {
             font-weight: 800 !important;
             background: #FFFFFF !important;
             transform: none !important;
             box-shadow: none !important;
        }

        /* ENVELOPES (PAPEL DE CARTA) */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 4px !important; /* Canto de papel */
            border-top: 0px !important;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #FFFFFF;
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -15px; left: 20px; font-size: 24px; z-index: 99; transform: none; }

        /* BOTÕES RETRÔ (SÓLIDOS) */
        div.stButton > button, div.stDownloadButton > button {
            background: #FFFFFF !important;
            color: #495057 !important;
            border: 1px solid #CED4DA !important;
            border-radius: 6px !important;
            font-weight: 700 !important;
            height: 45px !important;
            width: 100% !important;
            text-transform: uppercase !important;
            box-shadow: 0 2px 0 #CED4DA !important;
            transition: all 0.1s ease !important;
        }
        div.stButton > button:hover, div.stDownloadButton > button:hover {
             transform: translateY(2px) !important;
             box-shadow: none !important;
        }

        </style>
    """, unsafe_allow_html=True)
