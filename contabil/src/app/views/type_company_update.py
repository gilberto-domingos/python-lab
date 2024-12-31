import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.type_company_database import Database
from src.app.models.type_company_model import TypeCompany
from src.app.utils.validate import validate_cod


class TypeCompanyEditor:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def show_type_company_table(self, df_type_companies):
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_type_companies.style.set_table_styles(
            [s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def edit_type_company(self, type_company):
        new_cod = st.text_input(
            "Novo Código", value=type_company.get_cod_company(), max_chars=5)
        new_descr = st.text_input(
            "Nova Descrição", value=type_company.get_descr_company(), max_chars=100)

        cod_valid = True
        if new_cod and not validate_cod(new_cod):
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False

        if st.button("Salvar Alterações"):
            if not cod_valid:
                st.error("Corrija os erros antes de salvar.")
            else:
                try:
                    self.db.update_type_company(
                        type_company.id, new_cod, new_descr)
                    st.success("Tipo de empresa atualizado com sucesso!")
                    return new_cod, new_descr
                except Exception as e:
                    st.error(f"Erro ao atualizar tipo de empresa: {e}")
        return None


def show():
    css_path = Path("src/app/css/type_company_update.css")
    editor = TypeCompanyEditor(Database())
    editor.load_css(css_path)

    st.subheader("Tipo de Empresa - Editar")

    try:
        all_type_companies = editor.db.get_all_type_companies()
        df_type_companies = pd.DataFrame(
            all_type_companies).drop(columns=["id"])
        df_type_companies.rename(columns={
            "cod_company": "Código",
            "descr_company": "Descrição"
        }, inplace=True)
    except Exception as e:
        st.error(f"Erro ao buscar tipos de empresa: {e}")
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Descrição"))

    if 'filtered_type_companies' not in st.session_state:
        st.session_state['filtered_type_companies'] = df_type_companies

    filtered_type_companies = st.session_state['filtered_type_companies']

    if filter_option == "por Código":
        cod_company = st_keyup(
            "Digite o código do tipo de empresa:", key="filter_cod")
        if cod_company:
            filtered_type_companies = df_type_companies[df_type_companies['Código'].str.contains(
                cod_company, na=False)]
            if filtered_type_companies.empty:
                st.warning(
                    "Nenhum tipo de empresa encontrado com esse código.")
        st.session_state['filtered_type_companies'] = filtered_type_companies

    elif filter_option == "por Descrição":
        descr_company = st_keyup(
            "Digite a descrição do tipo de empresa:", key="filter_descr")
        if descr_company:
            filtered_type_companies = df_type_companies[df_type_companies['Descrição'].str.contains(
                descr_company, case=False, na=False)]
            if filtered_type_companies.empty:
                st.warning(
                    "Nenhum tipo de empresa encontrado com essa descrição.")
        st.session_state['filtered_type_companies'] = filtered_type_companies

    if not filtered_type_companies.empty:
        editor.show_type_company_table(filtered_type_companies)

        selected_type_company_data = filtered_type_companies.iloc[0]
        selected_type_company = editor.db.get_type_company_by_cod(
            selected_type_company_data['Código'])

        type_company = TypeCompany(selected_type_company['cod_company'],
                                   selected_type_company['descr_company'],
                                   selected_type_company['id'])

        updated_values = editor.edit_type_company(type_company)

        if updated_values:
            filtered_type_companies.loc[filtered_type_companies['Código'] == selected_type_company_data['Código'], [
                'Descrição']] = updated_values[1]
            st.session_state['filtered_type_companies'] = filtered_type_companies
            editor.show_type_company_table(filtered_type_companies)


if __name__ == "__main__":
    show()
