import streamlit as st
from streamlit_option_menu import option_menu
import pathlib
import psycopg2

st.set_page_config(
    page_title="Mosimann",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("css/style.css")
st.markdown(
    """
    <style>
        button[data-testid="stBaseButton-header"] {
            display: none !important;
        }        
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        button[data-testid="stBaseButton-headerNoPadding"] { 
            box-shadow: #ff4b4b;
        }

        button[data-testid="stBaseButton-headerNoPadding"]:hover {
             color: #ff4b4b;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown(
        '''
        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 15px;">
            <div style="display: inline-flex; align-items: center; margin-bottom: 5px;">
                <span class="status-indicator" style="margin-right: 8px;"></span> 
                <span>Online</span>
            </div>
            <div style="display: inline-flex; align-items: center; margin-bottom: 5px;">
                <span class="status-indicator" style="margin-right: 8px;"></span> 
                <span>Itamar Mosimann</span>
            </div>
            <div style="display: inline-flex; align-items: center; margin-bottom: 5px;">
                <!-- Ícone de prédio com tamanho reduzido -->
                <i class="fas fa-building" style="margin-right: 8px; font-size: 13px;"></i>
                <span>Empresa : Mosimann LTDA</span>
            </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

    selected = option_menu(
        "Mosimann",
        [
            # "Componentes",
            "Home",
            "Cadastro",
            "Empresas",
            "Solicitações",
            "Método APLA",
            "Dashboards",
            "Relatórios",
            "Imagens",
            "CSV"
        ],
        icons=[
            # "list-check",
            "house",
            "list-check",
            "sliders",
            "clipboard-check",
            "building",
            "list-check",
            "people",
            "chat",
            "book",
            "bar-chart",
            "file-earmark-text",
            "file-earmark-text",
            "file-earmark-text",
            "database",
        ],
        menu_icon="cast",
        default_index=1,
    )


if selected == "Componentes":
    from views import comp
    comp.show()

elif selected == "Home":
    from views import homex
    homex.show()

elif selected == "Cadastro":
    cadastro_menu = option_menu(
        "Opções de Cadastro",
        [
            "Operadora",
            "Cliente",
            "Célula",
            "Funcionário",
            "Tipo de empresa",
            "Regime tributario",
        ],
        icons=[
            "building",
            "person-lines-fill",
            "box",
            "person-bounding-box",
            "building",
            "list-check",
        ],
        menu_icon="card-list",
        default_index=0,
        orientation="horizontal",
    )

    if cadastro_menu == "Operadora":
        from views import operator
        operator.show()

    if cadastro_menu == "Cliente":
        from views import customers
        customers.show()

    elif cadastro_menu == "Célula":
        from views import cell
        cell.show()

    elif cadastro_menu == "Funcionário":
        from views import employee
        employee.show()

    elif cadastro_menu == "Tipo de empresa":
        from views import type_company
        type_company.show()

    elif cadastro_menu == "Regime tributario":
        from views import tax_regime
        tax_regime.show()

elif selected == "Empresas":
    from views import companies
    companies.show()

elif selected == "Solicitações":
    st.title("Solicitações")

elif selected == "Método APLA":
    from views import apla
    apla.show()

elif selected == "Dashboards":
    from views import dashboards
    dashboards.show()

elif selected == "Relatórios":
    st.title("Relatórios")
    from views import report
    report.show()

elif selected == "Imagens":
    from views import img
    img.show()

elif selected == "CSV":
    from views import csv
    csv.show()
