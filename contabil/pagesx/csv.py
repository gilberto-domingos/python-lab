# pagesx/show_csv.py
import streamlit as st
import pandas as pd

def show():
    st.title("Conteúdo CSV")

    # Caminho para o arquivo CSV
    csv_file_path = './data/supermarket_sales.csv'  # Altere o caminho se necessário

    # Verifique se o arquivo existe
    try:
        df = pd.read_csv(csv_file_path)
        st.write("arquivo 'vendas.csv' :")
        st.dataframe(df)  # Exibe o DataFrame como uma tabela
    except FileNotFoundError:
        st.error("O arquivo CSV não foi encontrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")

