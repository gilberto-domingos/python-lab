import streamlit as st
# from src.app.views.face_create import register_face
# from src.app.views.face_login import login_face
# from src.app.views import register_face, login_face

# from .face_create import register_face
# from .face_login import login_face
from src.app.views.face_create import register_face
from src.app.views.face_create import login_face


from src.app.models.operator_model import Operator

st.title("Sistema de Reconhecimento Facial")

menu = ["Registrar", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Registrar":
    register_face()
elif choice == "Login":
    login_face()
