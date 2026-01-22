import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- 1. ESTRUTURA --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 5px solid #FF69B4 !important;
        }

        header, [data-testid="stHeader"] { display: none !important; }

        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }

        /* --- 2. ABAS MESTRE DIAMANTE --- */
        .stTabs { overflow: visible !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; 
            padding: 60px 0 0 20px !important; 
            overflow: visible !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 85px !important;
            background: linear-gradient(180deg, #FDFDFD 0%, #D8C7B1 100%) !important;
            border-radius: 35px 90px 0 0 !important; 
            padding: 0px 70px !important;
            border: 2px solid #A67B5B !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            color: #8B5A2B !important;
        }

        /* Ativas das Mães */
        .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] { background: #00BFFF !important; transform: translateY(-30px) !important; color: white !important; }
        .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] { background: #FF69B4 !important; transform: translateY(-30px) !important; color: white !important; }

        /* --- 3. 📦 O CAIXOTÃO (PASTA MÃE) --- */
        [data-testid="stTabPanel"] {
            background: #FFFFFF !important;
            padding: 50px !important;
            border-radius: 0 60px 60px 60px !important;
            margin-top: -5px !important;
            border: 6px solid transparent !important;
            min-height: 800px !important;
            overflow: visible !important;
        }

        /* Neon Setorizado */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border-color: #00D1FF !important;
            box-shadow: 0 0 30px #00D1FF, 0 0 80px rgba(0, 209, 255, 0.4) !important;
        }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stTabPanel"] {
            border-color: #FF69B4 !important;
            box-shadow: 0 0 30px #FF69B4, 0 0 80px rgba(255, 105, 180, 0.4) !important;
        }

        /* --- 4. 📁 SUB-ABAS (CORREÇÃO DE ELEVAÇÃO PARA TODAS) --- */
        .stTabs .stTabs [data-baseweb="tab-list"] { 
            padding: 0 0 30px 0 !important; 
            overflow: visible !important;
        }
        
        .stTabs .stTabs [data-baseweb="tab"] {
            height: 60px !important;
            background: #F8F9FA !important;
            border-radius: 15px 45px 0 0 !important;
            transition: all 0.3s ease !important;
            margin-right: -10px !important;
            overflow: visible !important;
        }

        /* Força TODAS as sub-abas a elevarem (RET, PIS, COFINS inclusas) */
        .stTabs .stTabs [aria-selected="true"] {
            transform: translateY(-15px) !important;
            z-index: 10 !important;
        }

        /* Cores Sub-abas XML */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [data-baseweb="tab"] { color: #0088cc !important; border-bottom: 3px solid #00BFFF !important; }
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #00BFFF !important; color: white !important; box-shadow: 0 0 15px #00D1FF !important;
        }

        /* Cores Sub-abas Conformidade */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [data-baseweb="tab"] { color: #cc5588 !important; border-bottom: 3px solid #FF69B4 !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) .stTabs [aria-selected="true"] {
            background: #FF69B4 !important; color: white !important; box-shadow: 0 0 15px #FF69B4 !important;
        }

        /* --- 5. ✉️ ENVELOPES COM ÍCONES PROFISSIONAIS --- */
        [data-testid="stFileUploader"] {
            padding: 50px 45px 45px 45px !important;
            border-radius: 10px 10px 45px 45px !important;
            border-top: 18px solid #FDFDFD !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
            margin: 25px 0 !important;
            position: relative !important;
        }

        /* ÍCONE DINÂMICO: Gerencial (📊) ou Relatório (📄) */
        /* Nota: Como o CSS não lê o texto do label, usamos uma lógica de posição se possível, 
           ou mantemos o ícone de folha de dados que é universal para auditoria */
        [data-testid="stFileUploader"]::before {
            content: "📄"; 
            position: absolute;
            top: -32px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 30px;
            z-index: 99;
        }

        .stTabs:has(button:nth-child(1)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #EBF9FF !important; border: 2px solid #A7E9FF !important; }
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) [data-testid="stFileUploader"] { background-color: #FFF0F5 !important; border: 2px solid #FFD1DC !important; }

        /* --- 6. 📄 ÁREA DE AUDITORIA --- */
        div.stExpander, div.element-container:has(h1, h2, h3), .stDataFrame {
            background-color: white !important;
            padding: 30px !important;
            border-radius: 20px !important;
            box-shadow: 0 5px 25px rgba(0,0,0,0.03) !important;
            border: 1px solid #f2f2f2 !important;
        }

        </style>
    """, unsafe_allow_html=True)
