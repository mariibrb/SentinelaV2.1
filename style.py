import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA GERAL (BASE)
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        /* Título Limpo e Elegante */
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. O VISUAL "DIAMOND" (FÍSICO) - SEM CORES AINDA
        ================================================================================= */
        /* Design base para TODAS as abas (Mães e Filhas) */
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%); /* Prata */
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 70px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        /* Efeito Shine Bright (Brilho Metalizado no Hover) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
            border-color: #868E96 !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* =================================================================================
           3. A LÓGICA DE MUNDOS (CORES) - AQUI ESTÁ A CORREÇÃO
        ================================================================================= */
        
        /* --- MUNDO 1: ANÁLISE XML (AZUL) --- */
        /* Se a Aba Mãe 1 estiver ativa... */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            
            /* Pinta a própria Mãe de Azul */
            > div > [data-baseweb="tab-list"] > button:nth-child(1) { 
                background: #00BFFF !important; color: white !important; transform: translateY(-20px) !important;
            }
            
            /* Pinta QUALQUER filha selecionada neste mundo de Azul */
            [data-testid="stTabPanel"] [data-baseweb="tab"][aria-selected="true"] {
                background: #00BFFF !important; color: white !important;
            }
            
            /* Detalhes do Mundo Azul */
            [data-testid="stTabPanel"] { border-color: #00BFFF !important; box-shadow: 0 0 40px rgba(0, 191, 255, 0.3) !important; }
            [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px solid #A7E9FF !important; }
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #00BFFF !important; border-color: #00BFFF !important; }
        }

        /* --- MUNDO 2: CONFORMIDADE (ROSA) - A CASA DO RET --- */
        /* Se a Aba Mãe 2 estiver ativa... */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            
            /* Pinta a própria Mãe de Rosa */
            > div > [data-baseweb="tab-list"] > button:nth-child(2) { 
                background: #FF69B4 !important; color: white !important; transform: translateY(-20px) !important;
            }
            
            /* Pinta QUALQUER filha selecionada neste mundo de Rosa (INCLUINDO A 3ª/RET) */
            /* Como estamos dentro do bloco do Mundo 2, o verde não tem poder aqui */
            [data-testid="stTabPanel"] [data-baseweb="tab"][aria-selected="true"] {
                background: #FF69B4 !important; color: white !important;
            }
            
            /* Detalhes do Mundo Rosa */
            [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 40px rgba(255, 105, 180, 0.3) !important; }
            [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; }
        }

        /* --- MUNDO 3: APURAÇÃO (VERDE) --- */
        /* Se a Aba Mãe 3 estiver ativa... */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            
            /* Pinta a própria Mãe de Verde */
            > div > [data-baseweb="tab-list"] > button:nth-child(3) { 
                background: #2ECC71 !important; color: white !important; transform: translateY(-20px) !important;
            }
            
            /* Pinta QUALQUER filha selecionada neste mundo de Verde */
            [data-testid="stTabPanel"] [data-baseweb="tab"][aria-selected="true"] {
                background: #2ECC71 !important; color: white !important;
            }
            
            /* Detalhes do Mundo Verde */
            [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 40px rgba(46, 204, 113, 0.3) !important; }
            [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px solid #A9DFBF !important; }
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; }
        }

        /* =================================================================================
           4. ACABAMENTOS (ENVELOPES E PAINÉIS)
        ================================================================================= */
        
        /* O Grande Caixotão Branco */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -10px !important;
            border: 6px solid transparent !important;
            min-height: 800px !important;
        }

        /* Ajuste de tamanho para as Sub-abas (Filhas) para não ficarem gigantes */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F1F3F5 !important; /* Cinza claro quando inativo */
            border-radius: 15px 45px 0 0 !important;
            padding: 0 30px !important;
            font-size: 1.2rem !important;
        }

        /* O Envelope de Upload (Definição Global para não sumir) */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            border-top: 18px solid #FDFDFD !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA; /* Cor padrão de segurança */
        }
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute;
            top: -32px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 30px;
            z-index: 99;
        }

        /* Botão de Download */
        div.stDownloadButton > button {
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
