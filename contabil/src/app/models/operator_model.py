class Operator:
    def __init__(self, cod_operator, cnpj_operator, name_operator):
        self.cod_operator = cod_operator
        self.cnpj_operator = cnpj_operator
        self.name_operator = name_operator

    def get_cod_operator(self):
        return self.cod_operator

    def set_cod_operator(self, cod_operator):
        self.cod_operator = cod_operator

    def get_cnpj_operator(self):
        return self.cnpj_operator

    def set_cnpj_operator(self, cnpj_operator):
        self.cnpj_operator = cnpj_operator

    def get_name_operator(self):
        return self.name_operator

    def set_name_operator(self, name_operator):
        self.name_operator = name_operator

    def display_info(self):
        print(f"Código: {self.cod_operator}, CNPJ: {
              self.cnpj_operator}, Nome: {self.name_operator}")
