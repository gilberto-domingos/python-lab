import streamlit as st
import cv2
import numpy as np
import face_recognition
from src.database.face_database import Database


def capture_face():
    """
    Captura uma imagem da webcam para reconhecimento facial.

    Returns:
        frame (ndarray): Imagem capturada.
        face_encoding (ndarray): Codificação do rosto detectado.
    """
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("Erro ao acessar a câmera.")
        return None, None

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    if face_encodings:
        return frame, face_encodings[0]
    return None, None


def login_face():
    """
    Exibe a interface de login por reconhecimento facial no Streamlit.
    """
    st.header("Login por Reconhecimento Facial")

    # Conectar ao banco de dados
    db = Database()
    db.connect()

    # Captura uma imagem da câmera
    st.warning("Olhe para a câmera e aguarde...")
    frame, face_encoding = capture_face()

    if frame is None:
        return

    # Verificar se o rosto foi reconhecido
    known_faces = fetch_faces_from_db(db)
    for username, encoding in known_faces:
        match = face_recognition.compare_faces([encoding], face_encoding)
        if match[0]:
            st.success(f"Bem-vindo, {username}!")
            return

    st.error("Não permitido ! Rosto não reconhecido, tente novamente.")


def fetch_faces_from_db(db):
    """
    Busca todas as faces cadastradas no banco de dados.

    Returns:
        list: Lista de tuplas contendo (username, face_encoding).
    """
    rows = db.get_all_faces()
    return [
        (row["username"], np.frombuffer(row["face_encoding"], dtype=np.float64))
        for row in rows
    ]
