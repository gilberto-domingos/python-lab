from models.operator_model import Operator
import streamlit as st


def show():
    st.subheader("Cadastro de Operadoras")

    cod_operator = st.text_input("Código:")

    cnpj_operator = st.text_input("CNPJ (somente números):", max_chars=14)

    name_operator = st.text_input("Nome:")

    if cnpj_operator:
        if len(cnpj_operator) > 14:
            cnpj_operator = cnpj_operator[:14]  # Limita para 14 dígitos
            st.warning("O CNPJ foi truncado para 14 dígitos.")

        if len(cnpj_operator) != 14:
            st.error("O CNPJ deve conter exatamente 14 números.")

        elif not cnpj_operator.isdigit():
            st.error("Digite somente números no campo CNPJ.")

    if st.button("Salvar"):
        if not cod_operator or not cnpj_operator or not name_operator:
            st.error("Todos os campos são obrigatórios.")
        elif len(cnpj_operator) != 14:
            st.error("O CNPJ deve conter exatamente 14 números.")
        else:
            operator_obj = Operator(cod_operator, name_operator, cnpj_operator)
            st.success("Operadora salva com sucesso!")
            st.write(f"Dados para armazenamento no banco:")
            st.write(f"- Código: {operator_obj.cod_operator}")
            st.write(f"- CNPJ (limpo): {operator_obj.cnpj_operator}")
            st.write(f"- Nome: {operator_obj.name_operator}")
