import streamlit as st

def render_kpi_dashboard(total_pacientes: int, total_medicos: int, taxa_ocupacao: float):
    """
    Renderiza uma linha de KPIs padronizada.
    """
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total de Pacientes", value=f"{total_pacientes:,}")
    with col2:
        st.metric(label="Médicos Ativos", value=total_medicos)
    with col3:
        st.metric(label="Taxa de Ocupação", value=f"{taxa_ocupacao}%", delta="-2%")