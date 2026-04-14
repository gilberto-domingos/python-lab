import streamlit as st
from pathlib import Path


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/cell.css")
    load_css(css_path)

    st.subheader('Escolha a opção para células')

    options = [
        ("Adicionar", "cell_create"),
        ("Consultar", "cell_read"),
        ("Editar", "cell_update"),
        ("Deletar", "cell_delete")
    ]

    query_params = st.session_state.get("query_params", {})
    current_page = query_params.get("page", "cell_create")

    default_index = next((i for i, opt in enumerate(
        options) if opt[1] == current_page), 0)
    choice, selected_page = st.selectbox(
        "Escolha a opção:",
        options,
        format_func=lambda x: x[0],
        index=default_index,
        key="cell_select_main"
    )

    if current_page != selected_page:
        st.session_state["query_params"] = {"page": selected_page}
        st.rerun()

    if selected_page == "cell_create":
        import src.app.views.cell_create as cell_create
        cell_create.show()
    elif selected_page == "cell_read":
        import src.app.views.cell_read as cell_read
        cell_read.show()
    elif selected_page == "cell_update":
        import src.app.views.cell_update as cell_update
        cell_update.show()
    elif selected_page == "cell_delete":
        import src.app.views.cell_delete as cell_delete
        cell_delete.show()
