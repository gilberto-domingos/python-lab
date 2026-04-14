import streamlit as st
from pathlib import Path
from src.database.type_company_database import Database
from src.app.models.type_company_model import TypeCompany
from src.app.utils.validate import validate_cod


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/type_company_create.css")
    load_css(css_path)

    db = Database()

    st.subheader('Cadastro do Tipo de Empresa')

    cod_company = st.text_input("Código:", max_chars=5)
    descr_company = st.text_input("Descrição:")

    cod_valid = True

    if st.button("Salvar", key="save_button"):
        if cod_company:
            if len(cod_company) != 5:
                st.error("O Código deve conter exatamente 5 caracteres.")
                cod_valid = False
            elif not cod_company.isdigit():
                st.error("Digite somente números no campo Código.")
                cod_valid = False
            elif not validate_cod(cod_company):
                st.error(
                    "O Código deve conter exatamente 5 números, sem caracteres especiais.")
                cod_valid = False
        else:
            st.error("O campo Código está vazio.")
            cod_valid = False

        if not cod_company or not descr_company:
            st.error("Todos os campos são obrigatórios.")
        elif not cod_valid:
            st.error("Corrija os erros antes de salvar.")
        else:
            type_company_obj = TypeCompany(cod_company, descr_company)
            try:
                db.insert_type_company(
                    type_company_obj.get_cod_company(),
                    type_company_obj.get_descr_company()
                )
                st.success("Tipo de Empresa salvo com sucesso!")
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")


if __name__ == "__main__":
    show()
