import streamlit as st
from PIL import Image

# Defina os nomes que você deseja exibir no menu
menu_options = {
    "home": "Página Inicial",
    "companies": "Empresas",
    "sys": "Sistemas"
}

# Carregar o CSS externo
with open("../css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Criar um seletor no corpo principal da página
selected_page = st.selectbox("Navegação", list(menu_options.values()))

# Lógica para renderizar as páginas com base na seleção
if selected_page == "Página Inicial":
    st.title("Bem-vindo à Página Inicial")
    # Adicione o conteúdo da página inicial aqui
elif selected_page == "Empresas":
    st.title("Empresas")
    # Certifique-se de que companies.py está na pasta pages
    import pagesx.comp_regis as comp_regis
    comp_regis.show()  # Chame a função show() da página companies.py
elif selected_page == "Sistemas":
    st.title("Sistemas")
    import pagesx.sys as sys  # Certifique-se de que sys.py está na pasta pages
    sys.show()  # Chame a função show() da página sys.py

# Exibir logotipo centralizado
with st.container():
    st.markdown('<div class="logo">', unsafe_allow_html=True)
    path = '../img/logo.png'

    try:
        imagex = Image.open(path)
        st.image(imagex, width=200)
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")

    st.markdown('</div>', unsafe_allow_html=True)
