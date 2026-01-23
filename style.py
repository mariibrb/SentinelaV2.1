import streamlit as st

def aplicar_estilo_sentinela():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Plus+Jakarta+Sans:wght@500;800&display=swap');

        /* 1. FUNDO CHUMBO PROFUNDO (MAIS CLARO QUE O PRETO) */
        [data-testid="stSidebar"] { 
            background-color: #1A1C21 !important; 
            border-right: 3px solid #343A40 !important; 
        }
        header, [data-testid="stHeader"] { display: none !important; }
        
        .stApp { 
            background: linear-gradient(135deg, #212529 0%, #111317 100%) !important; 
            color: #FFFFFF !important;
        }

        /* TÍTULO E VERSÃO */
        .titulo-principal { 
            font-family: 'Orbitron', sans-serif !important; 
            color: #ADB5BD !important; 
            font-size: 0.9rem !important; 
            font-weight: 800; 
            text-transform: uppercase; 
            letter-spacing: 3px;
            padding: 5px 0 !important;
        }

        /* =================================================================================
           2. MENU MASTER - CORES SÓLIDAS E TEXTO BRANCO
        ================================================================================= */
        [role="radiogroup"] { 
            display: flex; 
            justify-content: center; 
            gap: 15px; 
            padding: 25px 0 !important;
        }
        
        [role="radiogroup"] label > div:first-child { display: none !important; }

        /* Botão Inativo (Chumbo com borda) */
        [role="radiogroup"] label {
            background: #2D3238 !important;
            border: 2px solid #495057 !important;
            border-radius: 10px 30px 5px 30px !important; 
            padding: 15px 30px !important;
            min-width: 240px; 
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 800;
            color: #CED4DA !important; /* Texto claro mas discreto */
            cursor: pointer !important;
            transition: all 0.3s ease;
            text-align: center;
        }

        /* 🟦 XML - AZUL TOTAL */
        div:has(#modulo-xml) [role="radiogroup"] label[data-checked="true"] {
            background: #00BFFF !important;
            color: #FFFFFF !important; /* TEXTO BRANCO PURO */
            border: none !important;
            box-shadow: 0 0 25px #00BFFF;
            transform: translateY(-10px);
            text-shadow: 1px 1px 5px rgba(0,0,0,0.3);
        }

        /* 🟥 CONFORMIDADE - ROSA TOTAL */
        div:has(#modulo-conformidade) [role="radiogroup"] label[data-checked="true"] {
            background: #FF00E5 !important;
            color: #FFFFFF !important; /* TEXTO BRANCO PURO */
            border: none !important;
            box-shadow: 0 0 25px #FF00E5;
            transform: translateY(-10px);
            text-shadow: 1px 1px 5px rgba(0,0,0,0.3);
        }

        /* 🟩 APURAÇÃO - VERDE TOTAL */
        div:has(#modulo-apuracao) [role="radiogroup"] label[data-checked="true"] {
            background: #00FF94 !important;
            color: #000000 !important; /* Texto preto no verde pra dar leitura */
            border: none !important;
            box-shadow: 0 0 25px #00FF94;
            transform: translateY(-10px);
            font-weight: 900;
        }

        /* =================================================================================
           3. ABAS FILHAS - PREENCHIMENTO E LEITURA
        ================================================================================= */
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background: #343A40 !important;
            border: 1px solid #495057 !important;
            border-radius: 8px 25px 0 0 !important;
            color: #DEE2E6 !important;
            font-weight: 700;
            margin-right: 8px;
        }

        /* Abas Internas Ativas */
        div:has(#modulo-xml) .stTabs [aria-selected="true"] { background: #00BFFF !important; color: white !important; }
        div:has(#modulo-conformidade) .stTabs [aria-selected="true"] { background: #FF00E5 !important; color: white !important; }
        div:has(#modulo-apuracao) .stTabs [aria-selected="true"] { background: #00FF94 !important; color: black !important; }

        /* =================================================================================
           4. ENVELOPES - CHUMBO COM NEON 📄
        ================================================================================= */
        [data-testid="stFileUploader"] {
            background: #2D3238 !important;
            border: 2px solid #495057 !important;
            border-radius: 15px !important;
            padding: 40px !important;
            color: #FFFFFF !important;
        }

        [data-testid="stFileUploader"] section { color: #FFFFFF !important; }
        [data-testid="stFileUploader"] label { color: #ADB5BD !important; font-size: 1.1rem !important; }

        /* Cores Neon nas bordas do envelope */
        div:has(#modulo-xml) [data-testid="stFileUploader"] { border-color: #00BFFF !important; box-shadow: 0 0 15px rgba(0, 191, 255, 0.2); }
        div:has(#modulo-conformidade) [data-testid="stFileUploader"] { border-color: #FF00E5 !important; box-shadow: 0 0 15px rgba(255, 0, 229, 0.2); }
        div:has(#modulo-apuracao) [data-testid="stFileUploader"] { border-color: #00FF94 !important; box-shadow: 0 0 15px rgba(0, 255, 148, 0.2); }

        /* =================================================================================
           5. CAIXOTÃO E BOTÕES
        ================================================================================= */
        [data-testid="stTabPanel"] {
            background: #1A1C21 !important;
            border: 1px solid #343A40;
            border-radius: 0 20px 20px 20px !important;
            padding: 30px !important;
            border-top: 6px solid !important;
        }
        
        /* Botões de Download (Verde Neon sempre) */
        div.stDownloadButton > button {
            background: #00FF94 !important;
            color: #000000 !important;
            border: none !important;
            font-weight: 800 !important;
            font-family: 'Orbitron', sans-serif !important;
            box-shadow: 0 0 15px rgba(0, 255, 148, 0.4);
        }

        /* Botões Normais */
        div.stButton > button {
            background: #343A40 !important;
            color: white !important;
            border: 1px solid #495057 !important;
        }

        </style>
    """, unsafe_allow_html=True)
