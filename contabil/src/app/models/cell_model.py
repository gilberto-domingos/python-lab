class Cell:
    def __init__(self, cod_cell, name_cell, email_cell, id=None):
        self.id = id
        self.cod_cell = cod_cell
        self.name_cell = name_cell
        self.email_cell = email_cell

    def get_cod_cell(self):
        return self.cod_cell

    def set_cod_cell(self, cod_cell):
        self.cod_cell = cod_cell

    def get_name_cell(self):
        return self.name_cell

    def set_name_cell(self, name_cell):
        self.name_cell = name_cell

    def get_email_cell(self):
        return self.email_cell

    def set_email_cell(self, email_cell):
        self.email_cell = email_cell

    def display_info(self):
        print(f"Código: {self.cod_cell}, "
              f"Nome: {self.name_cell}, "
              f"Email: {self.email_cell}, "
              f"ID: {self.id}")
