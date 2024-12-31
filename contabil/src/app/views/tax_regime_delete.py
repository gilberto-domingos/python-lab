import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.tax_regime_database import Database
from src.app.models.tax_regime_model import TaxRegime


class TaxRegimeDeleter:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_tax_regime_data(self):
        try:
            all_tax_regimes = self.db.get_all_tax_regimes()
            tax_regimes = [
                TaxRegime(
                    id=tax_regime["id"],  # Aqui usamos 'id' corretamente
                    cod_tax_regime=tax_regime["cod_tax_regime"],
                    descr_tax_regime=tax_regime["descr_tax_regime"]
                )
                for tax_regime in all_tax_regimes
            ]

            data = [{
                "Código": tax_regime.get_cod_tax_regime(),
                "Descrição": tax_regime.get_descr_tax_regime()
            } for tax_regime in tax_regimes]

            return pd.DataFrame(data)
        except Exception as e:
            st.error(f"Erro ao buscar regimes tributários: {e}")
            return pd.DataFrame()

    def show_tax_regime_table(self, df_tax_regimes):
        styled_df = df_tax_regimes.style.set_table_styles([
            dict(selector='th', props=[('text-align', 'center')]),
            dict(selector='td', props=[('text-align', 'center')])
        ]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_tax_regimes(self, df_tax_regimes, filter_option, filter_value):
        try:
            if filter_option == "por Código":
                return df_tax_regimes[df_tax_regimes['Código'].str.contains(filter_value, na=False)]
            elif filter_option == "por Descrição":
                return df_tax_regimes[df_tax_regimes['Descrição'].str.contains(filter_value, case=False, na=False)]
        except Exception as e:
            st.error(f"Erro ao filtrar regimes tributários: {e}")
        return pd.DataFrame()

    # Aqui também usamos 'id' corretamente
    def delete_tax_regime(self, id, cod_tax_regime):
        try:
            if self.db.delete_tax_regime(id):  # A variável 'id' é usada aqui
                st.success(f"Regime tributário com Código '{
                           cod_tax_regime}' deletado com sucesso!")
            else:
                st.error(
                    "Regime tributário não encontrado ou não foi possível deletar.")
        except Exception as e:
            st.error(f"Erro ao deletar regime tributário: {e}")

    # Corrigido para 'id'
    def display_delete_confirmation(self, id, cod_tax_regime, descr_tax_regime):
        st.warning(f"Tem certeza que deseja deletar o regime tributário '{
                   descr_tax_regime}' (Código: {cod_tax_regime})?")
        if st.button("Deletar"):
            self.delete_tax_regime(id, cod_tax_regime)  # Corrigido para 'id'

    def display_filtered_tax_regimes(self, filtered_tax_regimes):
        """Exibe os regimes tributários filtrados e permite a seleção para exclusão."""
        if filtered_tax_regimes.empty:
            st.warning("Nenhum regime tributário encontrado com esse critério.")
        else:
            self.show_tax_regime_table(filtered_tax_regimes)

            selected_code = st.selectbox(
                "Escolha o regime tributário para deletar", filtered_tax_regimes['Código'].tolist(
                )
            )
            if selected_code:
                selected_tax_regime_data = self.db.get_tax_regime_by_cod(
                    selected_code)
                if selected_tax_regime_data:
                    descr_tax_regime = selected_tax_regime_data.get(
                        "descr_tax_regime", "Desconhecido")
                    cod_tax_regime = selected_tax_regime_data.get(
                        "cod_tax_regime")
                    id = selected_tax_regime_data.get(
                        "id")  # Aqui também usamos 'id'
                    self.display_delete_confirmation(
                        id, cod_tax_regime, descr_tax_regime)  # Corrigido para 'id'


def show():
    css_path = Path("src/app/css/tax_regime_delete.css")
    db = Database()
    deleter = TaxRegimeDeleter(db)
    deleter.load_css(css_path)

    st.subheader("Regimes Tributários - Deletar")

    df_tax_regimes = deleter.get_tax_regime_data()
    if df_tax_regimes.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Descrição")
    )

    filter_value = st_keyup("Digite o valor para filtrar:", key="filter_value")

    if filter_value:
        filtered_tax_regimes = deleter.filter_tax_regimes(
            df_tax_regimes, filter_option, filter_value)
        deleter.display_filtered_tax_regimes(filtered_tax_regimes)
    else:
        deleter.show_tax_regime_table(df_tax_regimes)


if __name__ == "__main__":
    show()
