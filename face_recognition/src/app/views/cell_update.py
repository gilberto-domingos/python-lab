import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.cell_database import Database
from src.app.models.cell_model import Cell
from src.app.utils.validate import validate_cod, validate_email_address


class CellEditor:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        """Carrega e aplica o CSS da página."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def show_cell_table(self, df_cells):
        """Exibe a tabela de células com formatação e centralização."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_cells.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def edit_cell(self, cell):
        """Permite editar uma célula existente."""
        new_cod = st.text_input(
            "Novo Código", value=cell.get_cod_cell(), max_chars=5)
        new_name = st.text_input(
            "Novo Nome", value=cell.get_name_cell(), max_chars=50)
        new_email = st.text_input(
            "Novo Email", value=cell.get_email_cell(), max_chars=50)

        # Validação do Código
        cod_valid = True
        if new_cod and not validate_cod(new_cod):
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False

        # Validação do Email
        email_valid = True
        if new_email and not validate_email_address(new_email):
            st.error("Email inválido.")
            email_valid = False

        if st.button("Salvar Alterações") and cod_valid and email_valid:
            try:
                self.db.update_cell(
                    cell.id, new_cod, new_name, new_email)
                st.success("Célula atualizada com sucesso!")
                return new_cod, new_name, new_email
            except Exception as e:
                st.error(f"Erro ao atualizar célula: {e}")
        return None


def show():
    """Função principal para exibir a tela de edição de células."""
    css_path = Path("src/app/css/cell_update.css")
    editor = CellEditor(Database())
    editor.load_css(css_path)

    st.subheader("Células - Editar")

    try:
        all_cells = editor.db.get_all_cells()
        df_cells = pd.DataFrame(
            all_cells).drop(columns=["id"])
        df_cells.rename(columns={
            "cod_cell": "Código",
            "name_cell": "Nome",
            "email_cell": "Email"
        }, inplace=True)
    except Exception as e:
        st.error(f"Erro ao buscar células: {e}")
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if 'filtered_cells' not in st.session_state:
        st.session_state['filtered_cells'] = df_cells

    filtered_cells = st.session_state['filtered_cells']

    if filter_option == "por Código":
        cod_cell = st_keyup(
            "Digite o código da célula:", key="filter_cod")
        if cod_cell:
            filtered_cells = df_cells[df_cells['Código'].str.contains(
                cod_cell, na=False)]
            if filtered_cells.empty:
                st.warning("Nenhuma célula encontrada com esse código.")
        st.session_state['filtered_cells'] = filtered_cells

    elif filter_option == "por Nome":
        name_cell = st_keyup(
            "Digite o nome da célula:", key="filter_name")
        if name_cell:
            filtered_cells = df_cells[df_cells['Nome'].str.contains(
                name_cell, case=False, na=False)]
            if filtered_cells.empty:
                st.warning("Nenhuma célula encontrada com esse nome.")
        st.session_state['filtered_cells'] = filtered_cells

    # Exibe a tabela e a opção de edição
    if not filtered_cells.empty:
        editor.show_cell_table(filtered_cells)

        # Seleciona a primeira célula automaticamente
        selected_cell_data = filtered_cells.iloc[0]
        selected_cell = editor.db.get_cell_by_cod(
            selected_cell_data['Código'])

        cell = Cell(selected_cell['cod_cell'],
                    selected_cell['name_cell'],
                    selected_cell['email_cell'],
                    selected_cell['id'])

        updated_values = editor.edit_cell(cell)

        if updated_values:
            # Atualiza a linha da tabela diretamente com os novos dados
            filtered_cells.loc[filtered_cells['Código'] == selected_cell_data['Código'], [
                'Nome', 'Email']] = updated_values[1], updated_values[2]
            # Atualiza o estado com os dados modificados
            st.session_state['filtered_cells'] = filtered_cells
            # Reexibe a tabela com os dados atualizados
            editor.show_cell_table(filtered_cells)


if __name__ == "__main__":
    show()
