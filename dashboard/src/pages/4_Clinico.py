import streamlit as st
import plotly.express as px
from src.utils.database import run_query
from src.utils.formatters import fmt_int_br

st.title("Análise Clínica")
st.markdown("---")


# ---------------------------------------------------------------------------
# Queries com cache
# ---------------------------------------------------------------------------

@st.cache_data(ttl=600)
def get_doencas():
    return run_query("""
        SELECT
            condicoes_medicas,
            COUNT(*) AS qtd
        FROM CAMADA_OURO.FCT_INTERNACOES
        WHERE condicoes_medicas IS NOT NULL
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 10
    """)


@st.cache_data(ttl=600)
def get_testes():
    return run_query("""
        SELECT
            resultado_testes,
            COUNT(*) AS qtd
        FROM CAMADA_OURO.FCT_INTERNACOES
        WHERE resultado_testes IS NOT NULL
        GROUP BY 1
    """)


# ---------------------------------------------------------------------------
# Carregamento dos dados
# ---------------------------------------------------------------------------

doencas = get_doencas()
testes  = get_testes()

dados_ok = (
    doencas is not None and not doencas.empty and
    testes  is not None and not testes.empty
)

if not dados_ok:
    st.warning("Não foi possível carregar os dados clínicos. Verifique a conexão com o Snowflake.")
    st.stop()


# ---------------------------------------------------------------------------
# Mini KPIs de contexto
# ---------------------------------------------------------------------------

col_kpi1, col_kpi2 = st.columns(2)

with col_kpi1:
    condicao_top = str(doencas.iloc[0]["condicoes_medicas"])
    st.metric("Condição Mais Frequente", condicao_top)

with col_kpi2:
    total_testes = int(testes["qtd"].sum())
    st.metric("Total de Exames Analisados", fmt_int_br(total_testes))

st.markdown("---")


# ---------------------------------------------------------------------------
# Gráficos lado a lado
# ---------------------------------------------------------------------------

col1, col2 = st.columns(2)

# --- Gráfico 1: Top Condições Médicas (barras horizontais) ---
with col1:
    st.subheader("Top condições médicas")

    fig_bar = px.bar(
        doencas,
        x="qtd",
        y="condicoes_medicas",
        text_auto=True,
        orientation="h",
        title="Diagnósticos mais frequentes",
        labels={"condicoes_medicas": "Diagnóstico", "qtd": "Casos"},
        color="qtd",
        color_continuous_scale="Blues",
    )
    fig_bar.update_layout(
        template="plotly_dark",
        showlegend=False,
        coloraxis_showscale=False,
        yaxis={"categoryorder": "total ascending"},
        xaxis=dict(showgrid=True, gridcolor="#262730"),
        height=400,
        margin=dict(t=50, b=20),
    )
    st.plotly_chart(fig_bar, use_container_width=True)


# --- Gráfico 2: Resultados dos Testes (rosca) ---
with col2:
    st.subheader("Resultados dos testes laboratoriais")

    fig_donut = px.pie(
        testes,
        names="resultado_testes",
        values="qtd",
        hole=0.5,
        title="Distribuição dos resultados",
        color_discrete_sequence=[
       "#2563EB",
       "#60A5FA",
       "#10B981",
       "#64748B",
        ]
    )
    fig_donut.update_traces(
        textinfo="percent+label",
        pull=[0.05, 0, 0, 0],                          # destaque leve na maior fatia
        marker=dict(line=dict(color="#0E1117", width=2)),
    )
    fig_donut.update_layout(
        template="plotly_dark",
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
        height=400,
        margin=dict(t=50, b=20),
    )
    st.plotly_chart(fig_donut, use_container_width=True)