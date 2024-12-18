import streamlit as st


def show():
    st.subheader("Regime tributário")
    cod_regime_tr = st.text_input("Código :")
    descr_regime_tr = st.text_input("Descrição :")
