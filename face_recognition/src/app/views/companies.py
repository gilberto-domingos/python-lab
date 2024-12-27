import streamlit as st
import os
import pandas as pd
import random


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

        # Exibe a tabela no Streamlit com a configuração de coluna personalizada e sem índice
        st.dataframe(
            table,
            column_config={
                "name": st.column_config.TextColumn("Nome da Empresa"),
                "url": st.column_config.LinkColumn("URL da Empresa"),
                "stars": st.column_config.NumberColumn(
                    "Estrelas do GitHub",
                    help="Número de estrelas no GitHub",
                    format="%d ⭐",
                ),
                "views_history": st.column_config.LineChartColumn(
                    "Visualizações (últimos 30 dias)", y_min=0, y_max=5000
                ),
            },
            hide_index=True,
            use_container_width=True
        )

    except FileNotFoundError:
        st.error(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")


if __name__ == "__main__":
    show()
