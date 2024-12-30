import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.employee_database import Database
from src.app.models.employee_model import Employee
from src.app.utils.validate import validate_cod, validate_email_address, validate_phone_employee


class EmployeeEditor:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        """Carrega e aplica o CSS da página."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def show_employee_table(self, df_employees):
        """Exibe a tabela de empregados com formatação e centralização."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_employees.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def edit_employee(self, employee):
        """Permite editar um empregado existente."""
        new_cod = st.text_input(
            "Novo Código", value=employee.get_cod_employee(), max_chars=5)
        new_name = st.text_input(
            "Novo Nome", value=employee.get_name_employee(), max_chars=50)
        new_email = st.text_input(
            "Novo Email", value=employee.get_email_employee(), max_chars=50)
        new_phone = st.text_input(
            "Novo Telefone", value=employee.get_phone_employee(), max_chars=15)

        cod_valid = True
        if new_cod and not validate_cod(new_cod):
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False

        email_valid = True
        if new_email:
            validation_result = validate_email_address(new_email)
            if validation_result != new_email:
                st.error(f"Email inválido: {validation_result}")
                email_valid = False

        phone_valid = True
        if new_phone:
            is_valid, validation_result = validate_phone_employee(new_phone)
            if not is_valid:
                st.error(f"Telefone inválido: {validation_result}")
                phone_valid = False

        if st.button("Salvar Alterações"):
            if not (cod_valid and email_valid and phone_valid):
                st.error("Corrija os erros antes de salvar.")
            else:
                try:
                    self.db.update_employee(
                        employee.id, new_cod, new_name, new_email, new_phone)
                    st.success("Empregado atualizado com sucesso!")
                    return new_cod, new_name, new_email, new_phone
                except Exception as e:
                    st.error(f"Erro ao atualizar empregado: {e}")
        return None


def show():
    """Função principal para exibir a tela de edição de empregados."""
    css_path = Path("src/app/css/employee_update.css")
    editor = EmployeeEditor(Database())
    editor.load_css(css_path)

    st.subheader("Funcionários - Editar")

    try:
        all_employees = editor.db.get_all_employees()
        df_employees = pd.DataFrame(
            all_employees).drop(columns=["id"])
        df_employees.rename(columns={
            "cod_employee": "Código",
            "name_employee": "Nome",
            "email_employee": "Email",
            "phone_employee": "Telefone"
        }, inplace=True)
    except Exception as e:
        st.error(f"Erro ao buscar empregados: {e}")
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if 'filtered_employees' not in st.session_state:
        st.session_state['filtered_employees'] = df_employees

    filtered_employees = st.session_state['filtered_employees']

    if filter_option == "por Código":
        cod_employee = st_keyup(
            "Digite o código do empregado:", key="filter_cod")
        if cod_employee:
            filtered_employees = df_employees[df_employees['Código'].str.contains(
                cod_employee, na=False)]
            if filtered_employees.empty:
                st.warning("Nenhum empregado encontrado com esse código.")
        st.session_state['filtered_employees'] = filtered_employees

    elif filter_option == "por Nome":
        name_employee = st_keyup(
            "Digite o nome do empregado:", key="filter_name")
        if name_employee:
            filtered_employees = df_employees[df_employees['Nome'].str.contains(
                name_employee, case=False, na=False)]
            if filtered_employees.empty:
                st.warning("Nenhum empregado encontrado com esse nome.")
        st.session_state['filtered_employees'] = filtered_employees

    if not filtered_employees.empty:
        editor.show_employee_table(filtered_employees)

        selected_employee_data = filtered_employees.iloc[0]
        selected_employee = editor.db.get_employee_by_cod(
            selected_employee_data['Código'])

        employee = Employee(selected_employee['cod_employee'],
                            selected_employee['name_employee'],
                            selected_employee['email_employee'],
                            selected_employee['phone_employee'],
                            selected_employee['id'])

        updated_values = editor.edit_employee(employee)

        if updated_values:
            filtered_employees.loc[filtered_employees['Código'] == selected_employee_data['Código'], [
                'Nome', 'Email', 'Telefone']] = updated_values[1], updated_values[2], updated_values[3]
            st.session_state['filtered_employees'] = filtered_employees
            editor.show_employee_table(filtered_employees)


if __name__ == "__main__":
    show()
