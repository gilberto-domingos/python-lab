import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.app.models.cell_model import Cell
from src.database.cell_database import Database


class CellDeleter:
    def __init__(self, db):
        """Inicializa o deletador de células com a injeção de dependência do banco de dados."""
        self.db = db

    def load_css(self, file_path):
        """Carrega o arquivo CSS no Streamlit."""
        try:
            with open(file_path) as f:
                st.markdown(f"<style>{f.read()}</style>",
                            unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erro ao carregar CSS: {e}")

    def get_cell_data(self):
        """Obtém todas as células do banco de dados e formata para exibição."""
        try:
            all_cells = self.db.get_all_cells()
            cells = [Cell(**cell_data) for cell_data in all_cells]

            data = [
                {
                    "Código": cell.get_cod_cell(),
                    "Nome": cell.get_name_cell(),
                    "Email": cell.get_email_cell(),
                }
                for cell in cells
            ]
            return pd.DataFrame(data)
        except Exception as e:
            st.error(f"Erro ao buscar células: {e}")
            return pd.DataFrame()

    def show_cell_table(self, df_cells):
        """Exibe a tabela de células com formatação e oculta o índice."""
        if not df_cells.empty:
            styled_df = df_cells.style.set_table_styles([
                dict(selector='th', props=[('text-align', 'center')]),
                dict(selector='td', props=[('text-align', 'center')])
            ]).hide(axis=0)  # Oculta índice
            st.markdown('<div style="display: flex; justify-content: center;">' +
                        styled_df.to_html() + '</div>', unsafe_allow_html=True)
        else:
            st.warning("Nenhuma célula cadastrada no momento.")

    def filter_cells(self, df_cells, filter_option, filter_value):
        """Filtra as células por código ou nome conforme a escolha do usuário."""
        try:
            if filter_option == "por Código":
                return df_cells[df_cells['Código'].str.contains(filter_value, na=False)]
            elif filter_option == "por Nome":
                return df_cells[df_cells['Nome'].str.contains(filter_value, case=False, na=False)]
        except Exception as e:
            st.error(f"Erro ao filtrar células: {e}")
        return pd.DataFrame()

    def delete_cell(self, cell_id, cod_cell):
        """Deleta a célula selecionada."""
        try:
            if self.db.delete_cell(cell_id):
                st.success(f"Célula com Código '{
                           cod_cell}' deletada com sucesso!")
            else:
                st.error("Célula não encontrada ou não foi possível deletar.")
        except Exception as e:
            st.error(f"Erro ao deletar célula: {e}")

    def display_delete_confirmation(self, cell_id, cod_cell, name_cell):
        """Exibe uma confirmação de exclusão antes de deletar a célula."""
        st.warning(f"Tem certeza que deseja deletar a célula '{
                   name_cell}' (Código: {cod_cell})?")
        if st.button("Deletar"):
            self.delete_cell(cell_id, cod_cell)

    def display_filtered_cells(self, filtered_cells):
        """Exibe as células filtradas e permite a seleção para exclusão."""
        if filtered_cells.empty:
            st.warning("Nenhuma célula encontrada com esse critério.")
        else:
            self.show_cell_table(filtered_cells)

            selected_code = st.selectbox(
                "Escolha a célula para deletar", filtered_cells['Código'].tolist(
                )
            )
            if selected_code:
                selected_cell_data = self.db.get_cell_by_cod(selected_code)
                if selected_cell_data:
                    name_cell = selected_cell_data.get(
                        "name_cell", "Desconhecido")
                    cod_cell = selected_cell_data.get(
                        "cod_cell")
                    cell_id = selected_cell_data.get("id")
                    self.display_delete_confirmation(
                        cell_id, cod_cell, name_cell)


def show():
    css_path = Path("src/app/css/cell_delete.css")
    db = Database()
    deleter = CellDeleter(db)

    deleter.load_css(css_path)
    st.subheader("Células - Deletar")

    df_cells = deleter.get_cell_data()
    if df_cells.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome")
    )
    filter_value = st_keyup("Digite o valor para filtrar:", key="filter_value")

    if filter_value:
        filtered_cells = deleter.filter_cells(
            df_cells, filter_option, filter_value)
        deleter.display_filtered_cells(filtered_cells)
    else:
        deleter.show_cell_table(df_cells)


if __name__ == "__main__":
    show()
