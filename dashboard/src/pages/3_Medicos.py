# dashboard/src/pages/3_Medicos.py
import streamlit as st
import plotly.express as px
from src.utils.database import run_query

st.title("Análise do corpo clínico e iagnósticos")
st.markdown("---")

st.subheader("Top 10 Condições Médicas Mais Frequentes")

# Buscando as top condições direto da fato
df_condicoes = run_query("""
    SELECT 
        UPPER(condicoes_medicas) AS condicao,
        COUNT(*) AS total_casos,
        SUM(valor_faturamento) AS faturamento_associado
    FROM CAMADA_OURO.FCT_INTERNACOES
    WHERE condicoes_medicas IS NOT NULL
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
""")

if df_condicoes is not None and not df_condicoes.empty:
    
    # 🌈 1. AJUSTE NO GRÁFICO: Formatação sênior e intuitiva
    fig = px.bar(
        df_condicoes,
        x="condicao",
        y="total_casos",
        color="faturamento_associado",
        text_auto=True,
        labels={
            "condicao": "Condição Médica", 
            "total_casos": "Número de Casos", 
            "faturamento_associado": "Faturamento"
        },
        color_continuous_scale="Cividis"
    )
    
    fig.update_layout(
        template="plotly_dark",
        xaxis={'categoryorder':'total descending'},
        height=450,
        # Formata o faturamento na barra lateral para o padrão compacto (Ex: 1.4M)
        coloraxis_colorbar=dict(
            title="Faturamento",
            tickformat="$.2s", # Padrão internacional de compactação de BI
            tickprefix="R$ "
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Detalhes financeiros por patologia")
    
    # 💎 2. AJUSTE NA TABELA: Exibição limpa e profissional
    # Criamos uma cópia para não estragar a tipagem dos dados originais
    df_visual = df_condicoes.copy()
    
    # Renomeando as colunas para o usuário final
    df_visual.columns = ["Condição Médica", "Total de Casos", "Faturamento Associado"]
    
    # Formatando a tabela nativamente usando o styler do Pandas (evita o número por extenso feio)
    st.dataframe(
        df_visual.style.format({
            "Total de Casos": "{:,}".format,
            "Faturamento Associado": lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        }),
        use_container_width=True,
        hide_index=True # Remove a coluna de índices (0, 1, 2...) que polui o layout
    )
    
else:
    st.warning("Nenhum dado de condições médicas foi localizado.")