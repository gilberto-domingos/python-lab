import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Função para gerar datas aleatórias entre 2020 e 2024
def gerar_data_aleatoria():
    inicio = datetime(2020, 1, 1)
    fim = datetime(2024, 12, 31)
    delta = fim - inicio
    random_days = random.randint(0, delta.days)
    return inicio + timedelta(days=random_days)

# Definir o caminho para o arquivo situation2.xlsx
file_path = os.path.join("..", "data", "situation2.xlsx")

# Ler o arquivo original
df = pd.read_excel(file_path)

# Definir os novos valores para a coluna 'Célula'
novas_celulas = ['LETÍCIA', 'MARCOS', 'ANA', 'JOSÉ', 'CARLA']
df['Célula'] = [random.choice(novas_celulas) for _ in range(len(df))]

# Definir os novos valores para a coluna 'Empresa'
novas_empresas = [
    'MOURA S.A',
    'REZENDE LTDA',
    'BARBOSA S.A',
    'DOMINGOS LTDA',
    'DUARTE S.A',
    'CARDOSO LTDA',
    'FERREIRA S.A',
    'GONÇALVES LTDA'
]
df['Empresa'] = [random.choice(novas_empresas) for _ in range(len(df))]

# Gerar datas aleatórias para a coluna 'Auditado'
df['Auditado'] = [gerar_data_aleatoria() for _ in range(len(df))]

# Salvar o novo arquivo
output_path = os.path.join("..", "data", "situationx.xlsx")
df.to_excel(output_path, index=False)

print(f"Arquivo gerado com sucesso em: {output_path}")
