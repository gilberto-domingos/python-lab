import streamlit as st


def show():
    st.subheader("Tipo de empresa")
    cod_company = st.text_input("Código :")
    descr_company = st.text_input("Descrição :")
