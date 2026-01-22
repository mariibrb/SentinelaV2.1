import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

        /* --- TRAVA MESTRE: SIDEBAR --- */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            background-color: #F3E9DC !important; 
            border-right: 4px solid #FF69B4 !important; /* Borda da sidebar mais forte */
            z-index: 999999 !important;
            box-shadow: 10px 0 30px rgba(0,0,0,0.1) !important;
        }

        /* RESET DO LIXO VISUAL */
        header, [data-testid="stHeader"] { display: none !important; }

        /* FUNDO MOCHA MOUSSE */
        .stApp { 
            background: radial-gradient(circle at top left, #FCF8F4 0%, #E8DCCB 100%) !important; 
        }
        
        html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* --- TÍTULO DESIGNER: SENTINELA 2.1 --- */
        .titulo-principal { 
            font-family: 'Montserrat', sans-serif !important;
            color: #5D3A1A; 
            font-size: 3.5rem; 
            font-weight: 800; 
            margin-bottom: 5px;
            letter-spacing: -1.5px;
            text-transform: uppercase;
            line-height: 1;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        .subtitulo-versao {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #A67B5B;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: -10px;
            margin-bottom: 40px;
            letter-spacing: 1px;
        }

        /* LINHA GLOW ROSA ABAIXO DO TÍTULO */
        .linha-glow {
            width: 150px;
            height: 3px;
            background: #FF69B4;
            border-radius: 50px;
            box-shadow: 0 0 15px #FF69B4, 0 0 30px rgba(255, 105, 180, 0.4);
            margin-bottom: 50px;
        }

        /* --- ESTILO BASE DAS ABAS (FICHÁRIO METALIZADO INATIVO) --- */
        .stTabs [data-baseweb="tab-border"] { display: none !important; }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px !important; /* Espaçamento entre as abas mãe */
            background-color: transparent !important;
            padding: 20px 0 !important;
            align-items: flex-end; /* Alinha as abas por baixo para criar o efeito cascata */
        }

        .stTabs [data-baseweb="tab"] {
            height: 80px !important; /* Mais altas */
            background: linear-gradient(180deg, #F0F0F0 0%, #C0C0C0 100%) !important; /* Metal Cinza */
            border-radius: 28px 70px 0 0 !important; /* Curva de Fichário Acentuada */
            margin-right: -25px !important; /* Sobreposição maior */
            padding: 0px 60px !important; /* Mais preenchimento */
            border: 2px solid #A0A0A0 !important;
            font-size: 1.6rem !important; /* Texto maior */
            font-weight: 800 !important;
            color: #616161 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: inset 0 3px 5px rgba(255,255,255,0.7), 8px 0 20px rgba(0,0,0,0.2) !important; /* Brilho interno e sombra */
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
            position: relative; /* Para o efeito de "pasta" */
            bottom: 0;
            align-self: flex-end; /* Garante alinhamento na base */
        }

        /* --- ABAS MÃE ATIVAS (GLOW INTENSO) --- */

        /* 🔵 ANÁLISE XML: AZUL CROMADO + GLOW */
        .stTabs [data-baseweb="tab"]:has(div:contains("XML"))[aria-selected="true"] {
            background: linear-gradient(145deg, #A7E9FF 0%, #00BFFF 100%) !important; /* Azul Cromado */
            color: white !important;
            transform: translateY(-20px) scale(1.08) !important; /* Salto maior e escala */
            border: 3px solid #00D1FF !important;
            box-shadow: 0 0 25px #00D1FF, 0 0 50px rgba(0, 209, 255, 0.6), inset 0 5px 10px rgba(255,255,255,0.8) !important; /* GLOW MULTICAMADAS */
            z-index: 100 !important;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.3) !important;
        }

        /* 💗 CONFORMIDADE: ROSA PINK GLOSS + GLOW */
        .stTabs [data-baseweb="tab"]:has(div:contains("CONFORMIDADE"))[aria-selected="true"] {
            background: linear-gradient(145deg, #FFB6C1 0%, #FF1493 100%) !important; /* Rosa Pink Gloss */
            color: white !important;
            transform: translateY(-20px) scale(1.08) !important; /* Salto maior e escala */
            border: 3px solid #FF69B4 !important;
            box-shadow: 0 0 25px #FF69B4, 0 0 50px rgba(255, 105, 180, 0.6), inset 0 5px 10px rgba(255,255,255,0.8) !important; /* GLOW MULTICAMADAS */
            z-index: 100 !important;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.3) !important;
        }

        /* --- SUB-ABAS (DIVISÓRIAS INTERNAS) --- */
        /* Estilo para parecer uma "gaveta" dentro da pasta mãe */
        .stTabs .stTabs [data-baseweb="tab-list"] {
            gap: 10px !important;
            padding: 15px 0 15px 40px !important; /* Recuo da sub-lista */
            border-left: 4px dashed #FFB6C1 !important; /* Linha conectora */
            margin-top: 20px !important;
            align-items: center; /* Alinha sub-abas no centro */
        }

        .stTabs .stTabs [data-baseweb="tab"] {
            height: 55px !important; /* Menor que as mães */
            background: linear-gradient(145deg, #F0F0F0 0%, #E0E0E0 100%) !important; /* Metal mais suave */
            border-radius: 18px 45px 0 0 !important; /* Curva de sub-divisória */
            margin-right: -10px !important;
            padding: 0px 35px !important;
            border: 1px solid #D1D1D1 !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            color: #888888 !important;
            box-shadow: inset 0 2px 3px rgba(255,255,255,0.5), 3px 0 8px rgba(0,0,0,0.1) !important;
            transform: none !important; /* Resetar transform da aba mãe */
            align-self: center; /* Garante alinhamento */
        }

        /* SUB-ABA ATIVA (GLOW ROSA) */
        .stTabs .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(145deg, #FFD1DC 0%, #FFB6C1 100%) !important; /* Rosa Suave */
            color: #C71585 !important;
            transform: scale(1.05) !important; /* Aumenta um pouco */
            border: 2px solid #FF69B4 !important;
            box-shadow: 0 0 15px #FF69B4, 0 0 30px rgba(255, 105, 180, 0.5), inset 0 3px 5px rgba(255,255,255,0.7) !important; /* GLOW SUTIL */
            z-index: 10 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2) !important;
        }

        /* EFEITO HOVER (passar o mouse): LEVE BRILHO */
        .stTabs [data-baseweb="tab"]:hover {
            filter: brightness(1.15) saturate(1.1) !important;
            transform: translateY(-5px) !important;
            cursor: pointer !important;
        }

        /* --- BOTÕES DO SISTEMA (MOCHA METAL) --- */
        .stButton > button {
            width: 100%;
            background: linear-gradient(145deg, #C2936E, #8B5A2B) !important;
            color: #FFFFFF !important;
            border-radius: 40px !important;
            padding: 12px 25px !important;
            font-weight: 700 !important;
            box-shadow: 0 8px 20px rgba(139, 90, 43, 0.3), inset 0 2px 5px rgba(255,255,255,0.4) !important;
            text-transform: uppercase;
            transition: all 0.3s ease !important;
        }
        .stButton > button:hover {
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 12px 25px rgba(255, 105, 180, 0.5), inset 0 2px 5px rgba(255,255,255,0.5) !important;
            filter: brightness(1.1) !important;
        }
        </style>
    """, unsafe_allow_html=True)
