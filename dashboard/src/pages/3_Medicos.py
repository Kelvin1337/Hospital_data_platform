import streamlit as st
import plotly.express as px
from src.utils.database import run_query
from src.utils.formatters import fmt_brl

st.title("Análise do corpo clínico e diagnósticos")  # ← typo corrigido
st.markdown("---")


# ---------------------------------------------------------------------------
# Query com cache
# ---------------------------------------------------------------------------

@st.cache_data(ttl=600)
def get_condicoes():
    return run_query("""
        SELECT
            UPPER(condicoes_medicas)    AS condicao,
            COUNT(*)                   AS total_casos,
            SUM(valor_faturamento)     AS faturamento_associado
        FROM CAMADA_OURO.FCT_INTERNACOES
        WHERE condicoes_medicas IS NOT NULL
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 10
    """)


# ---------------------------------------------------------------------------
# Carregamento dos dados
# ---------------------------------------------------------------------------

df_condicoes = get_condicoes()

if df_condicoes is None or df_condicoes.empty:
    st.warning("Nenhum dado de condições médicas foi localizado.")
    st.stop()


# ---------------------------------------------------------------------------
# Gráfico: Top 10 Condições Médicas
# ---------------------------------------------------------------------------

st.subheader("Top 10 condições médicas mais frequentes")

fig = px.bar(
    df_condicoes,
    x="condicao",
    y="total_casos",
    color="faturamento_associado",
    text_auto=True,
    title="Frequência de internações por condição médica",
    labels={
        "condicao":               "Condição Médica",
        "total_casos":            "Número de Casos",
        "faturamento_associado":  "Faturamento",
    },
    color_continuous_scale="Blues")

fig.update_layout(
    template="plotly_dark",
    xaxis={"categoryorder": "total descending"},
    height=650,
    bargap = 0.5, 
    margin=dict(t=50, b=20),
    coloraxis_colorbar=dict(
        title="Faturamento",
        tickformat="$.2s",
        tickprefix="R$ ",
    ),
)


st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------------------------------
# Tabela: Detalhes financeiros por patologia
# ---------------------------------------------------------------------------

st.markdown("---")
st.subheader("Detalhes financeiros por patologia")

df_visual = df_condicoes.copy()
df_visual.columns = ["Condição Médica", "Total de Casos", "Faturamento Associado"]

st.dataframe(
    df_visual.style.format({
        "Total de Casos":        "{:,}".format,
        "Faturamento Associado": lambda x: fmt_brl(x),
    }),
    use_container_width=True,
    hide_index=True,
)