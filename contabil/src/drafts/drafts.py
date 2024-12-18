from decimal import Decimal


def comparate(ativo, passivo):
    # Usando Decimal para garantir precisão nos cálculos
    ativo = Decimal(ativo)
    passivo = Decimal(passivo)

    if ativo == passivo:
        return f"Os valores são iguais: R$ {ativo:.2f}"
    else:
        return f"Os valores são diferentes: R$ {ativo:.2f} vs R$ {passivo:.2f}"


# Testando a função com valores de reais
respose = comparate(12.50, 12.50)
print(respose)  # Vai imprimir: Os valores são iguais: R$ 12.50
