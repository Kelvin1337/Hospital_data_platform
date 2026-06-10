import streamlit as st
from src.utils.database import run_query
from src.utils.formatters import fmt_brl

st.title("Performance por unidade hospitalar")
st.markdown("---")


# ---------------------------------------------------------------------------
# Query com cache
# ---------------------------------------------------------------------------

@st.cache_data(ttl=600)
def get_dados_hospitais():
    return run_query("""
        SELECT
            COALESCE(INITCAP(h.nome_hospital), 'Não Informado') AS hospital,
            SUM(f.valor_faturamento)                            AS receita
        FROM CAMADA_OURO.FCT_INTERNACOES f
        LEFT JOIN CAMADA_OURO.DIM_HOSPITAIS h
            ON f.fk_hospital = h.id_hospital
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 50
    """)


# ---------------------------------------------------------------------------
# Carregamento dos dados
# ---------------------------------------------------------------------------

df = get_dados_hospitais()

if df is None or df.empty:
    st.warning("Nenhum dado de faturamento por hospital foi retornado pelo Snowflake.")
    st.stop()


# ---------------------------------------------------------------------------
# Ranking de hospitais
# ---------------------------------------------------------------------------

st.subheader("Top 50 unidades por faturamento")
st.markdown("---")

max_receita = df["receita"].max()

for rank, (_, row) in enumerate(df.iterrows(), start=1):
    hospital = row["hospital"]
    receita  = row["receita"]
    proporcao = float(receita / max_receita) if max_receita > 0 else 0.0

    col_texto, col_barra = st.columns([2, 3])

    with col_texto:
        st.markdown(f"**{rank}. {hospital}**")
        st.caption(fmt_brl(receita))

    with col_barra:
        # Barra colorida em HTML para refletir o tema neon do dashboard
        largura = round(proporcao * 100, 1)
        cor = (
        "#2563EB" if rank == 1
        else "#10B981" if rank <= 3
        else "#64748B"
        )

        st.markdown(
            f"""
            <div style="
                background: {cor};
                width: {largura}%;
                height: 8px;
                border-radius: 4px;
                margin-top: 14px;
                opacity: 0.85;
            "></div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)