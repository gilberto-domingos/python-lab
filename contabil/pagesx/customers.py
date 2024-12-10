import streamlit as st


def show():
    st.subheader("Cadastro de clientes")
    cod = st.text_input("Código :")
    name = st.text_input("Nome :")
    cell = st.text_input("Célula :")
    email = st.text_input("Email:")
    phone = st.text_input("Celular :")
