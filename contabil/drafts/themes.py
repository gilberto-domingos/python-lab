'''
def apply_light_theme():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff;
        }
        .stSidebar {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def apply_dark_theme():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #262730;
        }
        .stSidebar {
            background-color: #262730;
        }
        .stButton>button {
            background-color: #e31b22;
            color: #fafafa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def show():
    # Inicializar o estado do tema
    if "theme" not in st.session_state:
        st.session_state["theme"] = "Escuro"

    # Alternar o tema quando o toggle for alterado
    on = st.toggle("🌓 Claro/Escuro", key="theme_toggle",
                   value=st.session_state["theme"] == "Claro")

    if on:
        st.session_state["theme"] = "Claro"
    else:
        st.session_state["theme"] = "Escuro"

    # Aplicar o tema atual
    if st.session_state["theme"] == "Claro":
        apply_light_theme()
    else:
        apply_dark_theme()
'''
# -----------------------------------------#

'''
def apply_light_theme():
    """Aplica o tema claro na página."""
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff;
        }
        .stSidebar {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def apply_dark_theme():
    """Aplica o tema escuro na página."""
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #262730;
        }
        .stSidebar {
            background-color: #262730;
        }
        .stButton>button {
            background-color: #e31b22;
            color: #fafafa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def show():
    # Inicializar o estado do tema
    if "theme" not in st.session_state:
        st.session_state["theme"] = "Escuro"

    # Alternar o tema quando o botão for clicado
    if st.button("🌓 Mudar tema", key="toggle_theme_button"):
        st.session_state["theme"] = "Claro" if st.session_state["theme"] == "Escuro" else "Escuro"

    # Aplicar o tema atual
    if st.session_state["theme"] == "Claro":
        apply_light_theme()
    else:
        apply_dark_theme()

    # Exemplo de conteúdo da página
    st.title("Página de Solicitações")
    st.write("Clique no botão acima para alternar o tema.")
'''
