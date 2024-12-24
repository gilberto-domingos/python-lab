import re


def validate_cnpj(cnpj):
    if re.match(r'^\d{14}$', cnpj):
        return True
    return False


def validate_cod(cod):
    if re.match(r'^\d{5}$', cod):
        return True
    return False
