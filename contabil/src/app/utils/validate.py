from validate_docbr import CNPJ
from email_validator import validate_email, EmailNotValidError
import re


def validate_cod(cod):
    if re.match(r'^\d{5}$', cod):
        return True
    return False


def validate_phone_customer(phone_customer):
    if re.match(r'^\d{1,11}$', phone_customer):
        return True
    return False


def validate_email_address(email_customer):
    try:
        valid = validate_email(email_customer)
        return valid.email
    except EmailNotValidError as e:
        return str(e)


def validate_cnpj(cnpj_operator):
    cnpj_validator = CNPJ()
    return cnpj_validator.validate(cnpj_operator)


if __name__ == '__main__':
    cnpj_valido = "12.345.678/0001-95"  # Um CNPJ válido 12.345.678/0001-95
    cnpj_invalido = "12.345.678/0001-00"  # Um CNPJ inválido

    print("validação do cnpj valido", validate_cnpj(cnpj_valido))   # Saída: True
    print("validação do cnpj invalido", validate_cnpj(
        cnpj_invalido))  # Saída: False
