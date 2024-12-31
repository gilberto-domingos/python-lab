import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.employee_database import Database
from src.app.models.employee_model import Employee


class EmployeeReader:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_employee_data(self):
        try:
            all_employees = self.db.get_all_employees()
            employees = [Employee(
                employee['cod_employee'],
                employee['name_employee'],
                employee['email_employee'],
                employee['phone_employee']
            ) for employee in all_employees]

            df_employees = pd.DataFrame([{
                'Código': emp.cod_employee,
                'Nome': emp.name_employee,
                'Email': emp.email_employee,
                'Telefone': emp.phone_employee
            } for emp in employees])

            return df_employees
        except Exception as e:
            st.error(f"Erro ao buscar funcionários: {e}")
            return pd.DataFrame()

    def show_employee_table(self, df_employees):
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_employees.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_employees(self, df_employees, filter_option, filter_value):
        if filter_option == "por Código":
            return df_employees[df_employees['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Nome":
            return df_employees[df_employees['Nome'].str.contains(filter_value, case=False, na=False)]
        return df_employees

    def display_filtered_employees(self, filtered_employees):
        if filtered_employees.empty:
            st.warning("Nenhum funcionário encontrado com esse critério.")
        else:
            self.show_employee_table(filtered_employees)


def show():
    css_path = Path("src/app/css/employee_read.css")
    db = Database()
    reader = EmployeeReader(db)
    reader.load_css(css_path)

    st.subheader("Funcionários - consultar")

    df_employees = reader.get_employee_data()
    if df_employees.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if filter_option == "por Código":
        filter_value = st_keyup(
            "Digite o código do funcionário:", key="filter_cod")
    else:
        filter_value = st_keyup(
            "Digite o nome do funcionário:", key="filter_name")

    if filter_value:
        filtered_employees = reader.filter_employees(
            df_employees, filter_option, filter_value)
        reader.display_filtered_employees(filtered_employees)
    else:
        reader.show_employee_table(df_employees)


if __name__ == "__main__":
    show()
