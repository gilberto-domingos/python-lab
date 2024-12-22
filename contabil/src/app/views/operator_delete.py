import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.operator_database import Database


class OperatorDeleter:
    def __init__(self, db):
        """Inicializa o deletador de operadoras com a injeção de dependência do banco de dados."""
        self.db = db

    def load_css(self, file_path):
        """Carrega o arquivo CSS no Streamlit."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_operator_data(self):
        """Obtém todas as operadoras do banco de dados e formata para exibição."""
        try:
            all_operators = self.db.get_all_operators()
            df_operators = pd.DataFrame(all_operators).drop(columns=["id"])
            df_operators.rename(columns={
                "cod_operator": "Código",
                "cnpj_operator": "CNPJ",
                "name_operator": "Nome"
            }, inplace=True)
            return df_operators
        except Exception as e:
            st.error(f"Erro ao buscar operadoras: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

    def show_operator_table(self, df_operators):
        """Exibe a tabela de operadoras com formatação."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_operators.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

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

    def display_delete_confirmation(self, operator_name, operator_id):
        """Exibe uma confirmação de exclusão antes de deletar a operadora."""
        st.warning(f"Tem certeza que deseja deletar a operadora {
                   operator_name} (Código: {operator_id})?")
        if st.button("Deletar"):
            self.delete_operator(operator_id)

    def display_filtered_operators(self, filtered_operators):
        """Exibe as operadoras filtradas e permite a seleção para exclusão."""
        if filtered_operators.empty:
            st.warning("Nenhuma operadora encontrada com esse critério.")
        else:
            self.show_operator_table(filtered_operators)

            # Seleção para deletar
            delete_option = st.selectbox(
                "Escolha a operadora para deletar", filtered_operators['Código'].tolist())
            if delete_option:
                selected_operator = self.db.get_operator_by_cod(delete_option)
                if selected_operator:
                    self.display_delete_confirmation(
                        selected_operator['name_operator'], selected_operator['id'])


def show():
    css_path = Path("src/app/css/operator_read.css")
    db = Database()
    deleter = OperatorDeleter(db)
    deleter.load_css(css_path)

    st.subheader("Operadoras - deletar")

    df_operators = deleter.get_operator_data()
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
        filtered_operators = deleter.filter_operators(
            df_operators, filter_option, filter_value)
        deleter.display_filtered_operators(filtered_operators)
    else:
        # Exibe a tabela sem filtro se nenhum valor for inserido
        deleter.show_operator_table(df_operators)


if __name__ == "__main__":
    show()
