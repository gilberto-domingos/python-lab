import streamlit as st
from pathlib import Path


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/customer.css")
    load_css(css_path)

    st.subheader('Escolha a opção para clientes')

    options = [
        ("Adicionar", "customer_create"),
        ("Consultar", "customer_read"),
        ("Editar", "customer_update"),
        ("Deletar", "customer_delete")
    ]

    query_params = st.session_state.get("query_params", {})
    current_page = query_params.get("page", "customer_create")

    default_index = next((i for i, opt in enumerate(
        options) if opt[1] == current_page), 0)
    choice, selected_page = st.selectbox(
        "Escolha a opção:",
        options,
        format_func=lambda x: x[0],
        index=default_index,
        key="customer_select_main"
    )

    if current_page != selected_page:
        st.session_state["query_params"] = {"page": selected_page}
        st.rerun()

    if selected_page == "customer_create":
        import src.app.views.customer_create as customer_create
        customer_create.show()
    elif selected_page == "customer_read":
        import src.app.views.customer_read as customer_read
        customer_read.show()
    elif selected_page == "customer_update":
        import src.app.views.customer_update as customer_update
        customer_update.show()
    elif selected_page == "customer_delete":
        import src.app.views.customer_delete as customer_delete
        customer_delete.show()
