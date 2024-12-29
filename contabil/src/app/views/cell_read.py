import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.cell_database import Database


class CellReader:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_cell_data(self):
        try:
            all_cells = self.db.get_all_cells()
            df_cells = pd.DataFrame(all_cells).drop(columns=["id"])
            df_cells.rename(columns={
                "cod_cell": "Código",
                "name_cell": "Nome",
                "email_cell": "Email"
            }, inplace=True)
            return df_cells
        except Exception as e:
            st.error(f"Erro ao buscar células: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

    def show_cell_table(self, df_cells):
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_cells.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_cells(self, df_cells, filter_option, filter_value):
        if filter_option == "por Código":
            return df_cells[df_cells['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Nome":
            return df_cells[df_cells['Nome'].str.contains(filter_value, case=False, na=False)]
        return df_cells

    def display_filtered_cells(self, filtered_cells):
        if filtered_cells.empty:
            st.warning("Nenhuma célula encontrada com esse critério.")
        else:
            self.show_cell_table(filtered_cells)


def show():
    css_path = Path("src/app/css/cell_read.css")
    db = Database()
    reader = CellReader(db)
    reader.load_css(css_path)

    st.subheader("Células - Consultar")

    df_cells = reader.get_cell_data()
    if df_cells.empty:
        return  # Caso não haja dados para exibir, retornamos

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if filter_option == "por Código":
        filter_value = st_keyup("Digite o código da célula:", key="filter_cod")
    else:
        filter_value = st_keyup("Digite o nome da célula:", key="filter_name")

    if filter_value:
        filtered_cells = reader.filter_cells(
            df_cells, filter_option, filter_value)
        reader.display_filtered_cells(filtered_cells)
    else:
        reader.show_cell_table(df_cells)


if __name__ == "__main__":
    show()
