import streamlit as st
import os
import pandas as pd


def show():
    st.title("Empresas")

    # Obtém o caminho do arquivo Excel
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data/empresas.xlsx")

    try:
        # Lê o arquivo Excel ignorando as primeiras linhas irrelevantes
        table = pd.read_excel(file_path, skiprows=2)

        # Renomeia colunas para remover valores 'Unnamed'
        table.columns = [col if not col.startswith(
            "Unnamed") else "" for col in table.columns]
        table = table.loc[:, table.columns != ""]  # Remove colunas vazias

        # Corrige a coluna 'Telefone' (remover .0 e garantir que seja texto)
        if 'Telefone' in table.columns:
            table['Telefone'] = table['Telefone'].apply(
                lambda x: str(int(x)) if pd.notnull(x) else '')

        # Exibe a tabela no Streamlit sem índice
        st.dataframe(table.reset_index(drop=True))
    except FileNotFoundError:
        st.error(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")


if __name__ == "__main__":
    show()
