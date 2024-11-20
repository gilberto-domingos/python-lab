import pandas as pd
import streamlit as st


def show():
    try:
        st.title("Empresas")

    except FileNotFoundError:
        st.error(
            "Arquivo 'situation.xlsx' não encontrado. Verifique o caminho e tente novamente."
        )
        st.stop()
