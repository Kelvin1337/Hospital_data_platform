# dashboard/src/pages/2_Hospitais.py
import streamlit as st
from src.utils.database import run_query

st.title("Performance por unidade hospitalar")
st.markdown("---")

def get_dados_hospitais():
    return run_query("""
        SELECT
            COALESCE(INITCAP(h.nome_hospital), 'Não Informado') AS hospital,
            SUM(f.valor_faturamento) AS receita
        FROM CAMADA_OURO.FCT_INTERNACOES f
        LEFT JOIN CAMADA_OURO.DIM_HOSPITAIS h
            ON f.fk_hospital = h.id_hospital
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 50
    """)

df = get_dados_hospitais()

if df is not None and not df.empty:
    st.subheader("Top 50 unidades por faturamento")
    st.markdown("---")
    
    max_receita = df['receita'].max()
    
    # Renderiza a lista otimizada limitada aos 50 primeiros
    for idx, row in df.iterrows():
        hospital = row['hospital']
        receita = row['receita']
        
        proporcao = receita / max_receita if max_receita > 0 else 0
        
        col_texto, col_barra = st.columns([2, 3])
        
        with col_texto:
            st.markdown(f"**{idx+1}. {hospital}**")
            st.caption(f"R$ {receita:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        
        with col_barra:
            st.progress(min(float(proporcao), 1.0))
            
        st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

else:
    st.warning("Nenhum dado de faturamento por hospital foi retornado pelo Snowflake.")