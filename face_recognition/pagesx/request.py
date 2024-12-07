import streamlit as st

# Função para customizar o tema claro


def show():

    def light_theme():
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

    # Função para customizar o tema escuro

    def dark_theme():
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

    # Adicionar um botão para alternar entre os temas

    def show():
        # Variável de estado para armazenar o tema selecionado
        if "theme" not in st.session_state:
            # Define o tema inicial como escuro
            st.session_state["theme"] = "Escuro"

        # Alternar o tema quando o botão for clicado
        if st.button("Trocar Tema"):
            st.session_state["theme"] = "Claro" if st.session_state["theme"] == "Escuro" else "Escuro"

        # Aplica o tema de acordo com a escolha do usuário
        if st.session_state["theme"] == "Claro":
            light_theme()
        else:
            dark_theme()

        # Conteúdo do aplicativo
        st.title("Meu App com Tema Dinâmico")
        st.write("O tema foi alternado com sucesso!")

    # Chama a função para exibir o tema
    show()
