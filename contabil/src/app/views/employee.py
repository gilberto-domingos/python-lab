import streamlit as st
from pathlib import Path


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/employee.css")
    load_css(css_path)

    st.subheader('Escolha a opção para funcionários')

    options = [
        ("Adicionar", "employee_create"),
        ("Consultar", "employee_read"),
        ("Editar", "employee_update"),
        ("Deletar", "employee_delete")
    ]

    query_params = st.session_state.get("query_params", {})
    current_page = query_params.get("page", "employee_create")

    default_index = next((i for i, opt in enumerate(
        options) if opt[1] == current_page), 0)
    choice, selected_page = st.selectbox(
        "Escolha a opção:",
        options,
        format_func=lambda x: x[0],
        index=default_index,
        key="employee_select_main"
    )

    if current_page != selected_page:
        st.session_state["query_params"] = {"page": selected_page}
        st.rerun()

    if selected_page == "employee_create":
        import src.app.views.employee_create as employee_create
        employee_create.show()
    elif selected_page == "employee_read":
        import src.app.views.employee_read as employee_read
        employee_read.show()
    elif selected_page == "employee_update":
        import src.app.views.employee_update as employee_update
        employee_update.show()
    elif selected_page == "employee_delete":
        import src.app.views.employee_delete as employee_delete
        employee_delete.show()
