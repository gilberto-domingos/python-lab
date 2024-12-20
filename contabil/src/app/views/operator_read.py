import streamlit as st
from pathlib import Path
import pandas as pd
from src.database.operator_database import Database


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/operator_read.css")
    load_css(css_path)

    db = Database()

    st.title("Operadoras")

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("Por Código", "Por Nome"))

    # Carregar todas as operadoras
    try:
        all_operators = db.get_all_operators()
        if not all_operators:
            st.warning("Nenhuma operadora cadastrada.")
    except Exception as e:
        st.error(f"Erro ao carregar operadoras: {e}")

    # Converter os dados para um DataFrame
    df_operators = pd.DataFrame(all_operators)

    if filter_option == "Por Código":
        cod_operator = st.text_input("Digite o código da operadora:")
        if cod_operator:
            # Filtra as operadoras pelo código
            filtered_operators = df_operators[df_operators['cod_operator'].str.contains(
                cod_operator)]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse código.")
            else:
                st.dataframe(filtered_operators)

    elif filter_option == "Por Nome":
        name_operator = st.text_input("Digite o nome da operadora:")
        if name_operator:
            # Filtra as operadoras pelo nome
            filtered_operators = df_operators[df_operators['name_operator'].str.contains(
                name_operator, case=False)]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse nome.")
            else:
                st.dataframe(filtered_operators)

    # Exibe todas as operadoras, ou as filtradas
    if filter_option == "Por Código" and not cod_operator:
        st.dataframe(df_operators)
    elif filter_option == "Por Nome" and not name_operator:
        st.dataframe(df_operators)
