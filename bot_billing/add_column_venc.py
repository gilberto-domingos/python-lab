import pandas as pd
from openpyxl import load_workbook
import random

# Abrir o arquivo Excel existente
file_path = 'files/filebill.xlsx'
wb = load_workbook(file_path)
ws = wb.active

# Lendo os dados no DataFrame
df = pd.read_excel(file_path)

# Criar uma cópia do DataFrame
df = df.copy()

# Verificar se a coluna 'Vencimento' existe
if 'Vencimento' in df.columns:
    # Percorrer cada linha da coluna 'Vencimento'
    for index in range(len(df)):
        data_vencimento = df.loc[index, 'Vencimento']
        # Separar dia, mês e ano
        dia, mes, ano = map(int, data_vencimento.split('/'))

        # Gerar novos dia e mês aleatórios
        novo_dia = random.randint(1, 31)
        novo_mes = random.randint(1, 12)

        # Criar a nova data com dia e mês aleatórios
        nova_data_vencimento = f'{novo_dia:02}/{novo_mes:02}/{ano}'

        # Substituir a data na coluna
        df.loc[index, 'Vencimento'] = nova_data_vencimento

    # Salvando o DataFrame modificado no arquivo Excel
    df.to_excel(file_path, index=False)

    print("Datas de vencimento alteradas com sucesso!")
else:
    print("Coluna 'Vencimento' não encontrada no arquivo.")