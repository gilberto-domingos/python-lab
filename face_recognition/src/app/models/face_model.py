class Face:
    def __init__(self, username, face_encoding, id=None):
        self.id = id
        self.username = username
        self.face_encoding = face_encoding

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_face_encoding(self):
        return self.face_encoding

    def set_face_encoding(self, face_encoding):
        self.face_encoding = face_encoding

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def display_info(self):
        print(f"ID: {self.id}, "
              f"Username: {self.username}, "
              f"Face Encoding: {self.face_encoding}")
