import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.type_company_database import Database
from src.app.models.type_company_model import TypeCompany


class TypeCompanyReader:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_type_company_data(self):
        try:
            all_companies = self.db.get_all_type_companies()
            companies = [TypeCompany(
                company['cod_company'],
                company['descr_company'],
                company['id']
            ) for company in all_companies]

            df_companies = pd.DataFrame([{
                'Código': comp.cod_company,
                'Descrição': comp.descr_company,
                'ID': comp.id
            } for comp in companies])

            return df_companies
        except Exception as e:
            st.error(f"Erro ao buscar tipo de empresa: {e}")
            return pd.DataFrame()

    def show_company_table(self, df_companies):
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_companies.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_companies(self, df_companies, filter_option, filter_value):
        if filter_option == "por Código":
            return df_companies[df_companies['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Descrição":
            return df_companies[df_companies['Descrição'].str.contains(filter_value, case=False, na=False)]
        return df_companies

    def display_filtered_companies(self, filtered_companies):
        if filtered_companies.empty:
            st.warning("Nenhum tipo de empresa encontrado com esse critério.")
        else:
            self.show_company_table(filtered_companies)


def show():
    css_path = Path("src/app/css/type_company_read.css")
    db = Database()
    reader = TypeCompanyReader(db)
    reader.load_css(css_path)

    st.subheader("Tipos de Empresa - consultar")

    df_companies = reader.get_type_company_data()
    if df_companies.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Descrição"))

    if filter_option == "por Código":
        filter_value = st_keyup(
            "Digite o código do tipo de empresa:", key="filter_cod")
    else:
        filter_value = st_keyup(
            "Digite a descrição do tipo de empresa:", key="filter_descr")

    if filter_value:
        filtered_companies = reader.filter_companies(
            df_companies, filter_option, filter_value)
        reader.display_filtered_companies(filtered_companies)
    else:
        reader.show_company_table(df_companies)


if __name__ == "__main__":
    show()
