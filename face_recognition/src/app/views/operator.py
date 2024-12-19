import streamlit as st
from pathlib import Path


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    # Definir a configuração da página aqui, se necessário

    css_path = Path("src/app/css/operator.css")
    load_css(css_path)

    st.subheader('Escolha a opção para operadoras')

    # Opções para o selectbox
    options = [
        ("Adicionar", "operator_create"),
        ("Consultar", "operator_read"),
        ("Editar", "operator_update"),
        ("Deletar", "operator_delete")
    ]

    # Obter parâmetros da URL do estado da sessão
    query_params = st.session_state.get("query_params", {})
    current_page = query_params.get("page", "operator_create")

    # Exibir selectbox
    default_index = next((i for i, opt in enumerate(
        options) if opt[1] == current_page), 0)
    choice, selected_page = st.selectbox(
        "Escolha a opção:",
        options,
        format_func=lambda x: x[0],
        index=default_index,
        key="operator_select_main"
    )

    # Atualizar o parâmetro `page` e reiniciar
    if current_page != selected_page:
        st.session_state["query_params"] = {"page": selected_page}
        st.rerun()

    # Renderizar a página correspondente
    if selected_page == "operator_create":
        import src.app.views.operator_create as operator_create
        operator_create.show()
    elif selected_page == "operator_read":
        import src.app.views.operator_read as operator_read
        operator_read.show()
    elif selected_page == "operator_update":
        import src.app.views.operator_update as operator_update
        operator_update.show()
    elif selected_page == "operator_delete":
        import src.app.views.operator_delete as operator_delete
        operator_delete.show()
