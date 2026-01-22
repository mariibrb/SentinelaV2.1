/* --- 8. 🚀 BOTÕES ESTILIZADOS (COMBINANDO COM A ESTÉTICA) --- */
        /* Estilo Base para todos os botões */
        div.stButton > button {
            width: 100% !important;
            border-radius: 15px !important;
            height: 60px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            transition: all 0.3s ease !important;
            border: 2px solid #ADB5BD !important;
            background: linear-gradient(180deg, #FFFFFF 0%, #DEE2E6 100%) !important; /* Prata Diamante */
            color: #495057 !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
        }

        /* Efeito de Hover (Passar o mouse) */
        div.stButton > button:hover {
            transform: scale(1.02) !important;
            color: white !important;
            border-color: transparent !important;
        }

        /* BOTÃO DINÂMICO: Azul Neon quando estiver na aba ANÁLISE XML */
        .stTabs:has(button:nth-child(1)[aria-selected="true"]) div.stButton > button:hover {
            background: #00BFFF !important;
            box-shadow: 0 0 20px rgba(0, 191, 255, 0.6) !important;
        }

        /* BOTÃO DINÂMICO: Rosa Neon quando estiver na aba CONFORMIDADE DOMÍNIO */
        .stTabs:has(button:nth-child(2)[aria-selected="true"]) div.stButton > button:hover {
            background: #FF69B4 !important;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.6) !important;
        }

        /* Ajuste para os botões de Download (st.download_button) */
        div.stDownloadButton > button {
            background: #495057 !important;
            color: white !important;
            border: none !important;
            height: 50px !important;
        }

        div.stDownloadButton > button:hover {
            background: #212529 !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2) !important;
        }
