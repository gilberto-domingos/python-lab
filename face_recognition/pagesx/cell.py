import streamlit as st


def show():
    st.subheader("Cadastro de Células")
    cod_cell = st.text_input("Código : ")
    cell_name = st.text_input("Nome da célula : ")
    email_cell = st.text_input("Email da célula : ")
