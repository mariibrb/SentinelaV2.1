import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA BASE (FUNDAÇÃO)
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 4px solid #CFD4D9 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: #F0F2F6 !important; } /* Fundo mais neutro e retrô */
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 2px 2px 0px #FFFFFF !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. O VISUAL RETRÔ ESTRUTURADO (A PASTINHA QUADRADA 📂)
        ================================================================================= */
        
        /* Espaço para as abas não cortarem */
        .stTabs [data-baseweb="tab-list"] {
            gap: 6px !important;
            padding-top: 20px !important;
            padding-bottom: 0px !important;
            border-bottom: none !important;
        }

        /* A ABA QUADRADINHA (Inativa) */
        .stTabs [data-baseweb="tab"] {
            height: 55px !important; /* Mais baixa e compacta */
            background: #E9ECEF !important; /* Cor de pasta fosca */
            /* O FORMATO QUADRADO: Cantos pequenos apenas no topo */
            border-radius: 8px 8px 0 0 !important; 
            padding: 0px 35px !important;
            border: 2px solid #CFD4D9 !important; /* Borda bem definida */
            border-bottom: none !important; /* Conecta com o papel */
            
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            color: #6C757D !important;
            transition: all 0.2s ease !important; /* Movimento mais rápido e seco */
            margin-right: 4px !important;
            box-shadow: inset 0 -3px 5px rgba(0,0,0,0.03) !important;
        }

        /* Hover Retrô */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-4px) !important; /* Pulo seco */
            background: #F8F9FA !important;
            color: #212529 !important;
        }

        /* A ABA ATIVA (MÃE) - Salta e conecta */
        .stTabs > div > [data-baseweb="tab-list"] > button[aria-selected="true"] {
            transform: translateY(-6px) !important;
            background: #FFFFFF !important; /* Fica branca igual o papel */
            color: #212529 !important;
            font-weight: 800 !important;
            height: 60px !important;
            border: 2px solid #CFD4D9 !important;
            border-bottom: none !important; /* FUSÃO PERFEITA COM O PAINEL */
            border-top-width: 6px !important; /* Indicador de cor grosso no topo */
            z-index: 100 !important;
            box-shadow: 0 -4px 8px rgba(0,0,0,0.05) !important;
        }

        /* =================================================================================
           3. MÓDULOS BLINDADOS (AS CORES NO TOPO DA PASTA)
        ================================================================================= */

        /* 🟦 MÓDULO 1: ANÁLISE XML (AZUL) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            /* Borda grossa no topo da aba */
            > div > [data-baseweb="tab-list"] > button:nth-child(1) { border-top-color: #00BFFF !important; color: #00BFFF !important; }
            
            /* O Caixotão com borda Azul */
            > [data-testid="stTabPanel"] {
                border: 2px solid #CFD4D9 !important;
                border-top: 6px solid #00BFFF !important;
            }
            
            /* Sub-abas e elementos Azuis */
            [data-testid="stTabPanel"] button[aria-selected="true"] { color: #00BFFF !important; border-bottom: 3px solid #00BFFF !important; }
            [data-testid="stFileUploader"] { border: 2px dashed #00BFFF !important; background-color: #F0F8FF !important; }
            div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; border-color: #00BFFF !important; }
        }

        /* 🟥 MÓDULO 2: CONFORMIDADE (ROSA) - CASA DO RET */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            /* Borda grossa no topo da aba */
            > div > [data-baseweb="tab-list"] > button:nth-child(2) { border-top-color: #FF69B4 !important; color: #FF69B4 !important; }
            
            /* O Caixotão com borda Rosa */
            > [data-testid="stTabPanel"] {
                border: 2px solid #CFD4D9 !important;
                border-top: 6px solid #FF69B4 !important;
            }
            
            /* Sub-abas e elementos Rosas (RET incluso) */
            [data-testid="stTabPanel"] button[aria-selected="true"] { color: #FF69B4 !important; border-bottom: 3px solid #FF69B4 !important; }
            [data-testid="stFileUploader"] { border: 2px dashed #FF69B4 !important; background-color: #FFF5F8 !important; }
            div.stDownloadButton > button:hover { background: #FF69B4 !important; color: white !important; border-color: #FF69B4 !important; }
        }

        /* 🟩 MÓDULO 3: APURAÇÃO (VERDE) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            /* Borda grossa no topo da aba */
            > div > [data-baseweb="tab-list"] > button:nth-child(3) { border-top-color: #2ECC71 !important; color: #2ECC71 !important; }
            
            /* O Caixotão com borda Verde */
            > [data-testid="stTabPanel"] {
                border: 2px solid #CFD4D9 !important;
                border-top: 6px solid #2ECC71 !important;
            }
            
            /* Sub-abas e elementos Verdes */
            [data-testid="stTabPanel"] button[aria-selected="true"] { color: #2ECC71 !important; border-bottom: 3px solid #2ECC71 !important; }
            [data-testid="stFileUploader"] { border: 2px dashed #2ECC71 !important; background-color: #F1FFF5 !important; }
            div.stDownloadButton > button:hover { background: #2ECC71 !important; color: white !important; border-color: #2ECC71 !important; }
        }

        /* =================================================================================
           4. ACABAMENTOS GERAIS (ESTRUTURADOS)
        ================================================================================= */
        
        /* O Caixotão (O Papel dentro da pasta) */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            /* Cantos menos arredondados, mais quadrados */
            border-radius: 0 15px 15px 15px !important; 
            margin-top: -2px !important; /* Conexão perfeita */
            min-height: 800px !important;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
        }

        /* Sub-abas Inativas (Pastinhas menores e quadradas) */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            border-radius: 6px 6px 0 0 !important; /* Bem quadradinhas */
            padding: 0 25px !important;
            transform: none !important;
            background: #F8F9FA !important;
            border: 1px solid #DEE2E6 !important;
            border-bottom: none !important;
        }
        /* Sub-aba ativa (Filha) */
        [data-testid="stTabPanel"] .stTabs [aria-selected="true"] {
             background: #FFFFFF !important;
             border-top: 3px solid !important; /* Cor vem do módulo */
             transform: translateY(-3px) !important;
        }

        /* ENVELOPES (GLOBAL) */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 12px !important; /* Menos redondo */
            border-top: 15px solid #FFFFFF !important;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA;
            border: 2px dashed #CFD4D9; /* Borda tracejada padrão */
        }
        [data-testid="stFileUploader"]::before { content: "📄"; position: absolute; top: -28px; left: 50%; transform: translateX(-50%); font-size: 32px; z-index: 99; }

        /* BOTÕES ESTRUTURADOS (SEM VERMELHO) */
        div.stButton > button, div.stDownloadButton > button {
            background: #F8F9FA !important; /* Fundo sólido, sem degradê */
            color: #495057 !important;
            border: 2px solid #CFD4D9 !important; /* Borda forte */
            border-radius: 8px !important; /* Canto quase quadrado */
            font-weight: 800 !important;
            height: 50px !important;
            width: 100% !important;
            text-transform: uppercase !important;
            box-shadow: 0 2px 0px #ADB5BD !important; /* Sombra sólida retrô */
            transition: all 0.1s ease !important;
            transform: translateY(0px);
        }
        div.stButton > button:hover, div.stDownloadButton > button:hover {
             transform: translateY(2px) !important; /* Efeito de clique físico */
             box-shadow: 0 0px 0px #ADB5BD !important;
        }

        </style>
    """, unsafe_allow_html=True)
