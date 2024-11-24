import streamlit as st


def show():
    st.title("Página do Sistema")
    st.write("Conteúdo da página do sistemas.")

    st.markdown('<div class="teste">', unsafe_allow_html=True)
