import streamlit as st
import plotly.express as px
from src.utils.database import run_query

st.title("Análise Clínica")
st.markdown("---")

# --- 1. Queries de Dados ---
doencas = run_query("""
    SELECT condicoes_medicas, COUNT(*) AS qtd
    FROM CAMADA_OURO.FCT_INTERNACOES
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
""")

testes = run_query("""
    SELECT resultado_testes, COUNT(*) AS qtd
    FROM CAMADA_OURO.FCT_INTERNACOES
    GROUP BY 1
""")

# --- 2. Linha de Mini KPIs Clínicos para dar Contexto ---
if not doencas.empty and not testes.empty:
    col_kpi1, col_kpi2 = st.columns(2)
    with col_kpi1:
        condicao_top = doencas.iloc[0]['condicoes_medicas']
        st.metric(label="Condição Mais Frequente", value=str(condicao_top))
    with col_kpi2:
        total_testes = testes['qtd'].sum()
        st.metric(label="Total de Exames Analisados", value=f"{int(total_testes):,}".replace(",", "."))
    
    st.markdown("---")

# --- 3. Gráficos Lado a Lado Repaginados ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Condições Médicas")
    if not doencas.empty:
        fig1 = px.bar(
            doencas, 
            x="qtd",                      # Invertemos os eixos para barras horizontais (fica mais elegante para textos longos)
            y="condicoes_medicas", 
            text_auto='.s',
            orientation='h',
            labels={"condicoes_medicas": "Diagnóstico", "qtd": "Casos"},
            color="qtd",
            color_continuous_scale="Tealgrn" # Paleta puxada para o verde hospitalar/teal
        )
        fig1.update_layout(
            template="plotly_dark",
            showlegend=False,
            coloraxis_showscale=False,
            yaxis={'categoryorder':'total ascending'}, # Ordena a maior barra para o topo
            xaxis=dict(showgrid=True, gridcolor="#262730"),
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("Sem dados de condições médicas.")

with col2:
    st.subheader("Resultados dos Testes Laboratoriais")
    if not testes.empty:
        # Transformando a pizza antiga em uma Rosca Moderna (Donut)
        fig2 = px.pie(
            testes, 
            names="resultado_testes", 
            values="qtd",
            hole=0.5, # Define o furo central da rosca
            color_discrete_sequence=px.colors.qualitative.D3
        )
        fig2.update_traces(textinfo='percent+label', pull=[0.05, 0, 0]) # Dá um leve destaque na primeira fatia
        fig2.update_layout(
            template="plotly_dark",
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5), # Legenda na horizontal abaixo do gráfico
            height=400
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Sem dados de testes clínicos.")