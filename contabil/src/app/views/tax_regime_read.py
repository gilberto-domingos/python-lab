import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.tax_regime_database import Database
from src.app.models.tax_regime_model import TaxRegime


class TaxRegimeReader:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_tax_regime_data(self):
        try:
            all_tax_regimes = self.db.get_all_tax_regimes()
            tax_regimes = [TaxRegime(
                tax_regime['cod_tax_regime'],
                tax_regime['descr_tax_regime'],
                tax_regime.get('id')
            ) for tax_regime in all_tax_regimes]

            df_tax_regimes = pd.DataFrame([{
                'Código': reg.cod_tax_regime,
                'Descrição': reg.descr_tax_regime
            } for reg in tax_regimes])

            return df_tax_regimes
        except Exception as e:
            st.error(f"Erro ao buscar regimes tributários: {e}")
            return pd.DataFrame()

    def show_tax_regime_table(self, df_tax_regimes):
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_tax_regimes.style.set_table_styles(
            [s1, s2]).hide(axis=0)  # Oculta índice
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_tax_regimes(self, df_tax_regimes, filter_option, filter_value):
        if filter_option == "por Código":
            return df_tax_regimes[df_tax_regimes['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Descrição":
            return df_tax_regimes[df_tax_regimes['Descrição'].str.contains(filter_value, case=False, na=False)]
        return df_tax_regimes

    def display_filtered_tax_regimes(self, filtered_tax_regimes):
        if filtered_tax_regimes.empty:
            st.warning("Nenhum regime tributário encontrado com esse critério.")
        else:
            self.show_tax_regime_table(filtered_tax_regimes)


def show():
    css_path = Path("src/app/css/tax_regime_read.css")
    db = Database()
    reader = TaxRegimeReader(db)
    reader.load_css(css_path)

    st.subheader("Regimes Tributários - consultar")

    df_tax_regimes = reader.get_tax_regime_data()
    if df_tax_regimes.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Descrição"))

    if filter_option == "por Código":
        filter_value = st_keyup(
            "Digite o código do regime tributário:", key="filter_cod")
    else:
        filter_value = st_keyup(
            "Digite a descrição do regime tributário:", key="filter_descr")

    if filter_value:
        filtered_tax_regimes = reader.filter_tax_regimes(
            df_tax_regimes, filter_option, filter_value)
        reader.display_filtered_tax_regimes(filtered_tax_regimes)
    else:
        reader.show_tax_regime_table(df_tax_regimes)


if __name__ == "__main__":
    show()
