import streamlit as st
from streamlit_option_menu import option_menu
import pathlib
import psycopg2

st.set_page_config(
    page_title="Mosimann",
    page_icon=":bar_chart:",
    layout="wide"
)

# Função para carregar o arquivo CSS externo


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("css/style.css")

# Ocultar botão do header e footer padrão do Streamlit
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

# Configuração da barra lateral
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
            "Componentes",
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
            "list-check",
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

# Tratamento para cada opção do menu
if selected == "Componentes":
    from pagesx import comp
    comp.show()

elif selected == "Home":
    from pagesx import homex
    homex.show()

elif selected == "Cadastro":
    cadastro_menu = option_menu(
        "Opções de Cadastro",
        [
            "Clientes",
            "Célula",
            "Funcionário",
            "Tipo de empresa",
            "Regime tributario",
        ],
        icons=[
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

    if cadastro_menu == "Clientes":
        from pagesx import customers
        customers.show()

    elif cadastro_menu == "Célula":
        from pagesx import cell
        cell.show()

    elif cadastro_menu == "Funcionário":
        from pagesx import employee
        employee.show()

    elif cadastro_menu == "Tipo de empresa":
        from pagesx import comp_regis
        comp_regis.show()

    elif cadastro_menu == "Regime tributario":
        from pagesx import tax_regime
        tax_regime.show()

elif selected == "Empresas":
    from pagesx import companies
    companies.show()

elif selected == "Solicitações":
    st.title("Solicitações")

elif selected == "Método APLA":
    from pagesx import apla
    apla.show()

elif selected == "Dashboards":
    from pagesx import dashboards
    dashboards.show()

elif selected == "Relatórios":
    st.title("Relatórios")
    from pagesx import report
    report.show()

elif selected == "Imagens":
    from pagesx import img
    img.show()

elif selected == "CSV":
    from pagesx import csv
    csv.show()
