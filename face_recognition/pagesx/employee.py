import streamlit as st


def show():
    st.subheader("Cadastro de funcionários")
    cod_employee = st.text_input("Código :")
    name_employee = st.text_input("Nome :")
    email_employee = st.text_input("Email:")
    phone_employee = st.text_input("Celular :")
