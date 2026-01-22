import streamlit as st

def aplicar_estilo_sentinela():
    # Injeta o botão de Reset Visual no canto direito como uma segurança extra
    st.markdown("""
        <div id="botao-home-mestre" onclick="window.location.reload()">
            <span style="font-size: 24px;">🏠</span>
        </div>

        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR ETERNA --- */
        /* Impede que a barra lateral seja escondida ou minimizada */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            display: block !important;
            visibility: visible !important;
            position: relative !important;
            background-color: #F3E9DC !important;
            border-right: 2px solid #FF69B4 !important;
        }

        /* Remove o botão oficial de "X" para você nem ter a opção de fechar */
        [data-testid="sidebar-close-button"], 
        button[aria-label="Close sidebar"],
        .st-emotion-cache-6qob1r {
            display: none !important;
            visibility: hidden !important;
        }

        /* Ajusta o corpo da página para respeitar o espaço da sidebar fixa */
        .stMain {
            margin-left: 0px !important;
        }

        /* BOTÃO HOME (RESET) À DIREITA */
        #botao-home-mestre {
            position: fixed;
            right: 30px;
            top: 30px;
            width: 60px;
            height: 60px;
            background: linear-gradient(145deg, #FF69B4, #FF1493);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 1000000;
            box-shadow: 0 10px 25px rgba(255, 20, 147, 0.4);
            border: 2px solid white;
            transition: all 0.3s ease;
        }

        /* RESET DO LIXO VISUAL DO TOPO */
        header, .st-emotion-cache-zq59db, 
        #keyboard_double, .st-emotion-cache-10oheav, 
        span[data-testid="stHeaderActionElements"] {
            display: none !important;
        }

        /* FUNDO E TIPOGRAFIA BOUTIQUE */
        .stApp { background: radial-gradient(circle at top left, #FCF8F4 0%, #F3E9DC 100%) !important; }
        .block-container { padding-top: 2.5rem !important; }
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; font-size: 3.2rem; font-weight: 800; 
            letter-spacing: -1px; text-transform: uppercase;
        }
        .titulo-principal span { font-weight: 200 !important; color: #A67B5B; }

        .barra-marsala { 
            width: 60px; height: 3px; background: #FF69B4; 
            border-radius: 50px; margin-top: 10px; margin-bottom: 50px;
            box-shadow: 0 0 15px rgba(255, 105, 180, 0.8);
        }

        /* ABAS COM BRILHO ROSA */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        .stTabs [data-baseweb="tab"] {
            height: 48px !important; background: rgba(166, 123, 91, 0.15) !important;
            border-radius: 25px !important; padding: 0px 30px !important;
            font-size: 15px !important; color: #5D3A1A !important;
            transition: all 0.4s ease !important; border: 1px solid rgba(255, 255, 255, 0.5) !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-3px) !important; background: white !important;
            color: #FF69B4 !important; filter: brightness(1.1) !important;
            box-shadow: 0 12px 25px rgba(255, 105, 180, 0.4) !important; border-top: 2px solid #FF69B4 !important;
        }

        .stTabs [aria-selected="true"] { background: #5D3A1A !important; color: white !important; font-weight: 600; }

        /* BOTÃO ADM EXCLUSIVO */
        div.stButton > button:has(div:contains("ABRIR GESTÃO ADMINISTRATIVA")) {
            background: linear-gradient(145deg, #FF69B4, #FF1493) !important;
            color: #5D3A1A !important; border-radius: 40px !important;
            box-shadow: 0 10px 25px rgba(255, 20, 147, 0.5) !important; font-weight: 800 !important;
        }
        </style>
    """, unsafe_allow_html=True)
