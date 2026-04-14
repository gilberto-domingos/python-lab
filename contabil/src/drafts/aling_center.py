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

    st.title("Operadoras")

    # Obtém todas as operadoras e converte para DataFrame
    try:
        all_operators = db.get_all_operators()
        df_operators = pd.DataFrame(all_operators).drop(columns=["id"])

        # Renomeia as colunas
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

    # Filtro
    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("Por Código", "Por Nome"))

    if filter_option == "Por Código":
        cod_operator = st_keyup(
            "Digite o código da operadora:", key="filter_cod")
        if cod_operator:
            # Filtra as operadoras pelo código
            filtered_operators = df_operators[
                df_operators['Código'].str.contains(cod_operator, na=False)
            ]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse código.")
            else:
                # Estilizando o DataFrame com centralização
                styled_df = filtered_operators.style.set_properties(**{
                    "background-color": "white",
                    "color": "black",
                    "border-color": "black",
                    'text-align': 'center'
                })

                # Centralizando os títulos
                st.markdown(
                    """
                    <style>
                        .streamlit-expanderHeader {
                            text-align: center;
                        }
                        thead th {
                            text-align: center;
                        }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

                st.dataframe(styled_df)
                st.write(styled_df.to_html(), unsafe_allow_html=True)
        else:
            # Estilizando o DataFrame com centralização
            styled_df = df_operators.style.set_properties(**{
                "background-color": "white",
                "color": "black",
                "border-color": "black",
                'text-align': 'center'
            })

            # Centralizando os títulos
            st.markdown(
                """
                <style>
                    thead th {
                        text-align: center;
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )

            st.dataframe(styled_df)
            st.write(styled_df.to_html(), unsafe_allow_html=True)

    elif filter_option == "Por Nome":
        name_operator = st_keyup(
            "Digite o nome da operadora:", key="filter_name")
        if name_operator:
            # Filtra as operadoras pelo nome
            filtered_operators = df_operators[
                df_operators['Nome'].str.contains(
                    name_operator, case=False, na=False)
            ]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse nome.")
            else:
                # Estilizando o DataFrame com centralização
                styled_df = filtered_operators.style.set_properties(**{
                    "background-color": "white",
                    "color": "black",
                    "border-color": "black",
                    'text-align': 'center'
                })

                # Centralizando os títulos
                st.markdown(
                    """
                    <style>
                        thead th {
                            text-align: center;
                        }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

                st.dataframe(styled_df)
                st.write(styled_df.to_html(), unsafe_allow_html=True)
        else:
            # Estilizando o DataFrame com centralização
            styled_df = df_operators.style.set_properties(**{
                "background-color": "white",
                "color": "black",
                "border-color": "black",
                'text-align': 'center'
            })

            # Centralizando os títulos
            st.markdown(
                """
                <style>
                    thead th {
                        text-align: center;
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )

            st.dataframe(styled_df)
            st.write(styled_df.to_html(), unsafe_allow_html=True)


if __name__ == "__main__":
    show()
