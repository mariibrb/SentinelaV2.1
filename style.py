import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* =================================================================================
           1. ESTRUTURA E FUNDO (BASE)
        ================================================================================= */
        [data-testid="stSidebar"] { min-width: 350px !important; background-color: #E9ECEF !important; border-right: 5px solid #FF69B4 !important; }
        header, [data-testid="stHeader"] { display: none !important; }
        .stApp { background: radial-gradient(circle at top left, #F8F9FA 0%, #CED4DA 100%) !important; }
        
        .titulo-principal { font-family: 'Montserrat', sans-serif !important; color: #495057 !important; font-size: 3.5rem; font-weight: 800; text-transform: uppercase; padding: 20px 0 !important; text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.8) !important; }
        div[data-testid="stVerticalBlock"] > div:has(.titulo-principal) { background: transparent !important; box-shadow: none !important; border: none !important; }

        /* =================================================================================
           2. OS ENVELOPES (GLOBAL - PARA NUNCA SUMIR)
        ================================================================================= */
        [data-testid="stFileUploader"] {
            padding: 40px 30px 30px 30px !important;
            border-radius: 15px !important;
            border-top: 18px solid #FDFDFD !important; /* Detalhe branco no topo */
            box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important;
            margin: 20px 0 !important;
            position: relative !important;
            background-color: #FFFFFF; /* Cor padrão se o ambiente falhar */
            transition: all 0.3s ease !important;
        }

        /* O ÍCONE DE PAPEL 📄 */
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 32px;
            z-index: 99;
        }

        /* =================================================================================
           3. ABAS DIAMANTE (FORMATO)
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 75px !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            border-radius: 20px 20px 0 0 !important; 
            padding: 0px 50px !important;
            border: 1px solid #ADB5BD !important;
            font-size: 1.4rem !important;
            font-weight: 700 !important;
            color: #495057 !important;
            transition: all 0.3s ease !important;
        }
        
        /* Brilho Metalizado (Hover) */
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-5px) !important;
            background: linear-gradient(45deg, rgba(255,255,255,0) 30%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 70%), linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important;
            background-size: 200% 100% !important;
            animation: brilhoMetalico 1.5s infinite linear !important;
        }
        @keyframes brilhoMetalico { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

        /* Mães Ativas (Levantam) */
        .stTabs > div > [data-baseweb="tab-list"] > button[aria-selected="true"] {
            transform: translateY(-20px) !important; color: white !important;
        }

        /* =================================================================================
           4. AMBIENTES COLORIDOS (A SOLUÇÃO VISUAL)
           Aqui mudamos o Fundo da Tela e a Cor dos Textos baseado na Mãe
        ================================================================================= */

        /* 🟦 AMBIENTE AZUL (Mãe 1 Ativa) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-of-type(1)[aria-selected="true"]) {
            
            /* Pinta a Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-of-type(1) { background: #00BFFF !important; }
            
            /* Pinta o FUNDO DO PAINEL (Tela toda fica azulada) */
            > [data-testid="stTabPanel"] {
                background: linear-gradient(180deg, #F0F8FF 0%, #FFFFFF 100%) !important; /* Azul suave */
                border-top: 5px solid #00BFFF !important;
                box-shadow: 0 0 40px rgba(0, 191, 255, 0.2) !important;
            }

            /* Envelope vira Azul */
            [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 1px dashed #00BFFF !important; }
            
            /* Texto das Filhas vira Azul */
            [data-testid="stTabPanel"] [aria-selected="true"] { color: #00BFFF !important; border-bottom: 3px solid #00BFFF !important; }
            
            /* Botão vira Azul */
            div.stDownloadButton > button:hover { background: #00BFFF !important; color: white !important; }
        }

        /* 🟥 AMBIENTE ROSA (Mãe 2 Ativa) - O RET MORA AQUI */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-of-type(2)[aria-selected="true"]) {
            
            /* Pinta a Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-of-type(2) { background: #FF69B4 !important; }
            
            /* Pinta o FUNDO DO PAINEL (Tela toda fica rosada) */
            > [data-testid="stTabPanel"] {
                background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%) !important; /* Rosa suave */
                border-top: 5px solid #FF69B4 !important;
                box-shadow: 0 0 40px rgba(255, 105, 180, 0.2) !important;
            }

            /* Envelope vira Rosa */
            [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 1px dashed #FF69B4 !important; }
            
            /* Texto das Filhas vira Rosa (RET INCLUÍDO) */
            [data-testid="stTabPanel"] [aria-selected="true"] { color: #FF69B4 !important; border-bottom: 3px solid #FF69B4 !important; }
            
            /* Botão vira Rosa */
            div.stDownloadButton > button:hover { background: #FF69B4 !important; color: white !important; }
        }

        /* 🟩 AMBIENTE VERDE (Mãe 3 Ativa) */
        .stTabs:has(> div > [data-baseweb="tab-list"] > button:nth-of-type(3)[aria-selected="true"]) {
            
            /* Pinta a Mãe */
            > div > [data-baseweb="tab-list"] > button:nth-of-type(3) { background: #2ECC71 !important; }
            
            /* Pinta o FUNDO DO PAINEL (Tela toda fica esverdeada) */
            > [data-testid="stTabPanel"] {
                background: linear-gradient(180deg, #F0FFF4 0%, #FFFFFF 100%) !important; /* Verde suave */
                border-top: 5px solid #2ECC71 !important;
                box-shadow: 0 0 40px rgba(46, 204, 113, 0.2) !important;
            }

            /* Envelope vira Verde */
            [data-testid="stFileUploader"] { background-color: #F1FFF7 !important; border: 1px dashed #2ECC71 !important; }
            
            /* Texto das Filhas vira Verde */
            [data-testid="stTabPanel"] [aria-selected="true"] { color: #2ECC71 !important; border-bottom: 3px solid #2ECC71 !important; }
            
            /* Botão vira Verde */
            div.stDownloadButton > button:hover { background: #2ECC71 !important; color: white !important; }
        }

        /* =================================================================================
           5. ACABAMENTOS GERAIS
        ================================================================================= */
        
        /* O Grande Caixotão (Reset) */
        [data-testid="stTabPanel"] {
            background: #FFFFFF; 
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -10px !important;
            min-height: 800px !important;
        }

        /* Sub-abas Inativas (Cinza Prata) */
        [data-testid="stTabPanel"] .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F1F3F5 !important;
            border-radius: 15px 45px 0 0 !important; /* PASTA ESCOLAR */
            padding: 0 30px !important;
            transform: none !important;
        }

        /* Botões Prateados (Matando o Vermelho para sempre) */
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
