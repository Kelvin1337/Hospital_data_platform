import streamlit as st
import snowflake.connector
import pandas as pd
def get_connection():
    return snowflake.connector.connect(
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"],
        role=st.secrets["snowflake"]["role"]
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