import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.operator_database import Database
from src.app.models.operator_model import Operator  # Importando o modelo Operator


class OperatorReader:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_operator_data(self):
        try:
            all_operators = self.db.get_all_operators()
            # Convertendo os dados de dicionário para instâncias da classe Operator
            operators = [Operator(
                operator['cod_operator'],
                operator['cnpj_operator'],
                operator['name_operator']
            ) for operator in all_operators]

            # Criando um DataFrame para exibição
            df_operators = pd.DataFrame([{
                'Código': operator.cod_operator,
                'CNPJ': operator.cnpj_operator,
                'Nome': operator.name_operator
            } for operator in operators])

            return df_operators
        except Exception as e:
            st.error(f"Erro ao buscar operadoras: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

    def show_operator_table(self, df_operators):
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_operators.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_operators(self, df_operators, filter_option, filter_value):
        if filter_option == "por Código":
            return df_operators[df_operators['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Nome":
            return df_operators[df_operators['Nome'].str.contains(filter_value, case=False, na=False)]
        return df_operators

    def display_filtered_operators(self, filtered_operators):
        if filtered_operators.empty:
            st.warning("Nenhuma operadora encontrada com esse critério.")
        else:
            self.show_operator_table(filtered_operators)


def show():
    css_path = Path("src/app/css/operator_read.css")
    db = Database()
    reader = OperatorReader(db)
    reader.load_css(css_path)

    st.subheader("Operadoras - Consultar")

    df_operators = reader.get_operator_data()
    if df_operators.empty:
        return  # Caso não haja dados para exibir, retornamos

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if filter_option == "por Código":
        filter_value = st_keyup(
            "Digite o código da operadora:", key="filter_cod")
    else:
        filter_value = st_keyup(
            "Digite o nome da operadora:", key="filter_name")

    if filter_value:
        filtered_operators = reader.filter_operators(
            df_operators, filter_option, filter_value)
        reader.display_filtered_operators(filtered_operators)
    else:
        reader.show_operator_table(df_operators)


if __name__ == "__main__":
    show()
