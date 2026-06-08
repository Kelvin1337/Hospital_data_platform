import streamlit as st
import plotly.express as px
from src.utils.database import run_query

st.title("👨‍⚕️ Faturamento por Médico")
st.markdown("---")

df = run_query("""
    SELECT
        m.nome_medico AS medico,
        SUM(f.valor_faturamento) AS receita
    FROM CAMADA_OURO.FCT_INTERNACOES f
    JOIN CAMADA_OURO.DIM_MEDICOS m
        ON f.fk_medico = m.id_medico
    GROUP BY 1
    ORDER BY 2 DESC
""")

if not df.empty:
    fig = px.bar(
        df, 
        x="medico", 
        y="receita", 
        color="receita",
        labels={"medico": "Médico", "receita": "Receita (R$)"},
        color_continuous_scale="Cividis"
    )
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado para faturamento de médicos.")