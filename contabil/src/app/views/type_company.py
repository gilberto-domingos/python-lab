import streamlit as st
from pathlib import Path


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/type_company.css")
    load_css(css_path)

    st.subheader('Escolha a opção para tipos de empresa')

    options = [
        ("Adicionar", "type_company_create"),
        ("Consultar", "type_company_read"),
        ("Editar", "type_company_update"),
        ("Deletar", "type_company_delete")
    ]

    query_params = st.session_state.get("query_params", {})
    current_page = query_params.get("page", "type_company_create")

    default_index = next((i for i, opt in enumerate(
        options) if opt[1] == current_page), 0)
    choice, selected_page = st.selectbox(
        "Escolha a opção:",
        options,
        format_func=lambda x: x[0],
        index=default_index,
        key="type_company_select_main"
    )

    if current_page != selected_page:
        st.session_state["query_params"] = {"page": selected_page}
        st.rerun()

    if selected_page == "type_company_create":
        import src.app.views.type_company_create as type_company_create
        type_company_create.show()
    elif selected_page == "type_company_read":
        import src.app.views.type_company_read as type_company_read
        type_company_read.show()
    elif selected_page == "type_company_update":
        import src.app.views.type_company_update as type_company_update
        type_company_update.show()
    elif selected_page == "type_company_delete":
        import src.app.views.type_company_delete as type_company_delete
        type_company_delete.show()
