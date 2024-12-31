import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database import Database
from src.database.type_company_database import Database
from src.app.models.type_company_model import TypeCompany


class TypeCompanyDeleter:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_type_company_data(self):
        try:
            all_type_companies = self.db.get_all_type_companies()
            type_companies = [
                TypeCompany(
                    id=type_company["id"],
                    cod_company=type_company["cod_company"],
                    descr_company=type_company["descr_company"]
                )
                for type_company in all_type_companies
            ]

            data = [{
                "Código": type_company.get_cod_company(),
                "Descrição": type_company.get_descr_company()
            } for type_company in type_companies]

            return pd.DataFrame(data)
        except Exception as e:
            st.error(f"Erro ao buscar tipos de empresas: {e}")
            return pd.DataFrame()

    def show_type_company_table(self, df_type_companies):
        styled_df = df_type_companies.style.set_table_styles([
            dict(selector='th', props=[('text-align', 'center')]),
            dict(selector='td', props=[('text-align', 'center')])
        ]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_type_companies(self, df_type_companies, filter_option, filter_value):
        try:
            if filter_option == "por Código":
                return df_type_companies[df_type_companies['Código'].str.contains(filter_value, na=False)]
            elif filter_option == "por Descrição":
                return df_type_companies[df_type_companies['Descrição'].str.contains(filter_value, case=False, na=False)]
        except Exception as e:
            st.error(f"Erro ao filtrar tipos de empresas: {e}")
        return pd.DataFrame()

    def delete_type_company(self, type_company_id, cod_company):
        try:
            if self.db.delete_type_company(type_company_id):
                st.success(f"Tipo de empresa com Código '{
                           cod_company}' deletado com sucesso!")
            else:
                st.error(
                    "Tipo de empresa não encontrado ou não foi possível deletar.")
        except Exception as e:
            st.error(f"Erro ao deletar tipo de empresa: {e}")

    def display_delete_confirmation(self, type_company_id, cod_company, descr_company):
        st.warning(f"Tem certeza que deseja deletar o tipo de empresa '{
                   descr_company}' (Código: {cod_company})?")
        if st.button("Deletar"):
            self.delete_type_company(type_company_id, cod_company)

    def display_filtered_type_companies(self, filtered_type_companies):
        if filtered_type_companies.empty:
            st.warning("Nenhum tipo de empresa encontrado com esse critério.")
        else:
            self.show_type_company_table(filtered_type_companies)

            selected_code = st.selectbox(
                "Escolha o tipo de empresa para deletar", filtered_type_companies['Código'].tolist(
                )
            )
            if selected_code:
                selected_type_company_data = self.db.get_type_company_by_cod(
                    selected_code)
                if selected_type_company_data:
                    descr_company = selected_type_company_data.get(
                        "descr_company", "Desconhecido")
                    cod_company = selected_type_company_data.get("cod_company")
                    type_company_id = selected_type_company_data.get("id")
                    self.display_delete_confirmation(
                        type_company_id, cod_company, descr_company)


def show():
    css_path = Path("src/app/css/type_company_read.css")
    db = Database()
    deleter = TypeCompanyDeleter(db)
    deleter.load_css(css_path)

    st.subheader("Tipo de Empresa - Deletar")

    df_type_companies = deleter.get_type_company_data()
    if df_type_companies.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Descrição")
    )

    filter_value = st_keyup("Digite o valor para filtrar:", key="filter_value")

    if filter_value:
        filtered_type_companies = deleter.filter_type_companies(
            df_type_companies, filter_option, filter_value)
        deleter.display_filtered_type_companies(filtered_type_companies)
    else:
        deleter.show_type_company_table(df_type_companies)


if __name__ == "__main__":
    show()
