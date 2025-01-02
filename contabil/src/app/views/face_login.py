import streamlit as st
import cv2
import numpy as np
import face_recognition
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from src.database.face_database import Database


class FaceLoginTransformer(VideoTransformerBase):
    def __init__(self, database):
        """
        Classe responsável pelo processamento do vídeo e reconhecimento facial.

        Args:
            database (Database): Instância da classe Database para acesso ao banco de dados.
        """
        self.db = database
        self.known_faces = self.fetch_faces()

    def fetch_faces(self):
        """
        Busca todas as faces cadastradas no banco de dados.

        Returns:
            list: Lista de tuplas contendo (username, face_encoding).
        """
        rows = self.db.get_all_faces()
        return [
            (row["username"], np.frombuffer(
                row["face_encoding"], dtype=np.float64))
            for row in rows
        ]

    def transform(self, frame):
        """
        Processa cada frame de vídeo para realizar o reconhecimento facial.

        Args:
            frame: Frame capturado pelo stream de vídeo.

        Returns:
            ndarray: Frame processado com os resultados do reconhecimento facial.
        """
        img = frame.to_ndarray(format="bgr24")
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_frame, face_locations)

        for face_encoding in face_encodings:
            for username, encoding in self.known_faces:
                match = face_recognition.compare_faces(
                    [encoding], face_encoding)
                if match[0]:
                    cv2.putText(img, f"Welcome {
                                username}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    return img
        cv2.putText(img, "Face not recognized", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return img


def login_face():
    """
    Exibe a interface de login por reconhecimento facial no Streamlit.
    """
    st.header("Login por Reconhecimento Facial")

    # Configura o banco de dados
    db = Database()
    db.connect()

    # Inicializa o streamer com o transformador
    webrtc_streamer(
        key="login",
        video_transformer_factory=lambda: FaceLoginTransformer(db)
    )
