import streamlit as st
from PIL import Image

def show():
    st.title("Página do homex")

# Exibir logotipo centralizado
with st.container():
    # Usar a classe .logo para centralizar a imagem
    st.markdown('<div class="logo">', unsafe_allow_html=True)
    path = 'img/logo.png'
    imagex = Image.open(path)

    # Exibir a imagem com Streamlit
    st.image(imagex, width=200)

    st.markdown('</div>', unsafe_allow_html=True)