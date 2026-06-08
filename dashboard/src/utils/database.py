import streamlit as st
import snowflake.connector
import pandas as pd

@st.cache_resource
def get_connection():
    """Mantém a conexão com o Snowflake ativa em cache rodando em segundo plano"""
    return snowflake.connector.connect(
        user=st.secrets["user"],
        password=st.secrets["password"],
        account=st.secrets["account"],
        warehouse=st.secrets["warehouse"],
        database=st.secrets["database"],
        schema=st.secrets["schema"]
    )

@st.cache_data(ttl=600)  # Cache de dados por 10 minutos para não estourar o orçamento do Snowflake
def run_query(sql: str) -> pd.DataFrame:
    """Executa a query e higieniza as colunas convertendo-as para minúsculo"""
    try:
        conn = get_connection()
        df = pd.read_sql(sql, conn)
        
        if df is not None and not df.empty:
            df.columns = df.columns.str.lower()  # Padroniza maiúsculas do Snowflake para minúsculas
        return df
    except Exception as e:
        st.error(f"Erro na execução da query: {e}")
        return pd.DataFrame()

def format_number(value):
    """Formata números para o padrão brasileiro (ex: 1.500)"""
    try:
        value = float(value)
        return f"{value:,.0f}".replace(",", ".")
    except:
        return "0"