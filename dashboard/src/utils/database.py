import streamlit as st
import snowflake.connector
import pandas as pd

def get_connection():
    return snowflake.connector.connect(
        user=st.secrets["user"],
        password=st.secrets["password"],
        account=st.secrets["account"],
        warehouse=st.secrets["warehouse"],
        database=st.secrets["database"],
        schema=st.secrets["schema"]
    )
@st.cache_data(ttl=3600) # Guarda o resultado por 1 hora na memória do Streamlit
def run_query(query):
    try:
        conn = get_connection()
        df = pd.read_sql(query, conn)
        conn.close()
        
        # Transforma todas as colunas do Snowflake em minúsculo
        if df is not None and not df.empty:
            df.columns = df.columns.str.lower()
            
        return df
    except Exception as e:
        st.error(f"Erro na execução da query: '{e}'")
        return pd.DataFrame()