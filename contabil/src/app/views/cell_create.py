from src.app.utils.validate import validate_cod, validate_email_address
from src.app.models.cell_model import Cell
from src.database.cell_database import Database
from pathlib import Path
import streamlit as st


def show():
    st.subheader("Page cell_create")


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/cell_create.css")
    load_css(css_path)

    db = Database()

    st.subheader('Cadastro de células')

    cod_cell = st.text_input("Código :", max_chars=5)
    name_cell = st.text_input("Nome da célula :")
    email_cell = st.text_input("Email:")

    cod_valid = True
    email_valid = True

    if cod_cell:
        if len(cod_cell) != 5:
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False
        elif not cod_cell.isdigit():
            st.error("Digite somente números no campo Código.")
            cod_valid = False
        elif not validate_cod(cod_cell):
            st.error(
                "O Código deve conter exatamente 5 números, sem caracteres especiais."
            )
            cod_valid = False

    if st.button("Salvar", key="save_button"):
        if email_cell:
            email_validation_result = validate_email_address(email_cell)
            if email_validation_result != email_cell:
                st.error(f"E-mail inválido: {email_validation_result}")
                email_valid = False
        else:
            st.error("O campo de e-mail está vazio.")
            email_valid = False

        if not cod_cell or not name_cell or not email_cell:
            st.error("Todos os campos são obrigatórios.")
        elif not cod_valid or not email_valid:
            st.error("Corrija os erros antes de salvar.")
        else:
            cell_obj = Cell(cod_cell, name_cell, email_cell)
            try:
                db.insert_cell(
                    cell_obj.get_cod_cell(),
                    cell_obj.get_name_cell(),
                    cell_obj.get_email_cell()
                )
                st.success("Célula salva com sucesso!")
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")


if __name__ == "__main__":
    show()
