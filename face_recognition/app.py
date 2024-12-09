import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Mosimann",
    page_icon=":bar_chart:",
    layout="wide",  # Configuração padrão
    initial_sidebar_state="auto"
)


# Título do aplicativo
st.title("Bem-vindo ao meu app Streamlit! ✨")

# Texto e entrada
st.write("Este é um exemplo básico de aplicativo Streamlit.")
name = st.text_input("Qual é o seu nome?")

# Botão de saudação
if st.button("Saudar"):
    st.write(f"Olá, {name}! 👋")

# Sidebar
st.sidebar.title("Navegação")
st.sidebar.write("Use esta barra lateral para configurar opções futuras.")

# Rodapé
st.markdown("---")
st.markdown("Feito com ❤️ usando [Streamlit](https://streamlit.io).")
