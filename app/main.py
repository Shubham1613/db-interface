import streamlit as st
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

st.write("""
# Query Interface
""")

query = st.text_area('Write the sql query')
run = st.button('Run')
# st.write("""
# # Insert Data from CSV
# """)
#
# data = st.file_uploader('Upload CSV file')

conn = psycopg2.connect(
    dbname=os.getenv('DB_DBNAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    client_encoding='LATIN-1'
)

chunk_size = 10
chunks = []

if query and run :
    for chunk in pd.read_sql_query(query, conn, chunksize=10):
        chunks.append(chunk)  # Append each chunk to the list

# Concatenate all chunks into a single DataFrame (optional)
    df = pd.concat(chunks, ignore_index=True)
    st.dataframe(df, use_container_width=True)


