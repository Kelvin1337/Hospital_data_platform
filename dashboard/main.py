import streamlit as st
import sys
from pathlib import Path

# Garante que o Python enxergue a pasta 'src' no path de execução
sys.path.insert(0, str(Path(__file__).parent))

# ⚠️ set_page_config DEVE ser o primeiro comando Streamlit executado
st.set_page_config(
    page_title="Hospital Data Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilo global injetado uma única vez aqui no main ---
st.markdown("""
    <style>
        /* Remove padding excessivo do topo */
        .block-container {
            padding-top: 1.5rem;
        }

        /* Métrica: deixa o valor mais destacado */
        [data-testid="stMetricValue"] {
            font-size: 1.6rem;
            font-weight: 700;
        }

        /* Sidebar: identidade visual do produto */
        [data-testid="stSidebar"] {
            background-color: #0E1117;
            border-right: 1px solid #1E2130;
        }

        /* Divisores mais sutis */
        hr {
            border-color: #1E2130;
        }
    </style>
""", unsafe_allow_html=True)


# --- Definição das páginas usando a API moderna st.Page ---
paginas = {
    "Menu Principal": [
        st.Page("src/pages/1_Visao_Executiva.py", title="Visão Executiva", default=True),
    ],
    "Visões Operacionais": [
        st.Page("src/pages/2_Hospitais.py",  title="Hospitais"),
        st.Page("src/pages/3_Medicos.py",    title="Médicos"),
        st.Page("src/pages/4_Clinico.py",    title="Análise Clínica"),
    ],
}

# --- Inicializa a navegação ---
nav = st.navigation(paginas)
nav.run()