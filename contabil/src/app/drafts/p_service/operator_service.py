from p_model.operator_model import Operator


class ComercialOperator(Operator):
    def __init__(self, cod_operator, cnpj_operator, name_operator, region):
        super().__init__(cod_operator, cnpj_operator, name_operator)
        self.region = region  # Novo atributo

    # Polimorfismo: Sobrescrevendo o método display_info
    def display_info(self):
        super().display_info()  # Chama o método da classe pai
        print(f"Região: {self.region}")
