import os
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
from src.gen_file import df

# Carregar o arquivo CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '../data/supermarket_sales.csv')

# Dicionário de traduções
translations = {
    'Yangon': 'Brusque',
    'Naypyitaw': 'Balneário',
    'Mandalay': 'Blumenau',
    'City': 'Cidade',
    'Date': 'Data',
    'Home and lifestyle': 'Estilo de vida',
    'Sports and travel': 'Esportes e viagens',
    'Health and beauty': 'Saúde e beleza',
    'Fashion accessories': 'Acessórios de moda',
    'Electronic accessories': 'Acessórios eletrônicos',
    'Food and beverages': 'Comida e bebidas',
    'cash': 'Dinheiro',
    'credit card': 'Cartão de crédito',
    'Ewallet': 'Compras online'
}

# Substituir palavras
df.replace(translations, inplace=True)

# Salvar o DataFrame alterado de volta ao arquivo CSV
df.to_csv(file_path, index=False)

print("Substituições feitas com sucesso!")
