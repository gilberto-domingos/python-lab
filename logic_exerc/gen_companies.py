import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Creating an instance of Faker with Brazilian locale
fake = Faker('pt_BR')

# Functions to generate unique data
def generate_company():
    suffixes = ['ME', 'EPP', 'GE']
    return f'{fake.company()} - {random.choice(suffixes)}'

def generate_product_name():
    product_names = ['bed(Q)', 'bed(I)', 'bed(C)', 'bed(E)', 'bed(Y)', 'bed(X)', 'bed(W)', 'bed(V)', 'bed(T)', 'bed(R)']
    return random.choice(product_names)

def generate_cnpj():
    return fake.cnpj()

def generate_title():
    return f'{random.randint(10000000, 99999999)}'

def generate_process_code():
    return f'P{random.randint(1000000000, 9999999999)}'

def generate_product_code():
    return f'P{random.randint(100000, 999999)}'

def generate_weight_code():
    return f'{random.randint(1, 9)},{random.randint(10, 99)}kg'

def generate_size_code():
    return f'{random.randint(1, 9)},{random.randint(10, 99)}mts'

def generate_employee_code():
    return random.randint(1000, 9999)

def generate_sale():
    sale_value = round(random.uniform(100.0, 10000.0), 2)
    return f'R$ {format(sale_value, ".2f").replace(".", ",")}'

def generate_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date).strftime('%d/%m/%Y')

# Ensuring the data is unique
companies = []
while len(companies) < 500:
    company = generate_company()
    if company not in companies:
        companies.append(company)

product_names = []
while len(product_names) < 500:
    product = generate_product_name()
    if product_names.count(product) < 50:  # Limit each product to appear at most 50 times
        product_names.append(product)

cnpjs = []
while len(cnpjs) < 500:
    cnpj = generate_cnpj()
    if cnpj not in cnpjs:
        cnpjs.append(cnpj)

titles = []
while len(titles) < 500:
    title = generate_title()
    if title not in titles:
        titles.append(title)

process_codes = []
while len(process_codes) < 500:
    process_code = generate_process_code()
    if process_code not in process_codes:
        process_codes.append(process_code)

product_codes = []
while len(product_codes) < 500:
    product_code = generate_product_code()
    if product_code not in product_codes:
        product_codes.append(product_code)

employee_codes = []
while len(employee_codes) < 500:
    employee_code = generate_employee_code()
    if employee_code not in employee_codes:
        employee_codes.append(employee_code)

weight_codes = []
while len(weight_codes) < 500:
    weight_code = generate_weight_code()
    if weight_code not in weight_codes:
        weight_codes.append(weight_code)

size_codes = []
while len(size_codes) < 500:
    size_code = generate_size_code()
    if size_code not in size_codes:
        size_codes.append(size_code)

sales = []
while len(sales) < 500:
    sale = generate_sale()
    if sale not in sales:
        sales.append(sale)

dates = []
while len(dates) < 500:
    date = generate_date()
    if date not in dates:
        dates.append(date)

# Creating the DataFrame
data = {
    'Empresa': companies,
    'CNPJ': cnpjs,
    'Título': titles,
    'Processo': process_codes,
    'Produto': product_codes,
    'Nome': product_names,
    'Peso(Kg)': weight_codes,
    'Tam': size_codes,
    'Funcionário': employee_codes,
    'Venda': sales,
    'Data': dates,
    'Comissão': [''] * 500  # Adding empty "Commission" column
}

df = pd.DataFrame(data)

# Calculate and add commission
def calculate_commission(sale_value):
    # Remove "R$ " and replace "," with "."
    sale_value = sale_value.replace("R$ ", "").replace(",", ".")
    sale_value = float(sale_value)
    commission = sale_value * 0.10
    # Format commission as currency with two decimal places
    return f'R$ {format(commission, ".2f").replace(".", ",")}'

df['Comissão'] = df['Venda'].apply(calculate_commission)

# Format 'Venda' column to ensure two decimal places
df['Venda'] = df['Venda'].apply(lambda x: f'R$ {format(float(x.replace("R$ ", "").replace(",", ".")), ".2f").replace(".", ",")}')

# Saving to an Excel file in the current directory
file_path = '../bot_auto/bot_files/com_vendas.xlsx'
df.to_excel(file_path, index=False)
print(f'File saved as {file_path}')
