import streamlit as st
from pathlib import Path
from src.database.tax_regime_database import Database
from src.app.models.tax_regime_model import TaxRegime
from src.app.utils.validate import validate_cod


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/tax_regime_create.css")
    load_css(css_path)

    db = Database()

    st.subheader('Cadastro do Regime Tributário')

    cod_tax_regime = st.text_input("Código:", max_chars=5)
    descr_tax_regime = st.text_input("Descrição:")

    cod_valid = True

    if st.button("Salvar", key="save_button"):
        if cod_tax_regime:
            if len(cod_tax_regime) != 5:
                st.error("O Código deve conter exatamente 5 caracteres.")
                cod_valid = False
            elif not cod_tax_regime.isdigit():
                st.error("Digite somente números no campo Código.")
                cod_valid = False
            elif not validate_cod(cod_tax_regime):
                st.error(
                    "O Código deve conter exatamente 5 números, sem caracteres especiais.")
                cod_valid = False
        else:
            st.error("O campo Código está vazio.")
            cod_valid = False

        if not cod_tax_regime or not descr_tax_regime:
            st.error("Todos os campos são obrigatórios.")
        elif not cod_valid:
            st.error("Corrija os erros antes de salvar.")
        else:
            tax_regime_obj = TaxRegime(cod_tax_regime, descr_tax_regime)
            try:
                db.insert_tax_regime(
                    tax_regime_obj.get_cod_tax_regime(),
                    tax_regime_obj.get_descr_tax_regime()
                )
                st.success("Regime Tributário salvo com sucesso!")
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")


if __name__ == "__main__":
    show()
