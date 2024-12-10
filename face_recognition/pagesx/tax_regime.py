import streamlit as st


def show():
    st.subheader("Regime tributário")
    cod_comp = st.text_input("Código :")
    descr_comp = st.text_input("Descrição :")
