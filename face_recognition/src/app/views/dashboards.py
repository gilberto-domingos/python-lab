import streamlit as st
import pandas as pd
import plotly.express as px


def show():
    # Carregar o conjunto de dados
    try:
        df = pd.read_csv(
            "./data/supermarket_sales.csv", sep=","
        )  # Ajuste o caminho se necessário
    except FileNotFoundError as e:
        st.error(
            "Arquivo não encontrado. Verifique se 'supermarket_sales.csv' está no diretório correto."
        )
        raise e  # Relevanta a exceção após registrar

    # Converter a coluna 'Data' para datetime
    df["Data"] = pd.to_datetime(df["Data"], format="%m/%d/%Y")  # Formato correto

    # Extrair mês e ano no formato mm/yyyy
    df["Month_Year"] = df["Data"].dt.strftime("%m/%Y")  # Formato mm/yyyy

    # Tratar a coluna 'Classificação' para garantir que seja numérica
    df["Classificação"] = (
        df["Classificação"].str.replace(",", ".").astype(float)
    )  # Substituir vírgulas por pontos e converter para float

    # Tratar a coluna 'Total' para garantir que seja numérica
    df["Total"] = (
        df["Total"].str.replace(",", ".").astype(float)
    )  # Substituir vírgulas por pontos e converter para float

    # Filtrar opções de mês para seleção
    month = st.sidebar.selectbox("Mês", df["Month_Year"].unique())

    # Filtrar o dataframe com base no mês selecionado
    df_filtered = df[df["Month_Year"] == month]

    # Criar colunas para layout
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)

    # Plotando receita por dia
    fig_date = px.bar(
        df_filtered, x="Data", y="Total", color="Cidade", title="Faturamento por dia"
    )
    col1.plotly_chart(fig_date, use_container_width=True)

    # Plotando receita por linha de produto
    fig_prod = px.bar(
        df_filtered,
        x="Linha de produtos",
        y="Total",
        color="Cidade",
        title="Faturamento por produto",
        orientation="h",
    )
    col2.plotly_chart(fig_prod, use_container_width=True)

    # Receita total por cidade em porcentagem
    city_total = df_filtered.groupby("Cidade")[["Total"]].sum().reset_index()

    # Calcular a porcentagem do faturamento total  aContabil/.venv/bin
    total_faturamento = city_total["Total"].sum()

    if (
        total_faturamento > 0
    ):  # Verifica se o total não é zero para evitar divisão por zero
        city_total["Porcentagem"] = (city_total["Total"] / total_faturamento) * 100
    else:
        city_total["Porcentagem"] = (
            0  # Se o total for zero, define a porcentagem como zero
        )

    fig_city = px.bar(
        city_total, x="Cidade", y="Porcentagem", title="Faturamento por filial (%)"
    )
    col3.plotly_chart(fig_city, use_container_width=True)

    # Receita por tipo de pagamento (corrigido para usar 'Pagamento')
    fig_kind = px.pie(
        df_filtered,
        values="Total",
        names="Pagamento",
        title="Faturamento por pagamento",
    )
    col4.plotly_chart(fig_kind, use_container_width=True)

    # Avaliação média por cidade (alterado para "Classificação")
    city_rating = (
        df_filtered.groupby("Cidade")[["Classificação"]].mean().reset_index()
    )  # Usar "Classificação"
    fig_rating = px.bar(
        city_rating, x="Cidade", y="Classificação", title="Avaliação"
    )  # Alterado para "Avaliação"
    col5.plotly_chart(fig_rating, use_container_width=True)


# Chamar a função show para executar o código
if __name__ == "__main__":
    show()
