import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA GERAL (FUNDAÇÃO)
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. VISUAL DIAMANTE/METALIZADO (AS PASTAS ESCOLARES VOLTARAM)
        ================================================================================= */
        
        /* Forma Base das Abas (Prata Diamante) */
        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 35px 90px 0 0 !important; /* O formato de pasta */
            padding: 0px 70px !important;
            border: 2px solid #ADB5BD !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #495057 !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        /* Efeito Shine Bright (Brilho Metalizado no Hover) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-8px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), 
                        linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* MÃES ATIVAS: Definimos a cor fixa APENAS para as abas do topo */
        .stTabs > div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; transform: translateY(-30px) !important; color: white !important; }
        .stTabs > div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; transform: translateY(-30px) !important; color: white !important; }
        .stTabs > div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"] { background: #2ECC71 !important; transform: translateY(-30px) !important; color: white !important; }

        /* =================================================================================
           3. OS ENVELOPES (ELES VOLTARAM!)
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            border-top: 18px solid #FDFDFD !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
            margin: 25px 0 !important;
            position: relative !important;
            background-color: #F8F9FA; /* Base cinza claro se nenhuma cor pegar */
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

        /* =================================================================================
           4. LÓGICA DE CORES DOS SETORES (A CORREÇÃO DO RET)
        ================================================================================= */

        /* 🟦 CENÁRIO AZUL (Pai 1 Ativo) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(1)[aria-selected="true"]) {
            /* Neon */
            > [data-testid="stTabPanel"] { border-color: #00D1FF !important; box-shadow: 0 0 30px #00D1FF !important; }
            /* Filhas */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #00BFFF !important; color: white !important; }
            /* Envelopes */
            [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px solid #A7E9FF !important; }
            /* Botão Hover */
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #00BFFF !important; border-color: #00BFFF !important; }
        }

        /* 🟩 CENÁRIO VERDE (Pai 3 Ativo) */
        /* Coloquei o verde ANTES do rosa para ele ser "mais fraco" na cascata */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(3)[aria-selected="true"]) {
            /* Neon */
            > [data-testid="stTabPanel"] { border-color: #2ECC71 !important; box-shadow: 0 0 30px #2ECC71 !important; }
            /* Filhas */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #2ECC71 !important; color: white !important; }
            /* Envelopes */
            [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 2px solid #A9DFBF !important; }
            /* Botão Hover */
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #2ECC71 !important; border-color: #2ECC71 !important; }
        }

        /* 🟥 CENÁRIO ROSA (Pai 2 Ativo) - O MESTRE */
        /* Estando por último, ele manda. */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-child(2)[aria-selected="true"]) {
            /* Neon */
            > [data-testid="stTabPanel"] { border-color: #FF69B4 !important; box-shadow: 0 0 30px #FF69B4 !important; }
            
            /* Filhas (Regra Geral Rosa) */
            [data-testid="stTabPanel"] button[aria-selected="true"] { background-color: #FF69B4 !important; color: white !important; }

            /* 🚨 A CURA DO RET (REGRA ESPECÍFICA) 🚨 */
            /* Aqui eu digo: "Se estiver na Casa Rosa, o 3º filho É ROSA!" */
            [data-testid="stTabPanel"] button:nth-child(3)[aria-selected="true"] { 
                background-color: #FF69B4 !important; 
            }

            /* Envelopes */
            [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }
            /* Botão Hover */
            div.stDownloadButton > button:hover { box-shadow: 0 0 20px #FF69B4 !important; border-color: #FF69B4 !important; }
        }

        /* =================================================================================
           5. ACABAMENTOS FINAIS
        ================================================================================= */
        [data-testid="stTabPanel"] { background: white !important; padding: 50px !important; border-radius: 0 60px 60px 60px !important; border: 6px solid transparent !important; }
        
        /* Reset para sub-abas não selecionadas (Ficam cinza e menores) */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] { 
            height: 60px !important; 
            background: #F1F3F5 !important; 
            border-radius: 15px 45px 0 0 !important; 
            transform: none !important;
            padding: 0 30px !important;
        }
        
        /* Botão Download Base */
        div.stDownloadButton > button { background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important; color: #495057 !important; border: 2px solid #ADB5BD !important; border-radius: 15px !important; font-weight: 800 !important; height: 55px !important; width: 100% !important; text-transform: uppercase !important; }
        
        </style>
    """, unsafe_allow_html=True)
