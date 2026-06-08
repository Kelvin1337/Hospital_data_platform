import streamlit as st
import pandas as pd

def render_hospital_filters(df: pd.DataFrame):
    """
    Renderiza filtros padrão na barra lateral e retorna os dados filtrados.
    """
    st.sidebar.header("Filtros Globais")
    
    # Exemplo: Filtro por Hospital (se a coluna existir no DF)
    if "nome_hospital" in df.columns:
        hospitais = ["Todos"] + list(df["nome_hospital"].unique())
        hospital_selecionado = st.sidebar.selectbox("Selecione o Hospital", hospitais)
        
        if hospital_selecionado != "Todos":
            df = df[df["nome_hospital"] == hospital_selecionado]
            
    return df