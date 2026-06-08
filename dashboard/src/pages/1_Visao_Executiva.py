# dashboard/src/pages/1_Visao_Executiva.py
import streamlit as st
import plotly.express as px
import pandas as pd
from src.utils.database import run_query

st.title("Visão Executiva")
st.markdown("---")

# ==========================================
# 1. CARREGAMENTO DOS DADOS (Queries Corrigidas)
# ==========================================

# Query dos KPIs usando as colunas reais do seu Snowflake
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

# Query de evolução temporal usando DATA_ADMISSAO
df_evolucao = run_query("""
    SELECT
        DATE_TRUNC('month', data_admissao) AS mes,
        COUNT(*) AS qtd_internacoes,
        SUM(valor_faturamento) AS faturamento
    FROM CAMADA_OURO.FCT_INTERNACOES
    GROUP BY 1
    ORDER BY 1 ASC
""")

# ==========================================
# 2. RENDERIZAÇÃO DOS KPIs
# ==========================================
if df_kpis is not None and not df_kpis.empty:
    row = df_kpis.iloc[0]
    
    # Primeira Linha de KPIs (Idêntica ao topo do seu print)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Internações", value=f"{int(row['total_internacoes']):,}".replace(",", "."))
    with col2:
        st.metric(label="Faturamento Total", value=f"R$ {row['faturamento_total']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col3:
        st.metric(label="Ticket Médio", value=f"R$ {row['ticket_medio']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col4:
        st.metric(label="Dias Médios", value=f"{row['dias_medios']:.1f}".replace(".", ","))

    st.markdown("---")

    # Segunda Linha de KPIs (Meio do seu print)
    col5, col6, col7 = st.columns(3)
    with col5:
        st.metric(label="Pacientes", value=f"{int(row['total_pacientes']):,}".replace(",", "."))
    with col6:
        st.metric(label="Médicos", value=f"{int(row['total_medicos']):,}".replace(",", "."))
    with col7:
        st.metric(label="Hospitais", value=f"{int(row['total_hospitais']):,}".replace(",", "."))

else:
    st.error("Não foi possível carregar os KPIs da base de dados.")

st.markdown("---")

# ==========================================
# 3. RENDERIZAÇÃO DOS GRÁFICOS DE EVOLUÇÃO
# ==========================================
if df_evolucao is not None and not df_evolucao.empty:
    # Garante a tipagem de data para o Plotly ordenar o eixo X horizontal corretamente
    df_evolucao['mes'] = pd.to_datetime(df_evolucao['mes'])

    # ---- GRÁFICO 1: Evolução das Internações ----
    st.subheader("Evolução das Internações")
    fig_internacoes = px.line(
        df_evolucao,
        x="mes",
        y="qtd_internacoes",
        labels={"mes": "Tempo", "qtd_internacoes": "Quantidade de Internações"}
    )
    fig_internacoes.update_traces(line=dict(color="#4EA8DE", width=2))
    fig_internacoes.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=True, gridcolor="#262730"),
        yaxis=dict(showgrid=True, gridcolor="#262730"),
        height=300
    )
    st.plotly_chart(fig_internacoes, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    # ---- GRÁFICO 2: Evolução do Faturamento ----
    st.subheader("Evolução do Faturamento")
    fig_faturamento = px.line(
        df_evolucao,
        x="mes",
        y="faturamento",
        labels={"mes": "Tempo", "faturamento": "Faturamento (R$)"}
    )
    fig_faturamento.update_traces(line=dict(color="#4EA8DE", width=2))
    fig_faturamento.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=True, gridcolor="#262730"),
        yaxis=dict(showgrid=True, gridcolor="#262730"),
        height=300
    )
    st.plotly_chart(fig_faturamento, use_container_width=True)

else:
    st.info("Sem dados históricos para plotar os gráficos de evolução.")