from p_service.operator_service import ComercialOperator


# Testando as classes e objetos


# Criando instâncias
operador1 = ComercialOperator(
    101, "12.345.678/0001-99", "Comercial XYZ", "Sul")


# Usando os getters e setters
operador1.set_cod_operator(201)


# Exibindo informações
print("Informações do Operador Comercial:")
operador1.display_info()


# Reusando objetos e métodos
print("\nAcessando atributos diretamente:")
print(f"Código do operador1: {operador1.get_cod_operator()}")
