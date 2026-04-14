import streamlit as st
import pandas as pd
import plotly.express as px
import os


def show():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            base_dir, '..', 'data', 'supermarket_sales.csv')  # Caminho correto

        if not os.path.exists(file_path):
            raise FileNotFoundError

        df = pd.read_csv(file_path, sep=",")

    except FileNotFoundError as e:
        st.error(
            "Arquivo não encontrado. Verifique se 'supermarket_sales.csv' está no diretório correto."
        )
        raise e

    df["Data"] = pd.to_datetime(
        df["Data"], format="%m/%d/%Y")  # Formato correto

    df["Month_Year"] = df["Data"].dt.strftime("%m/%Y")

    df["Classificação"] = df["Classificação"].str.replace(",", ".").astype(
        float)

    df["Total"] = df["Total"].str.replace(",", ".").astype(float)

    month = st.sidebar.selectbox("Mês", df["Month_Year"].unique())

    df_filtered = df[df["Month_Year"] == month]

    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)

    fig_date = px.bar(
        df_filtered, x="Data", y="Total", color="Cidade", title="Faturamento por dia"
    )
    col1.plotly_chart(fig_date, use_container_width=True)

    fig_prod = px.bar(
        df_filtered,
        x="Linha de produtos",
        y="Total",
        color="Cidade",
        title="Faturamento por produto",
        orientation="h",
    )
    col2.plotly_chart(fig_prod, use_container_width=True)

    city_total = df_filtered.groupby("Cidade")[["Total"]].sum().reset_index()

    total_faturamento = city_total["Total"].sum()

    if total_faturamento > 0:
        city_total["Porcentagem"] = (
            city_total["Total"] / total_faturamento) * 100
    else:
        city_total["Porcentagem"] = 0

    fig_city = px.bar(
        city_total, x="Cidade", y="Porcentagem", title="Faturamento por filial (%)"
    )
    col3.plotly_chart(fig_city, use_container_width=True)

    fig_kind = px.pie(
        df_filtered,
        values="Total",
        names="Pagamento",
        title="Faturamento por pagamento",
    )
    col4.plotly_chart(fig_kind, use_container_width=True)

    city_rating = df_filtered.groupby(
        "Cidade")[["Classificação"]].mean().reset_index()
    fig_rating = px.bar(
        city_rating, x="Cidade", y="Classificação", title="Avaliação"
    )
    col5.plotly_chart(fig_rating, use_container_width=True)


if __name__ == "__main__":
    show()
