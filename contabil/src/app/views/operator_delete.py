import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.operator_database import Database
from src.app.models.operator_model import Operator


class OperatorDeleter:
    def __init__(self, db):
        """Inicializa o deletador de operadoras com a injeção de dependência do banco de dados."""
        self.db = db

    def load_css(self, file_path):
        """Carrega o arquivo CSS no Streamlit."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_operator_objects(self):
        """Obtém todas as operadoras do banco de dados e cria objetos Operator."""
        try:
            all_operators = self.db.get_all_operators()
            return [
                Operator(
                    cod_operator=op["cod_operator"],
                    cnpj_operator=op["cnpj_operator"],
                    name_operator=op["name_operator"],
                    id=op["id"]
                ) for op in all_operators
            ]
        except Exception as e:
            st.error(f"Erro ao buscar operadoras: {e}")
            return []

    def create_operator_dataframe(self, operators):
        """Converte uma lista de objetos Operator em um DataFrame para exibição."""
        data = [{
            "Código": op.get_cod_operator(),
            "CNPJ": op.get_cnpj_operator(),
            "Nome": op.get_name_operator(),
            "ID": op.id
        } for op in operators]

        return pd.DataFrame(data).drop(columns=["ID"])

    def filter_operators(self, df_operators, filter_option, filter_value):
        """Filtra as operadoras por código ou nome conforme a escolha do usuário."""
        if filter_option == "por Código":
            return df_operators[df_operators['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Nome":
            return df_operators[df_operators['Nome'].str.contains(filter_value, case=False, na=False)]
        return df_operators

    def delete_operator(self, operator_id):
        """Deleta a operadora selecionada."""
        try:
            self.db.delete_operator(operator_id)
            st.success("Operadora deletada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao deletar operadora: {e}")

    def display_delete_confirmation(self, operator):
        """Exibe uma confirmação de exclusão antes de deletar a operadora."""
        st.warning(f"Tem certeza que deseja deletar a operadora {
                   operator.get_name_operator()} (Código: {operator.get_cod_operator()})?")
        if st.button("Deletar"):
            self.delete_operator(operator.id)

    def display_filtered_operators(self, filtered_operators):
        """Exibe as operadoras filtradas e permite a seleção para exclusão."""
        if filtered_operators.empty:
            st.warning("Nenhuma operadora encontrada com esse critério.")
        else:
            st.dataframe(filtered_operators)

            # Seleção para deletar
            delete_option = st.selectbox(
                "Escolha a operadora para deletar", filtered_operators['Código'].tolist(
                )
            )
            if delete_option:
                operator = next((op for op in self.get_operator_objects(
                ) if op.get_cod_operator() == delete_option), None)
                if operator:
                    self.display_delete_confirmation(operator)


def show():
    css_path = Path("src/app/css/operator_read.css")
    db = Database()
    deleter = OperatorDeleter(db)
    deleter.load_css(css_path)

    st.subheader("Operadoras - deletar")

    operators = deleter.get_operator_objects()
    if not operators:
        return

    df_operators = deleter.create_operator_dataframe(operators)

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome")
    )

    if filter_option == "por Código":
        filter_value = st_keyup(
            "Digite o código da operadora:", key="filter_cod"
        )
    else:
        filter_value = st_keyup(
            "Digite o nome da operadora:", key="filter_name"
        )

    if filter_value:
        filtered_operators = deleter.filter_operators(
            df_operators, filter_option, filter_value
        )
        deleter.display_filtered_operators(filtered_operators)
    else:
        st.dataframe(df_operators)


if __name__ == "__main__":
    show()
