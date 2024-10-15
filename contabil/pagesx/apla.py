import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    # Carregar o arquivo situation.xlsx
    try:
        df = pd.read_excel("./data/situationx.xlsx")
    except FileNotFoundError:
        st.error("Arquivo 'situation.xlsx' não encontrado. Verifique o caminho e tente novamente.")
        st.stop()

    # Ajuste no formato das colunas
    df.columns = df.columns.str.strip()  # Remover possíveis espaços
    data_columns = df.columns[3:]  # As colunas de datas começam a partir da quarta coluna

    # Título da Dashboard
    st.title("Dashboard de Empresas e Células")

    # Mostrar uma amostra dos dados
    st.subheader("Dados - Amostra")
    st.dataframe(df.head())

    # Objetivo 1: Distribuição por Empresa
    st.subheader("Distribuição de Registros por Empresa")
    empresa_counts = df['Empresa'].value_counts()

    fig1 = px.bar(
        empresa_counts,
        x=empresa_counts.index,
        y=empresa_counts.values,
        labels={'x': 'Empresa', 'y': 'Quantidade de Registros'},
        title="Distribuição de Registros por Empresa"
    )
    st.plotly_chart(fig1)

    # Objetivo 2: Distribuição por Célula
    st.subheader("Distribuição de Registros por Célula")
    celula_counts = df['Célula'].value_counts()

    fig2 = px.bar(
        celula_counts,
        x=celula_counts.index,
        y=celula_counts.values,
        labels={'x': 'Célula', 'y': 'Quantidade de Registros'},
        title="Distribuição de Registros por Célula"
    )
    st.plotly_chart(fig2)

    # Objetivo 3: Evolução ao longo das datas
    st.subheader("Evolução Temporal")

    # Exibir dados nas colunas de data para verificação
    st.write("Dados nas colunas de data:")
    st.write(df[data_columns].head())  # Mostra as primeiras linhas das colunas de data

