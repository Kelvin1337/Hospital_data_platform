# dashboard/src/pages/5_Qualidade_Dados.py
import streamlit as st

st.title("📊 Qualidade de Dados (Data Quality)")
st.markdown("---")

st.info("Módulo destinado ao monitoramento de volumetria, testes do dbt (freshness, unique, not_null) e auditoria de cargas.")
# Aqui você pode ler logs ou metadados de testes