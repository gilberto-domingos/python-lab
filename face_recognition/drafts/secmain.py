import streamlit as st
from streamlit_option_menu import option_menu
import pathlib
import psycopg2

st.set_page_config(page_title="Mosimann",
                   page_icon=":bar_chart:")


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("css/style.css")


# Configurações do banco de dados
DB_HOST = "mosimann-database"  # Nome do serviço no docker-compose
DB_PORT = 5432                # Porta padrão do PostgreSQL
DB_NAME = "contabil"          # Nome do banco de dados
DB_USER = "mmss"              # Usuário configurado
DB_PASS = "mmssmmnn"          # Senha configurada


def testar_conexao():
    """
    Função para testar a conexão com o banco de dados.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        st.success("Conexão com o banco de dados bem-sucedida!")
        conn.close()
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")


with st.sidebar:
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
            "database",  # Ícone para a opção de teste de conexão
        ],
        menu_icon="cast",
        default_index=1,
    )

if selected == "Componentes":
    from pagesx import comp
    comp.show()

elif selected == "Home":
    from pagesx import homex
    homex.show()

elif selected == "Cadastro":
    from pagesx import crud
    crud.show()

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
