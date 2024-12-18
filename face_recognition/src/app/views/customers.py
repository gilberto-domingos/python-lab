import streamlit as st


def show():
    st.subheader("Cadastro de clientes")
    cod_customer = st.text_input("Código :")
    name_customer = st.text_input("Nome :")
    cell_customer = st.text_input("Célula :")
    email_customer = st.text_input("Email:")
    phone_customer = st.text_input("Celular :")
