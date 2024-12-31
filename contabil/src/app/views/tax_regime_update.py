import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.tax_regime_database import Database
from src.app.models.tax_regime_model import TaxRegime
from src.app.utils.validate import validate_cod


class TaxRegimeEditor:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        """Carrega e aplica o CSS da página."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def show_tax_regime_table(self, df_tax_regimes):
        """Exibe a tabela de regimes tributários com formatação e centralização."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_tax_regimes.style.set_table_styles(
            [s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def edit_tax_regime(self, tax_regime):
        """Permite editar um regime tributário existente."""
        new_cod = st.text_input(
            "Novo Código", value=tax_regime.get_cod_tax_regime(), max_chars=5)
        new_descr = st.text_input(
            "Nova Descrição", value=tax_regime.get_descr_tax_regime(), max_chars=50)

        cod_valid = True
        if new_cod and not validate_cod(new_cod):
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False

        if st.button("Salvar Alterações"):
            if not cod_valid:
                st.error("Corrija os erros antes de salvar.")
            else:
                try:
                    self.db.update_tax_regime(
                        tax_regime.id, new_cod, new_descr)
                    st.success("Regime Tributário atualizado com sucesso!")
                    return new_cod, new_descr
                except Exception as e:
                    st.error(f"Erro ao atualizar regime tributário: {e}")
        return None


def show():
    """Função principal para exibir a tela de edição de regimes tributários."""
    css_path = Path("src/app/css/tax_regime_update.css")
    editor = TaxRegimeEditor(Database())
    editor.load_css(css_path)

    st.subheader("Regimes Tributários - Editar")

    try:
        all_tax_regimes = editor.db.get_all_tax_regimes()
        df_tax_regimes = pd.DataFrame(
            all_tax_regimes).drop(columns=["id"])
        df_tax_regimes.rename(columns={
            "cod_tax_regime": "Código",
            "descr_tax_regime": "Descrição"
        }, inplace=True)
    except Exception as e:
        st.error(f"Erro ao buscar regimes tributários: {e}")
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Descrição"))

    if 'filtered_tax_regimes' not in st.session_state:
        st.session_state['filtered_tax_regimes'] = df_tax_regimes

    filtered_tax_regimes = st.session_state['filtered_tax_regimes']

    if filter_option == "por Código":
        cod_tax_regime = st_keyup(
            "Digite o código do regime tributário:", key="filter_cod")
        if cod_tax_regime:
            filtered_tax_regimes = df_tax_regimes[df_tax_regimes['Código'].str.contains(
                cod_tax_regime, na=False)]
            if filtered_tax_regimes.empty:
                st.warning(
                    "Nenhum regime tributário encontrado com esse código.")
        st.session_state['filtered_tax_regimes'] = filtered_tax_regimes

    elif filter_option == "por Descrição":
        descr_tax_regime = st_keyup(
            "Digite a descrição do regime tributário:", key="filter_descr")
        if descr_tax_regime:
            filtered_tax_regimes = df_tax_regimes[df_tax_regimes['Descrição'].str.contains(
                descr_tax_regime, case=False, na=False)]
            if filtered_tax_regimes.empty:
                st.warning(
                    "Nenhum regime tributário encontrado com essa descrição.")
        st.session_state['filtered_tax_regimes'] = filtered_tax_regimes

    if not filtered_tax_regimes.empty:
        editor.show_tax_regime_table(filtered_tax_regimes)

        selected_tax_regime_data = filtered_tax_regimes.iloc[0]
        selected_tax_regime = editor.db.get_tax_regime_by_cod(
            selected_tax_regime_data['Código'])

        tax_regime = TaxRegime(selected_tax_regime['cod_tax_regime'],
                               selected_tax_regime['descr_tax_regime'],
                               selected_tax_regime['id'])

        updated_values = editor.edit_tax_regime(tax_regime)

        if updated_values:
            filtered_tax_regimes.loc[filtered_tax_regimes['Código'] == selected_tax_regime_data['Código'], [
                'Descrição']] = updated_values[1]
            st.session_state['filtered_tax_regimes'] = filtered_tax_regimes
            editor.show_tax_regime_table(filtered_tax_regimes)


if __name__ == "__main__":
    show()
