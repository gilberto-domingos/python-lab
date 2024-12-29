import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.cell_database import Database


class CellDeleter:
    def __init__(self, db):
        """Inicializa o deletador de células com a injeção de dependência do banco de dados."""
        self.db = db

    def load_css(self, file_path):
        """Carrega o arquivo CSS no Streamlit."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_cell_data(self):
        """Obtém todas as células do banco de dados e formata para exibição."""
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
        """Exibe a tabela de células com formatação."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_cells.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_cells(self, df_cells, filter_option, filter_value):
        """Filtra as células por código ou nome conforme a escolha do usuário."""
        if filter_option == "por Código":
            return df_cells[df_cells['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Nome":
            return df_cells[df_cells['Nome'].str.contains(filter_value, case=False, na=False)]
        return df_cells

    def delete_cell(self, cell_id):
        """Deleta a célula selecionada."""
        try:
            self.db.delete_cell(cell_id)
            st.success("Célula deletada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao deletar célula: {e}")

    def display_delete_confirmation(self, cell_name, cod_cell):
        """Exibe uma confirmação de exclusão antes de deletar a célula."""
        st.warning(f"Tem certeza que deseja deletar a célula {
                   cell_name} (Código: {cod_cell})?")
        if st.button("Deletar"):
            self.delete_cell(cod_cell)

    def display_filtered_cells(self, filtered_cells):
        """Exibe as células filtradas e permite a seleção para exclusão."""
        if filtered_cells.empty:
            st.warning("Nenhuma célula encontrada com esse critério.")
        else:
            self.show_cell_table(filtered_cells)

            # Seleção para deletar
            delete_option = st.selectbox(
                "Escolha a célula para deletar", filtered_cells['Código'].tolist())
            if delete_option:
                selected_cell = self.db.get_cell_by_cod(delete_option)
                if selected_cell:
                    self.display_delete_confirmation(
                        selected_cell['name_cell'], selected_cell['cod_cell'])


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
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if filter_option == "por Código":
        filter_value = st_keyup(
            "Digite o código da célula:", key="filter_cod")
    else:
        filter_value = st_keyup(
            "Digite o nome da célula:", key="filter_name")

    if filter_value:
        filtered_cells = deleter.filter_cells(
            df_cells, filter_option, filter_value)
        deleter.display_filtered_cells(filtered_cells)
    else:
        # Exibe a tabela sem filtro se nenhum valor for inserido
        deleter.show_cell_table(df_cells)


if __name__ == "__main__":
    show()
