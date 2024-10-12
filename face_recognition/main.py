import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Mosimann", page_icon=":bar_chart:", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("css/style.css")

st.markdown(
    """
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    selected = option_menu("Mosimann",
                           ["Home", 'Sistema', 'Obrigações', 'Empresas', 'Lista de entregas', 'Gestão de Pessoas',
                            'Solicitações', 'Método APLA', 'Relatórios'],
                           icons=['house', 'sliders', 'clipboard-check', 'building', 'list-check', 'people', 'chat',
                                  'book', 'file-earmark-text'],
                           menu_icon="cast",
                           default_index=0)


if selected == "Home":
    import pagesx.homex as homex
    homex.show()
elif selected == "Sistema":
    import pagesx.sys as sys
    sys.show()
elif selected == "Obrigações":
    st.title("Obrigações")
elif selected == "Empresas":
    import pagesx.companies as companies
    companies.show()
elif selected == "Lista de entregas":
    st.title("Lista de Entregas")
elif selected == "Gestão de Pessoas":
    st.title("Gestão de Pessoas")
elif selected == "Solicitações":
    st.title("Solicitações")
elif selected == "Método APLA":
    st.title("Método APLA")
elif selected == "Relatórios":
    st.title("Relatórios")
