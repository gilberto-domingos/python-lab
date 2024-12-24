import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.operator_database import Database
from src.app.models.operator_model import Operator
# Importações adicionadas
from src.app.utils.validate import validate_cod, validate_cnpj


class OperatorEditor:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        """Carrega e aplica o CSS da página."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def show_operator_table(self, df_operators):
        """Exibe a tabela de operadoras com formatação e centralização."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_operators.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def edit_operator(self, operator):
        """Permite editar uma operadora existente."""
        new_cod = st.text_input(
            "Novo Código", value=operator.get_cod_operator(), max_chars=5)
        new_cnpj = st.text_input(
            "Novo CNPJ", value=operator.get_cnpj_operator(), max_chars=14)
        new_name = st.text_input(
            "Novo Nome", value=operator.get_name_operator(), max_chars=50)

        # Validação do Código
        cod_valid = True
        if new_cod and not validate_cod(new_cod):
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False

        # Validação do CNPJ
        cnpj_valid = True
        if new_cnpj and not validate_cnpj(new_cnpj):
            st.error("O CNPJ deve conter exatamente 14 números.")
            cnpj_valid = False

        if st.button("Salvar Alterações") and cod_valid and cnpj_valid:
            try:
                self.db.update_operator(
                    operator.operator_id, new_cod, new_cnpj, new_name)
                st.success("Operadora atualizada com sucesso!")
                return new_cod, new_cnpj, new_name
            except Exception as e:
                st.error(f"Erro ao atualizar operadora: {e}")
        return None


def show():
    """Função principal para exibir a tela de edição de operadoras."""
    css_path = Path("src/app/css/operator_read.css")
    editor = OperatorEditor(Database())
    editor.load_css(css_path)

    st.subheader("Operadoras - editar")

    try:
        all_operators = editor.db.get_all_operators()
        df_operators = pd.DataFrame(all_operators).drop(columns=["id"])
        df_operators.rename(columns={
            "cod_operator": "Código",
            "cnpj_operator": "CNPJ",
            "name_operator": "Nome"
        }, inplace=True)
    except Exception as e:
        st.error(f"Erro ao buscar operadoras: {e}")
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if 'filtered_operators' not in st.session_state:
        st.session_state['filtered_operators'] = df_operators

    filtered_operators = st.session_state['filtered_operators']

    if filter_option == "por Código":
        cod_operator = st_keyup(
            "Digite o código da operadora:", key="filter_cod")
        if cod_operator:
            filtered_operators = df_operators[df_operators['Código'].str.contains(
                cod_operator, na=False)]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse código.")
        st.session_state['filtered_operators'] = filtered_operators

    elif filter_option == "por Nome":
        name_operator = st_keyup(
            "Digite o nome da operadora:", key="filter_name")
        if name_operator:
            filtered_operators = df_operators[df_operators['Nome'].str.contains(
                name_operator, case=False, na=False)]
            if filtered_operators.empty:
                st.warning("Nenhuma operadora encontrada com esse nome.")
        st.session_state['filtered_operators'] = filtered_operators

    # Exibe a tabela e a opção de edição
    if not filtered_operators.empty:
        editor.show_operator_table(filtered_operators)
        edit_option = st.selectbox(
            "Escolha a operadora para editar", filtered_operators['Código'].tolist())
        if edit_option:
            selected_operator = editor.db.get_operator_by_cod(edit_option)
            operator = Operator(selected_operator['cod_operator'], selected_operator['cnpj_operator'],
                                selected_operator['name_operator'], selected_operator['id'])
            updated_values = editor.edit_operator(operator)

            if updated_values:
                # Atualiza a linha da tabela diretamente com os novos dados
                filtered_operators.loc[filtered_operators['Código'] == edit_option, [
                    'CNPJ', 'Nome']] = updated_values[1], updated_values[2]
                # Atualiza o estado com os dados modificados
                st.session_state['filtered_operators'] = filtered_operators
                # Reexibe a tabela com os dados atualizados
                editor.show_operator_table(filtered_operators)


if __name__ == "__main__":
    show()
