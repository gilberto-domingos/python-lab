import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.operator_database import Database


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/operator_read.css")
    load_css(css_path)

    db = Database()

    st.subheader("Operadoras - consultar")

    try:
        all_operators = db.get_all_operators()
        df_operators = pd.DataFrame(all_operators).drop(columns=["id"])

        df_operators.rename(
            columns={
                "cod_operator": "Código",
                "cnpj_operator": "CNPJ",
                "name_operator": "Nome",
            },
            inplace=True,
        )

    except Exception as e:
        st.error(f"Erro ao buscar operadoras: {e}")
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if filter_option == "por Código":
        cod_operator = st_keyup(
            "Digite o código da operadora:", key="filter_cod")
        if cod_operator:
            filtered_operators = df_operators[
                df_operators['Código'].str.contains(cod_operator, na=False)
            ]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse código.")
            else:
                s1 = dict(selector='th', props=[('text-align', 'center')])
                s2 = dict(selector='td', props=[('text-align', 'center')])

                styled_df = filtered_operators.style.set_table_styles(
                    [s1, s2]).hide(axis=0)

                st.markdown('<div style="display: flex; justify-content: center;">' +
                            styled_df.to_html() + '</div>', unsafe_allow_html=True)

        else:
            s1 = dict(selector='th', props=[('text-align', 'center')])
            s2 = dict(selector='td', props=[('text-align', 'center')])

            styled_df = df_operators.style.set_table_styles(
                [s1, s2]).hide(axis=0)

            st.markdown('<div style="display: flex; justify-content: center;">' +
                        styled_df.to_html() + '</div>', unsafe_allow_html=True)

    elif filter_option == "por Nome":
        name_operator = st_keyup(
            "Digite o nome da operadora:", key="filter_name")
        if name_operator:
            filtered_operators = df_operators[
                df_operators['Nome'].str.contains(
                    name_operator, case=False, na=False)
            ]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse nome.")
            else:
                s1 = dict(selector='th', props=[('text-align', 'center')])
                s2 = dict(selector='td', props=[('text-align', 'center')])

                styled_df = filtered_operators.style.set_table_styles(
                    [s1, s2]).hide(axis=0)

                st.markdown('<div style="display: flex; justify-content: center;">' +
                            styled_df.to_html() + '</div>', unsafe_allow_html=True)

        else:
            s1 = dict(selector='th', props=[('text-align', 'center')])
            s2 = dict(selector='td', props=[('text-align', 'center')])

            styled_df = df_operators.style.set_table_styles(
                [s1, s2]).hide(axis=0)

            st.markdown('<div style="display: flex; justify-content: center;">' +
                        styled_df.to_html() + '</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    show()
