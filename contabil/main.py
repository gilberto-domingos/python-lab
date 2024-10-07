import streamlit as st
from streamlit_option_menu import option_menu

# Adicionando estilo CSS para personalizar o menu
st.markdown(
    """
    <style>
    /* Remove o fundo preto do sidebar */
    [data-testid="stSidebar"] {
        border-right-style: solid;
        border-right-width: thin;
        border-right-color: #7d7d83;
    }

    /* Estilo para o item selecionado */
    .nav-link-selected {
        background-color: blue !important; /* Altere para a cor desejada */
        color: white !important; /* Cor do texto no item selecionado */
    }

    /* Estilo para os links do menu */
    .nav-link {
        color: black; /* Cor do texto dos links não selecionados */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1. Sidebar Menu
with st.sidebar:
    selected = option_menu("Mosimann",
                           ["Home", 'Sistema', 'Obrigações', 'Empresas', 'Lista de entregas', 'Gestão de Pessoas',
                            'Solicitações', 'Método APLA', 'Relatórios'],
                           icons=['house', 'sliders', 'clipboard-check', 'building', 'list-check', 'people', 'chat',
                                  'book', 'file-earmark-text'],
                           menu_icon="cast",
                           default_index=0)  # Altere para 0 para que "Home" seja a opção padrão

# Exemplo de como você pode usar a seleção
if selected == "Home":
    st.title("Página Inicial")
elif selected == "Sistema":
    st.title("Sistema")
elif selected == "Obrigações":
    st.title("Obrigações")
elif selected == "Empresas":
    st.title("Empresas")
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