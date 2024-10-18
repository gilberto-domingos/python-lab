import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Mosimann", page_icon=":bar_chart:", layout="wide")

# Função para carregar o arquivo CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Carregar estilos CSS
load_css("css/style.css")

# Ocultar header e footer
st.markdown(
    """
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Menu lateral
with st.sidebar:
    selected = option_menu("Mosimann",
                           ["Home", 'Sistema', 'Obrigações', 'Empresas', 'Lista de entregas', 'Gestão de Pessoas',
                            'Solicitações', 'Método APLA', 'Relatórios'],
                           icons=['house', 'sliders', 'clipboard-check', 'building', 'list-check', 'people', 'chat',
                                  'book', 'file-earmark-text'],
                           menu_icon="cast",
                           default_index=0)

# Carregar e exibir as páginas com base na seleção do menu
if selected == "Home":
    from pagesx import homex
    homex.show()
elif selected == "Sistema":
    from pagesx import sys
    sys.show()
elif selected == "Obrigações":
    st.title("Obrigações")
elif selected == "Empresas":
    from pagesx import companies
    companies.show()
elif selected == "Lista de entregas":
    st.title("Lista de Entregas")
elif selected == "Gestão de Pessoas":
    st.title("Gestão de Pessoas")
elif selected == "Solicitações":
    st.title("Solicitações")
elif selected == "Método APLA":
    from pagesx import apla
    apla.show()
elif selected == "Relatórios":
    st.title("Relatórios")
    from pagesx import report
    report.show()
