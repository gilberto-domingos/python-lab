import pandas as pd
import os
import streamlit as st
from pathlib import Path


def show():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data/situationx.xlsx")

    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        st.error(f"Arquivo 'situationx.xlsx' não encontrado em {
                 file_path}. Verifique o caminho e tente novamente.")
        st.stop()

    summary = df.describe(include='all')

    summary = summary.drop(index='unique')
    summary = summary.drop(index='top')

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
    }).fillna('Nenhum')

    unique_celulas = df['Célula'].value_counts()
    unique_empresas = df['Empresa'].value_counts()

    report_df = pd.DataFrame({
        'Célula': unique_celulas.index,
        'Contagem de Célula': unique_celulas.values
    })

    report_empresas_df = pd.DataFrame({
        'Empresa': unique_empresas.index,
        'Contagem de Empresa': unique_empresas.values
    })

    data_dir = Path(current_dir) / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    output_report_path = data_dir / "relatorio_situationx.xlsx"

    with pd.ExcelWriter(output_report_path) as writer:
        translated_summary.to_excel(writer, sheet_name='Resumo Estatístico')
        report_df.to_excel(
            writer, sheet_name='Contagem de Células', index=False)
        report_empresas_df.to_excel(
            writer, sheet_name='Contagem de Empresas', index=False)

    st.subheader("Resumo Estatístico")
    st.dataframe(translated_summary)

    st.subheader("Contagem de Células")
    st.dataframe(report_df)

    st.subheader("Contagem de Empresas")
    st.dataframe(report_empresas_df)


show()
