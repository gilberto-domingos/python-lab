import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show(file_name="situationx.xlsx"):
    css_path = Path("src/app/css/apla.css")
    load_css(css_path)

    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(current_dir, '..', 'data', file_name)

        if not os.path.exists(data_path):
            raise FileNotFoundError

        df = pd.read_excel(data_path)

    except FileNotFoundError:
        st.error(f"Arquivo '{
                 file_name}' não encontrado. Verifique o caminho e tente novamente.")
        st.stop()

    df.columns = df.columns.str.strip()
    data_columns = df.columns[3:]

    st.subheader("Dados e informações")
    st.dataframe(df.head())

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

    st.subheader("Evolução Temporal")

    st.write("Dados nas colunas de data:")
    st.write(df[data_columns].head())
