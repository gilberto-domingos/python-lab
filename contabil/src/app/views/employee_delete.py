import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.employee_database import Database
from src.app.models.employee_model import Employee


class EmployeeDeleter:
    def __init__(self, db):
        """Inicializa o deletador de empregados com a injeção de dependência do banco de dados."""
        self.db = db

    def load_css(self, file_path):
        """Carrega o arquivo CSS no Streamlit."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_employee_data(self):
        """Obtém todos os empregados do banco de dados e formata para exibição."""
        try:
            all_employees = self.db.get_all_employees()
            employees = [
                Employee(
                    id=employee["id"],
                    cod_employee=employee["cod_employee"],
                    name_employee=employee["name_employee"],
                    email_employee=employee["email_employee"],
                    phone_employee=employee["phone_employee"]
                )
                for employee in all_employees
            ]

            data = [{
                "Código": employee.get_cod_employee(),
                "Nome": employee.get_name_employee(),
                "Email": employee.get_email_employee(),
                "Telefone": employee.get_phone_employee()
            } for employee in employees]

            return pd.DataFrame(data)
        except Exception as e:
            st.error(f"Erro ao buscar empregados: {e}")
            return pd.DataFrame()

    def show_employee_table(self, df_employees):
        """Exibe a tabela de empregados com formatação."""
        styled_df = df_employees.style.set_table_styles([
            dict(selector='th', props=[('text-align', 'center')]),
            dict(selector='td', props=[('text-align', 'center')])
        ]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_employees(self, df_employees, filter_option, filter_value):
        """Filtra os empregados por código ou nome conforme a escolha do usuário."""
        try:
            if filter_option == "por Código":
                return df_employees[df_employees['Código'].str.contains(filter_value, na=False)]
            elif filter_option == "por Nome":
                return df_employees[df_employees['Nome'].str.contains(filter_value, case=False, na=False)]
        except Exception as e:
            st.error(f"Erro ao filtrar empregados: {e}")
        return pd.DataFrame()

    def delete_employee(self, employee_id, cod_employee):
        """Deleta o empregado selecionado."""
        try:
            if self.db.delete_employee(employee_id):
                st.success(f"Empregado com Código '{
                           cod_employee}' deletado com sucesso!")
            else:
                st.error("Empregado não encontrado ou não foi possível deletar.")
        except Exception as e:
            st.error(f"Erro ao deletar empregado: {e}")

    def display_delete_confirmation(self, employee_id, cod_employee, name_employee):
        """Exibe uma confirmação de exclusão antes de deletar o empregado."""
        st.warning(f"Tem certeza que deseja deletar o empregado '{
                   name_employee}' (Código: {cod_employee})?")
        if st.button("Deletar"):
            self.delete_employee(employee_id, cod_employee)

    def display_filtered_employees(self, filtered_employees):
        """Exibe os empregados filtrados e permite a seleção para exclusão."""
        if filtered_employees.empty:
            st.warning("Nenhum empregado encontrado com esse critério.")
        else:
            self.show_employee_table(filtered_employees)

            selected_code = st.selectbox(
                "Escolha o empregado para deletar", filtered_employees['Código'].tolist(
                )
            )
            if selected_code:
                selected_employee_data = self.db.get_employee_by_cod(
                    selected_code)
                if selected_employee_data:
                    name_employee = selected_employee_data.get(
                        "name_employee", "Desconhecido")
                    cod_employee = selected_employee_data.get("cod_employee")
                    employee_id = selected_employee_data.get("id")
                    self.display_delete_confirmation(
                        employee_id, cod_employee, name_employee)


def show():
    css_path = Path("src/app/css/employee_read.css")
    db = Database()
    deleter = EmployeeDeleter(db)
    deleter.load_css(css_path)

    st.subheader("Funcionários - Deletar")

    df_employees = deleter.get_employee_data()
    if df_employees.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome")
    )

    filter_value = st_keyup("Digite o valor para filtrar:", key="filter_value")

    if filter_value:
        filtered_employees = deleter.filter_employees(
            df_employees, filter_option, filter_value)
        deleter.display_filtered_employees(filtered_employees)
    else:
        deleter.show_employee_table(df_employees)


if __name__ == "__main__":
    show()
