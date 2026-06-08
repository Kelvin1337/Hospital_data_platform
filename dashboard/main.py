import streamlit as st
import sys
import os

# Garante que o Python enxergue a pasta 'src' no path de execução
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Configuração global da página - DEVE ser o primeiro comando Streamlit executado
st.set_page_config(
    page_title="Hospital Data Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definição das páginas usando a API moderna st.Page
paginas = {
    "Menu Principal": [
        st.Page("src/pages/1_Visao_Executiva.py", title="Visão Executiva", default=True)
    ],
    "Visões Operacionais": [
        st.Page("src/pages/2_Hospitais.py", title="Hospitais",),
        st.Page("src/pages/3_Medicos.py", title="Médicos",),
        st.Page("src/pages/4_Clinico.py", title="Análise Clínica",)
    ]
}

# Inicializa a navegação
nav = st.navigation(paginas)
nav.run()