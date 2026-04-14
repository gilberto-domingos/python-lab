import streamlit as st
from pathlib import Path
from src.database.customer_database import Database
from src.app.models.customer_model import Customer
from src.app.utils.validate import validate_cod, validate_email_address, validate_brazilian_phone


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/customer_create.css")
    load_css(css_path)

    db = Database()

    st.subheader('Cadastro de clientes')

    cod_customer = st.text_input("Código :", max_chars=5)
    name_customer = st.text_input("Nome do cliente :")
    cell_customer = st.text_input("Célula do cliente :")
    email_customer = st.text_input("Email:")
    phone_customer = st.text_input("Telefone :")

    cod_valid = True
    email_valid = True
    phone_valid = True

    if cod_customer:
        if len(cod_customer) != 5:
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False
        elif not cod_customer.isdigit():
            st.error("Digite somente números no campo Código.")
            cod_valid = False
        elif not validate_cod(cod_customer):
            st.error(
                "O Código deve conter exatamente 5 números, sem caracteres especiais."
            )
            cod_valid = False

    if st.button("Salvar", key="save_button"):
        if email_customer:
            email_validation_result = validate_email_address(email_customer)
            if email_validation_result != email_customer:
                st.error(f"E-mail inválido: {email_validation_result}")
                email_valid = False
        else:
            st.error("O campo de e-mail está vazio.")
            email_valid = False

        if phone_customer:
            phone_validation_result, phone_data = validate_brazilian_phone(
                phone_customer)
            if not phone_validation_result:
                st.error(f"Telefone inválido: {phone_data}")
                phone_valid = False
        else:
            st.error("O campo de telefone está vazio.")
            phone_valid = False

        if not cod_customer or not name_customer or not cell_customer or not email_customer or not phone_customer:
            st.error("Todos os campos são obrigatórios.")
        elif not cod_valid or not email_valid or not phone_valid:
            st.error("Corrija os erros antes de salvar.")
        else:
            customer_obj = Customer(
                cod_customer, cell_customer, name_customer, email_customer, phone_customer
            )
            try:
                db.insert_customer(
                    customer_obj.get_cod_customer(),
                    customer_obj.get_cell_customer(),
                    customer_obj.get_name_customer(),
                    customer_obj.get_email_customer(),
                    customer_obj.get_phone_customer()
                )
                st.success("Cliente salvo com sucesso!")
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")


if __name__ == "__main__":
    show()
