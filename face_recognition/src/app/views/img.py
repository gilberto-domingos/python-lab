# pagesx/img.py
import streamlit as st
import os

def show():
    st.title("Galeria de Imagens")
    
    # Diretório onde as imagens estão armazenadas
    img_dir = './img/'

    # Verifique se o diretório existe
    if not os.path.isdir(img_dir):
        st.error("O diretório de imagens não foi encontrado.")
        return

    # Liste todos os arquivos de imagem no diretório
    img_files = [f for f in os.listdir(img_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Exibe cada imagem
    for img_file in img_files:
        img_path = os.path.join(img_dir, img_file)
        st.image(img_path, caption=img_file)
