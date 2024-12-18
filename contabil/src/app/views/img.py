# pagesx/img.py
import streamlit as st
import os


def show():
    st.title("Galeria de Imagens")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(current_dir, "../img/")

    if not os.path.isdir(img_dir):
        st.error("O diretório de imagens não foi encontrado.")
        return

    img_files = [f for f in os.listdir(img_dir) if f.endswith(
        ('.png', '.jpg', '.jpeg', '.gif'))]

    for img_file in img_files:
        img_path = os.path.join(img_dir, img_file)
        st.image(img_path, caption=img_file)
