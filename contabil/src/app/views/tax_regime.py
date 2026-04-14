import streamlit as st
from pathlib import Path


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    css_path = Path("src/app/css/tax_regime.css")
    load_css(css_path)

    st.subheader('Escolha a opção para Regime Tributário:')

    options = [
        ("Adicionar", "tax_regime_create"),
        ("Consultar", "tax_regime_read"),
        ("Editar", "tax_regime_update"),
        ("Deletar", "tax_regime_delete")
    ]

    query_params = st.session_state.get("query_params", {})
    current_page = query_params.get("page", "tax_regime_create")

    default_index = next((i for i, opt in enumerate(
        options) if opt[1] == current_page), 0)

    choice, selected_page = st.selectbox(
        "Escolha a opção:",
        options,
        format_func=lambda x: x[0],
        index=default_index,
        key="tax_regime_select_main"
    )

    if current_page != selected_page:
        st.session_state["query_params"] = {"page": selected_page}
        st.rerun()

    if selected_page == "tax_regime_create":
        import src.app.views.tax_regime_create as tax_regime_create
        tax_regime_create.show()
    elif selected_page == "tax_regime_read":
        import src.app.views.tax_regime_read as tax_regime_read
        tax_regime_read.show()
    elif selected_page == "tax_regime_update":
        import src.app.views.tax_regime_update as tax_regime_update
        tax_regime_update.show()
    elif selected_page == "tax_regime_delete":
        import src.app.views.tax_regime_delete as tax_regime_delete
        tax_regime_delete.show()
