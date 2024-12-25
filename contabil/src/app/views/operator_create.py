import streamlit as st
from pathlib import Path
from src.database.operator_database import Database
from src.app.models.operator_model import Operator
from src.app.utils.validate import validate_cod, validate_cnpj


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/operator_create.css")
    load_css(css_path)

    db = Database()

    st.subheader('Cadastro de operadoras')

    cod_operator = st.text_input("Código :", max_chars=5)
    cnpj_operator = st.text_input("CNPJ :", max_chars=20)
    name_operator = st.text_input("Nome da operadora :")

    cod_valid = True
    if cod_operator:
        if len(cod_operator) != 5:
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False
        elif not cod_operator.isdigit():
            st.error("Digite somente números no campo Código.")
            cod_valid = False
        elif not validate_cod(cod_operator):
            st.error(
                "O Código deve conter exatamente 5 números, sem caracteres especiais.")
            cod_valid = False

    cnpj_valid = True
    if cnpj_operator:
        if not validate_cnpj(cnpj_operator):
            st.error("O CNPJ informado é inválido.")
            cnpj_valid = False

    if st.button("Salvar"):
        if not cod_operator or not cnpj_operator or not name_operator:
            st.error("Todos os campos são obrigatórios.")
        elif not cod_valid or not cnpj_valid:
            st.error("Corrija os erros no Código ou CNPJ antes de salvar.")
        else:
            operator_obj = Operator(cod_operator, cnpj_operator, name_operator)
            try:
                db.insert_operator(
                    operator_obj.get_cod_operator(),
                    operator_obj.get_cnpj_operator(),
                    operator_obj.get_name_operator()
                )
                st.success("Operadora salva com sucesso!")
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")


if __name__ == "__main__":
    show()
