import streamlit as st
from pathlib import Path
from src.database.employee_database import Database
from src.app.models.employee_model import Employee
from src.app.utils.validate import validate_cod, validate_email_address, validate_brazilian_phone


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/employee_create.css")
    load_css(css_path)

    db = Database()

    st.subheader('Cadastro de Funcionários')

    cod_employee = st.text_input("Código :", max_chars=5)
    name_employee = st.text_input("Nome do Funcionário :")
    email_employee = st.text_input("Email:")
    phone_employee = st.text_input("Celular :")

    cod_valid = True
    email_valid = True
    phone_valid = True

    if st.button("Salvar", key="save_button"):
        if cod_employee:
            if len(cod_employee) != 5:
                st.error("O Código deve conter exatamente 5 números.")
                cod_valid = False
            elif not cod_employee.isdigit():
                st.error("Digite somente números no campo Código.")
                cod_valid = False
            elif not validate_cod(cod_employee):
                st.error(
                    "O Código deve conter exatamente 5 números, sem caracteres especiais.")
                cod_valid = False
        else:
            st.error("O campo Código está vazio.")
            cod_valid = False

        if email_employee:
            email_validation_result = validate_email_address(email_employee)
            if email_validation_result != email_employee:
                st.error(f"E-mail inválido: {email_validation_result}")
                email_valid = False
        else:
            st.error("O campo de e-mail está vazio.")
            email_valid = False

        if phone_employee:
            phone_validation_result, phone_data = validate_brazilian_phone(
                phone_employee)
            if not phone_validation_result:
                st.error(f"Telefone inválido: {phone_data}")
                phone_valid = False
        else:
            st.error("O campo de telefone está vazio.")
            phone_valid = False

        if not cod_employee or not name_employee or not email_employee or not phone_employee:
            st.error("Todos os campos são obrigatórios.")
        elif not cod_valid or not email_valid or not phone_valid:
            st.error("Corrija os erros antes de salvar.")
        else:
            employee_obj = Employee(
                cod_employee, name_employee, email_employee, phone_employee)
            try:
                db.insert_employee(
                    employee_obj.get_cod_employee(),
                    employee_obj.get_name_employee(),
                    employee_obj.get_email_employee(),
                    employee_obj.get_phone_employee()
                )
                st.success("Funcionário salvo com sucesso!")
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")


if __name__ == "__main__":
    show()
