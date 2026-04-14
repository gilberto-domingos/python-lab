import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.customer_database import Database
from src.app.models.customer_model import Customer


class CustomerReader:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_customer_data(self):
        try:
            all_customers = self.db.get_all_customers()
            customers = [Customer(
                customer['cod_customer'],
                customer['name_customer'],
                customer['cell_customer'],
                customer['email_customer'],
                customer['phone_customer']
            ) for customer in all_customers]

            df_customers = pd.DataFrame([{
                'Código': cust.cod_customer,
                'Nome': cust.name_customer,
                'Célula': cust.cell_customer,
                'Email': cust.email_customer,
                'Telefone': cust.phone_customer
            } for cust in customers])

            return df_customers
        except Exception as e:
            st.error(f"Erro ao buscar clientes: {e}")
            return pd.DataFrame()

    def show_customer_table(self, df_customers):
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_customers.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_customers(self, df_customers, filter_option, filter_value):
        if filter_option == "por Código":
            return df_customers[df_customers['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Nome":
            return df_customers[df_customers['Nome'].str.contains(filter_value, case=False, na=False)]
        return df_customers

    def display_filtered_customers(self, filtered_customers):
        if filtered_customers.empty:
            st.warning("Nenhum cliente encontrado com esse critério.")
        else:
            self.show_customer_table(filtered_customers)


def show():
    css_path = Path("src/app/css/customer_read.css")
    db = Database()
    reader = CustomerReader(db)
    reader.load_css(css_path)

    st.subheader("Clientes - consultar")

    df_customers = reader.get_customer_data()
    if df_customers.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if filter_option == "por Código":
        filter_value = st_keyup(
            "Digite o código do cliente:", key="filter_cod")
    else:
        filter_value = st_keyup(
            "Digite o nome do cliente:", key="filter_name")

    if filter_value:
        filtered_customers = reader.filter_customers(
            df_customers, filter_option, filter_value)
        reader.display_filtered_customers(filtered_customers)
    else:
        reader.show_customer_table(df_customers)


if __name__ == "__main__":
    show()
