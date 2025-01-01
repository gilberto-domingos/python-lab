import streamlit as st
import pandas as pd
import os

SAVE_PATH = "src/balance"
os.makedirs(SAVE_PATH, exist_ok=True)


def show():
    st.title("Uploads de balanços")

    st.subheader("Arquivos salvos na pasta:")
    files = os.listdir(SAVE_PATH)
    if files:
        for file in files:
            st.write(f"- {file}")
    else:
        st.write("Nenhum arquivo salvo na pasta.")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo Excel (.xlsx)",
        type=["xlsx"]
    )

    if uploaded_file is not None:
        try:
            file_path = os.path.join(SAVE_PATH, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success("O arquivo foi salvo!")

            dataframe = pd.read_excel(uploaded_file)
            st.write("Visualização dos dados carregados:")
            st.dataframe(dataframe)

            st.write("Dimensões do DataFrame:")
            st.write(f"Linhas: {dataframe.shape[0]}, Colunas: {
                     dataframe.shape[1]}")

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")
    else:
        st.info("Por favor, envie um arquivo Excel (.xlsx).")
