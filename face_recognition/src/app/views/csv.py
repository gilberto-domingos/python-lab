import streamlit as st
import pandas as pd
import os


def show():
    st.title("Conteúdo CSV")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, "../data/supermarket_sales.csv")

    try:
        df = pd.read_csv(csv_file_path)
        st.write("arquivo 'vendas.csv' :")
        st.dataframe(df)  # Exibe o DataFrame como uma tabela
    except FileNotFoundError:
        st.error("O arquivo CSV não foi encontrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
