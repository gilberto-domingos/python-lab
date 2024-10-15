import pandas as pd
import os
import streamlit as st

def show():
    # Carregar o arquivo situation.xlsx
    try:
        df = pd.read_excel("./data/situationx.xlsx")
    except FileNotFoundError:
        st.error("Arquivo 'situationx.xlsx' não encontrado. Verifique o caminho e tente novamente.")
        st.stop()

    # Criar um resumo estatístico
    summary = df.describe(include='all')

    # Remover a linha 'unique' do resumo
    summary = summary.drop(index='unique')
    summary = summary.drop(index='top')

    # Criar um DataFrame com as colunas traduzidas
    translated_summary = summary.rename(index={
        'count': 'contagem',
        'top': 'topo',
        'freq': 'frequência',
        'mean': 'média',
        'std': 'desvio padrão',
        'min': 'mínimo',
        '25%': '25%',
        '50%': 'mediana',
        '75%': '75%',
        'max': 'máximo'
    }).fillna('Nenhum')  # Substituir NaN por 'Nenhum'

    # Contar valores únicos nas colunas 'Célula' e 'Empresa'
    unique_celulas = df['Célula'].value_counts()
    unique_empresas = df['Empresa'].value_counts()

    # Criar um DataFrame para o relatório
    report_df = pd.DataFrame({
        'Célula': unique_celulas.index,
        'Contagem de Célula': unique_celulas.values
    })

    report_empresas_df = pd.DataFrame({
        'Empresa': unique_empresas.index,
        'Contagem de Empresa': unique_empresas.values
    })

    # Verificar se o diretório data existe e criar se não existir
    os.makedirs("data", exist_ok=True)

    # Salvar o relatório em um arquivo Excel
    output_report_path = os.path.join("data", "relatorio_situationx.xlsx")

    with pd.ExcelWriter(output_report_path) as writer:
        translated_summary.to_excel(writer, sheet_name='Resumo Estatístico')
        report_df.to_excel(writer, sheet_name='Contagem de Células', index=False)
        report_empresas_df.to_excel(writer, sheet_name='Contagem de Empresas', index=False)

    # Exibir o resumo estatístico na interface Streamlit
    st.subheader("Resumo Estatístico")
    st.dataframe(translated_summary)

    st.subheader("Contagem de Células")
    st.dataframe(report_df)

    st.subheader("Contagem de Empresas")
    st.dataframe(report_empresas_df)

# Chamar a função show() para executar
show()
