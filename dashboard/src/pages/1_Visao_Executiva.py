# dashboard/src/pages/1_Visao_Executiva.py
import streamlit as st
import plotly.express as px
import pandas as pd
from src.utils.database import run_query

st.title("Visão Executiva")
st.markdown("---")

def format_compact(value):
    """Formata números grandes para o padrão K, M, B com separador brasileiro"""
    try:
        val = float(value)
        if val >= 1_000_000_000:
            return f"R$ {val / 1_000_000_000:.2f} B".replace('.', ',')
        elif val >= 1_000_000:
            return f"R$ {val / 1_000_000:.2f} M".replace('.', ',')
        elif val >= 1_000:
            return f"R$ {val / 1_000:.1f} K".replace('.', ',')
        return f"R$ {val:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except:
        return "R$ 0,00"

# --- Queries ---
df_kpis = run_query("""
    SELECT
        COUNT(*) AS total_internacoes,
        SUM(valor_faturamento) AS faturamento_total,
        AVG(valor_faturamento) AS ticket_medio,
        AVG(dias_internado) AS dias_medios,
        COUNT(DISTINCT fk_paciente) AS total_pacientes,
        COUNT(DISTINCT fk_medico) AS total_medicos,
        COUNT(DISTINCT fk_hospital) AS total_hospitais
    FROM CAMADA_OURO.FCT_INTERNACOES
""")

df_evolucao = run_query("""
    SELECT
        DATE_TRUNC('month', data_admissao) AS mes,
        COUNT(*) AS qtd_internacoes,
        SUM(valor_faturamento) AS faturamento
    FROM CAMADA_OURO.FCT_INTERNACOES
    GROUP BY 1
    ORDER BY 1 ASC
""")

if df_kpis is not None and not df_kpis.empty:
    row = df_kpis.iloc[0]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Internações", value=f"{int(row['total_internacoes']):,}".replace(",", "."))
    with col2:
        # Aqui entra a formatação corrigida (Ex: R$ 1,42 B)
        st.metric(label="Faturamento Total", value=format_compact(row['faturamento_total']))
    with col3:
        st.metric(label="Ticket Médio", value=f"R$ {row['ticket_medio']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col4:
        st.metric(label="Dias Médios", value=f"{row['dias_medios']:.1f}".replace(".", ","))

    st.markdown("---")

    col5, col6, col7 = st.columns(3)
    with col5:
        st.metric(label="Pacientes", value=f"{int(row['total_pacientes']):,}".replace(",", "."))
    with col6:
        st.metric(label="Médicos", value=f"{int(row['total_medicos']):,}".replace(",", "."))
    with col7:
        st.metric(label="Hospitais", value=f"{int(row['total_hospitais']):,}".replace(",", "."))

# --- GRÁFICO 1: Evolução das Internações (Azul Elétrico Neon) ---
st.subheader("Evolução temporal de internações")
fig_internacoes = px.line(
    df_evolucao,
    x="mes",
    y="qtd_internacoes",
    labels={"mes": "Tempo", "qtd_internacoes": "Quantidade"}
)
# Linha grossa azul cyan brilhante com marcadores nos pontos
fig_internacoes.update_traces(line=dict(color="#00E5FF", width=3), mode="lines+markers", marker=dict(size=6))
fig_internacoes.update_layout(
    template="plotly_dark",
    xaxis=dict(showgrid=True, gridcolor="#262730"),
    yaxis=dict(showgrid=True, gridcolor="#262730"),
    height=300
)
st.plotly_chart(fig_internacoes, use_container_width=True)

st.html("<br>")

# --- GRÁFICO 2: Evolução do Faturamento (Pink/Magenta Neon) ---
st.subheader("Evolução temporal do faturamento")
fig_faturamento = px.area(  # Mudamos para área preenchida para dar mais volume de cor na tela
    df_evolucao,
    x="mes",
    y="faturamento",
    labels={"mes": "Tempo", "faturamento": "Faturamento (R$)"}
)
# Linha magenta com preenchimento gradiente sutil abaixo dela
fig_faturamento.update_traces(line=dict(color="#FF007F", width=3), fillcolor="rgba(255, 0, 127, 0.2)")
fig_faturamento.update_layout(
    template="plotly_dark",
    xaxis=dict(showgrid=True, gridcolor="#262730"),
    yaxis=dict(showgrid=True, gridcolor="#262730"),
    height=300
)
st.plotly_chart(fig_faturamento, use_container_width=True)