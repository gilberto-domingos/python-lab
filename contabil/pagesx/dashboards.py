import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    # Carregar o arquivo CSV
    df = pd.read_csv("./data/supermarket_sales.csv", sep=";", decimal=",")  # Verifique se o delimitador está correto
    print(df.columns)  # Para verificar quais colunas foram lidas

    # Tentar converter a coluna 'Date'
    try:
        df["Date"] = pd.to_datetime(df["Date"])
    except KeyError:
        print("Coluna 'Date' não encontrada. As colunas disponíveis são:", df.columns)
        return  # Ou lance uma exceção

    df = df.sort_values("Date")

    # Mudar os nomes das cidades
    df["City"] = df["City"].replace({"Yangon": "Brusque", "Naypyitaw": "Balneário", "Mandalay": "Blumenau"})

    df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
    month = st.sidebar.selectbox("Mês", df["Month"].unique())

    df_filtered = df[df["Month"] == month]

    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)

    fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
    col1.plotly_chart(fig_date, use_container_width=True)

    fig_prod = px.bar(df_filtered, x="Date", y="Product line",
                      color="City", title="Faturamento por tipo de produto",
                      orientation="h")
    col2.plotly_chart(fig_prod, use_container_width=True)

    city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
    fig_city = px.bar(city_total, x="City", y="Total",
                       title="Faturamento por filial")
    col3.plotly_chart(fig_city, use_container_width=True)

    fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                       title="Faturamento por tipo de pagamento")
    col4.plotly_chart(fig_kind, use_container_width=True)

    city_total_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
    fig_rating = px.bar(city_total_rating, x="City", y="Rating",
                         title="Avaliação")
    col5.plotly_chart(fig_rating, use_container_width=True)

# Chame a função show() no seu módulo principal (main.py)