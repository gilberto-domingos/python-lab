import streamlit as st
import cv2
import face_recognition
from src.database.face_database import Database
from src.app.models.face_model import Face


class FaceRegistration:
    def __init__(self, database):
        self.db = database

    def capture_face(self):
        st.warning("Olhe para a câmera e aguarde...")
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if not ret:
            return None, None

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_frame, face_locations)

        if face_encodings:
            return frame, face_encodings[0]
        return None, None

    def save_face(self, username, face_encoding):
        face = Face(username=username, face_encoding=face_encoding.tobytes())
        self.db.insert_face(face.username, face.face_encoding)

    def register(self, username):
        frame, face_encoding = self.capture_face()

        if frame is None:
            st.error("Erro ao acessar a câmera.")
            return

        if face_encoding is None:
            st.error("Nenhum rosto detectado. Tente novamente.")
            return

        self.save_face(username, face_encoding)
        st.success(f"Usuário {username} registrado com sucesso!")


def register_face():
    st.header("Registrar Novo Usuário")

    username = st.text_input("Nome de Usuário")
    capture = st.button("Capturar Rosto")

    if capture and username:
        db = Database()
        db.connect()

        face_registration = FaceRegistration(database=db)
        face_registration.register(username)
