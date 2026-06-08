import streamlit as st
import plotly.express as px
from src.utils.database import run_query

st.title("Faturamento por Hospital")
st.markdown("---")

# Criamos uma função local com cache para guardar o resultado dessa agregação
@st.cache_data(ttl=1200)  # Guarda por 20 minutos
def get_dados_hospitais():
    return run_query("""
        SELECT
            INITCAP(h.nome_hospital) AS hospital,
            SUM(f.valor_faturamento) AS receita
        FROM CAMADA_OURO.FCT_INTERNACOES f
        JOIN CAMADA_OURO.DIM_HOSPITAIS h
            ON f.fk_hospital = h.id_hospital
        GROUP BY 1
        ORDER BY 2 DESC
    """)

df = get_dados_hospitais()

if not df.empty:
    fig = px.bar(
        df, 
        x="hospital", 
        y="receita", 
        color="receita",
        labels={"hospital": "Hospital", "receita": "Receita (R$)"},
        color_continuous_scale="Viridis"
    )
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado para faturamento de hospitais.")