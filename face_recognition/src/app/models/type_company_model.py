class TypeCompany:
    def __init__(self, cod_company, descr_company, id=None):
        self.id = id
        self.cod_company = cod_company
        self.descr_company = descr_company

    def get_cod_company(self):
        return self.cod_company

    def set_cod_company(self, cod_company):
        self.cod_company = cod_company

    def get_descr_company(self):
        return self.descr_company

    def set_descr_company(self, descr_company):
        self.descr_company = descr_company

    def display_info(self):
        print(f"Código: {self.cod_company}, "
              f"Descrição: {self.descr_company}, "
              f"ID: {self.id}")
