import re


class Customer:
    def __init__(self, cod_customer, cell_customer, name_customer, email_customer, phone_customer, id=None):
        self.id = id
        self.cod_customer = cod_customer
        self.name_customer = name_customer
        self.cell_customer = cell_customer
        self.email_customer = email_customer
        self.phone_customer = phone_customer

    def get_phone_customer(self):
        return self.phone_customer

    def set_phone_customer(self, phone_customer):
        self.phone_customer = phone_customer

    def get_email_customer(self):
        return self.email_customer

    def set_email_customer(self, email_customer):
        self.email_customer = email_customer

    def get_cod_customer(self):
        return self.cod_customer

    def set_cod_customer(self, cod_customer):
        self.cod_customer = cod_customer

    def get_cell_customer(self):
        return self.cell_customer

    def set_cell_customer(self, cell_customer):
        self.cell_customer = cell_customer

    def get_name_customer(self):
        return self.name_customer

    def set_name_customer(self, name_customer):
        self.name_customer = name_customer

    def display_info(self):
        print(f"Código: {self.cod_customer}, "
              f"Nome: {self.name_customer}, "
              f"Célula: {self.cell_customer}, "
              f"Email: {self.email_customer}, "
              f"Telefone: {self.phone_customer}, "
              f"ID: {self.id}")
