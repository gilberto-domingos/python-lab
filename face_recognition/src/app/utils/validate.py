from validate_docbr import CNPJ
from email_validator import validate_email, EmailNotValidError
import re
import phonenumbers
from phonenumbers import geocoder, carrier, NumberParseException


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


def validate_brazilian_phone(phone_customer):
    try:
        parsed_number = phonenumbers.parse(phone_customer, "BR")

        if not phonenumbers.is_valid_number(parsed_number):
            return False, "Número inválido."

        phone_type = carrier.name_for_number(parsed_number, "pt")
        region = geocoder.description_for_number(parsed_number, "pt")

        return True, {
            "formato_e164": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "formato_nacional": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL),
            "operadora": phone_type,
            "região": region
        }
    except NumberParseException as e:
        return False, str(e)


if __name__ == '__main__':
    #    cnpj_valido = "12.345.678/0001-95"  # Um CNPJ válido 12.345.678/0001-95
    #    cnpj_invalido = "12.345.678/0001-00"  # Um CNPJ inválido

    #    print("validação do cnpj valido", validate_cnpj(cnpj_valido))   # Saída: True
    #    print("validação do cnpj invalido", validate_cnpj(
    #        cnpj_invalido))  # Saída: False

    # Teste
    numero_valido = "+55 11 91234-5678"
    numero_invalido = "123456"

    # Número válido  "(47) 91234-5678"
    # print(validate_brazilian_phone(numero_invalido))
