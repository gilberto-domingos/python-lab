class Employee:
    def __init__(self, cod_employee, name_employee, email_employee, phone_employee, id=None):
        self.id = id
        self.cod_employee = cod_employee
        self.name_employee = name_employee
        self.email_employee = email_employee
        self.phone_employee = phone_employee

    def get_cod_employee(self):
        return self.cod_employee

    def set_cod_employee(self, cod_employee):
        self.cod_employee = cod_employee

    def get_name_employee(self):
        return self.name_employee

    def set_name_employee(self, name_employee):
        self.name_employee = name_employee

    def get_email_employee(self):
        return self.email_employee

    def set_email_employee(self, email_employee):
        self.email_employee = email_employee

    def get_phone_employee(self):
        return self.phone_employee

    def set_phone_employee(self, phone_employee):
        self.phone_employee = phone_employee

    def display_info(self):
        print(f"Código: {self.cod_employee}, "
              f"Nome: {self.name_employee}, "
              f"Email: {self.email_employee}, "
              f"Celular: {self.phone_employee}, "
              f"ID: {self.id}")
