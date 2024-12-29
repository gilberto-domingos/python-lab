import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.customer_database import Database


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
            df_customers = pd.DataFrame(all_customers).drop(columns=["id"])
            df_customers.rename(columns={
                "cod_customer": "Código",
                "cell_customer": "Célula",
                "name_customer": "Nome",
                "email_customer": "Email",
                "phone_customer": "Telefone"
            }, inplace=True)
            return df_customers
        except Exception as e:
            st.error(f"Erro ao buscar clientes: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

    def show_customer_table(self, df_customers):
        """Exibe a tabela de clientes com formatação."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_customers.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def filter_customers(self, df_customers, filter_option, filter_value):
        """Filtra os clientes por código ou nome conforme a escolha do usuário."""
        if filter_option == "por Código":
            return df_customers[df_customers['Código'].str.contains(filter_value, na=False)]
        elif filter_option == "por Nome":
            return df_customers[df_customers['Nome'].str.contains(filter_value, case=False, na=False)]
        return df_customers

    def delete_customer(self, customer_id):
        """Deleta o cliente selecionado."""
        try:
            self.db.delete_customer(customer_id)
            st.success("Cliente deletado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao deletar cliente: {e}")

    def display_delete_confirmation(self, customer_name, customer_id):
        """Exibe uma confirmação de exclusão antes de deletar o cliente."""
        st.warning(f"Tem certeza que deseja deletar o cliente {
                   customer_name} (Código: {customer_id})?")
        if st.button("Deletar"):
            self.delete_customer(customer_id)

    def display_filtered_customers(self, filtered_customers):
        """Exibe os clientes filtrados e permite a seleção para exclusão."""
        if filtered_customers.empty:
            st.warning("Nenhum cliente encontrado com esse critério.")
        else:
            self.show_customer_table(filtered_customers)

            # Seleção para deletar
            delete_option = st.selectbox(
                "Escolha o cliente para deletar", filtered_customers['Código'].tolist())
            if delete_option:
                selected_customer = self.db.get_customer_by_cod(delete_option)
                if selected_customer:
                    self.display_delete_confirmation(
                        selected_customer['name_customer'], selected_customer['id'])


def show():
    css_path = Path("src/app/css/customer_read.css")
    db = Database()
    deleter = CustomerDeleter(db)
    deleter.load_css(css_path)

    st.subheader("Clientes - deletar")

    df_customers = deleter.get_customer_data()
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
        filtered_customers = deleter.filter_customers(
            df_customers, filter_option, filter_value)
        deleter.display_filtered_customers(filtered_customers)
    else:
        # Exibe a tabela sem filtro se nenhum valor for inserido
        deleter.show_customer_table(df_customers)


if __name__ == "__main__":
    show()
