import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.customer_database import Database
from src.app.models.customer_model import Customer


class CustomerDeleter:
    def __init__(self, db):
        """Inicializa o deletador de clientes com a injeção de dependência do banco de dados."""
        self.db = db

    def load_css(self, file_path):
        """Carrega o arquivo CSS no Streamlit."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def get_customer_data(self):
        """Obtém todos os clientes do banco de dados e formata para exibição."""
        try:
            all_customers = self.db.get_all_customers()
            customers = [
                Customer(
                    id=customer["id"],
                    cod_customer=customer["cod_customer"],
                    cell_customer=customer["cell_customer"],
                    name_customer=customer["name_customer"],
                    email_customer=customer["email_customer"],
                    phone_customer=customer["phone_customer"]
                )
                for customer in all_customers
            ]

            data = [{
                "Código": customer.get_cod_customer(),
                "Célula": customer.get_cell_customer(),
                "Nome": customer.get_name_customer(),
                "Email": customer.get_email_customer(),
                "Telefone": customer.get_phone_customer()
            } for customer in customers]

            return pd.DataFrame(data)
        except Exception as e:
            st.error(f"Erro ao buscar clientes: {e}")
            return pd.DataFrame()

    def show_customer_table(self, df_customers):
        """Exibe a tabela de clientes com formatação."""
        styled_df = df_customers.style.set_table_styles([
            dict(selector='th', props=[('text-align', 'center')]),
            dict(selector='td', props=[('text-align', 'center')])
        ]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_customers(self, df_customers, filter_option, filter_value):
        """Filtra os clientes por código ou nome conforme a escolha do usuário."""
        try:
            if filter_option == "por Código":
                return df_customers[df_customers['Código'].str.contains(filter_value, na=False)]
            elif filter_option == "por Nome":
                return df_customers[df_customers['Nome'].str.contains(filter_value, case=False, na=False)]
        except Exception as e:
            st.error(f"Erro ao filtrar clientes: {e}")
        return pd.DataFrame()

    def delete_customer(self, customer_id, cod_customer):
        """Deleta o cliente selecionado."""
        try:
            if self.db.delete_customer(customer_id):
                st.success(f"Cliente com Código '{
                           cod_customer}' deletado com sucesso!")
            else:
                st.error("Cliente não encontrado ou não foi possível deletar.")
        except Exception as e:
            st.error(f"Erro ao deletar cliente: {e}")

    def display_delete_confirmation(self, customer_id, cod_customer, name_customer):
        """Exibe uma confirmação de exclusão antes de deletar o cliente."""
        st.warning(f"Tem certeza que deseja deletar o cliente '{
                   name_customer}' (Código: {cod_customer})?")
        if st.button("Deletar"):
            self.delete_customer(customer_id, cod_customer)

    def display_filtered_customers(self, filtered_customers):
        """Exibe os clientes filtrados e permite a seleção para exclusão."""
        if filtered_customers.empty:
            st.warning("Nenhum cliente encontrado com esse critério.")
        else:
            self.show_customer_table(filtered_customers)

            selected_code = st.selectbox(
                "Escolha o cliente para deletar", filtered_customers['Código'].tolist(
                )
            )
            if selected_code:
                selected_customer_data = self.db.get_customer_by_cod(
                    selected_code)
                if selected_customer_data:
                    name_customer = selected_customer_data.get(
                        "name_customer", "Desconhecido")
                    cod_customer = selected_customer_data.get(
                        "cod_customer")
                    customer_id = selected_customer_data.get("id")
                    self.display_delete_confirmation(
                        customer_id, cod_customer, name_customer)


def show():
    css_path = Path("src/app/css/customer_read.css")
    db = Database()
    deleter = CustomerDeleter(db)
    deleter.load_css(css_path)

    st.subheader("Clientes - Deletar")

    df_customers = deleter.get_customer_data()
    if df_customers.empty:
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome")
    )

    filter_value = st_keyup("Digite o valor para filtrar:", key="filter_value")

    if filter_value:
        filtered_customers = deleter.filter_customers(
            df_customers, filter_option, filter_value)
        deleter.display_filtered_customers(filtered_customers)
    else:
        deleter.show_customer_table(df_customers)


if __name__ == "__main__":
    show()
