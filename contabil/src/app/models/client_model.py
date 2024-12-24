import re


class Client:
    def __init__(self, cod_client, cell_client, name_client, email_client, phone_client, id_client=None):
        self.id_client = id_client
        self.cod_client = cod_client
        self.name_client = name_client
        self.cell_client = cell_client
        self.email_client = email_client
        self.phone_client = phone_client

    def get_phone_client(self):
        return self.phone_client

    def set_phone_client(self, phone_client):
        self.phone_client = phone_client

    def get_email_client(self):
        return self.email_client

    def set_email_client(self, email_client):
        self.email_client = email_client

    def get_cod_client(self):
        return self.cod_client

    def set_cod_client(self, cod_client):
        self.cod_client = cod_client

    def get_cell_client(self):
        return self.cell_client

    def set_cell_client(self, cell_client):
        self.cell_client = cell_client

    def get_name_client(self):
        return self.name_client

    def set_name_client(self, name_client):
        self.name_client = name_client

    def display_info(self):
        print(f"Código: {self.cod_client}, "
              f"Nome: {self.name_client}, "
              f"Celular: {self.cell_client}, "
              f"Email: {self.email_client}, "
              f"Telefone: {self.phone_client}, "
              f"ID: {self.id_client}")
