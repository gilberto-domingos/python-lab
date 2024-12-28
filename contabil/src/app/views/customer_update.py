import streamlit as st
import pandas as pd
from pathlib import Path
from st_keyup import st_keyup
from src.database.customer_database import Database
from src.app.models.customer_model import Customer
from src.app.utils.validate import validate_cod, validate_email_address, validate_brazilian_phone


class CustomerEditor:
    def __init__(self, db):
        self.db = db

    def load_css(self, file_path):
        """Carrega e aplica o CSS da página."""
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def show_customer_table(self, df_customers):
        """Exibe a tabela de clientes com formatação e centralização."""
        s1 = dict(selector='th', props=[('text-align', 'center')])
        s2 = dict(selector='td', props=[('text-align', 'center')])
        styled_df = df_customers.style.set_table_styles([s1, s2]).hide(axis=0)
        st.markdown('<div style="display: flex; justify-content: center;">' +
                    styled_df.to_html() + '</div>', unsafe_allow_html=True)

    def edit_customer(self, customer):
        """Permite editar um cliente existente."""
        new_cod = st.text_input(
            "Novo Código", value=customer.get_cod_customer(), max_chars=5)
        new_name = st.text_input(
            "Novo Nome", value=customer.get_name_customer(), max_chars=50)
        new_cell = st.text_input(
            "Nova Célula", value=customer.get_cell_customer(), max_chars=50)
        new_email = st.text_input(
            "Novo Email", value=customer.get_email_customer(), max_chars=50)
        new_phone = st.text_input(
            "Novo Telefone", value=customer.get_phone_customer(), max_chars=15)

        # Validação do Código
        cod_valid = True
        if new_cod and not validate_cod(new_cod):
            st.error("O Código deve conter exatamente 5 números.")
            cod_valid = False

        # Validação do Email
        email_valid = True
        if new_email and not validate_email_address(new_email):
            st.error("Email inválido.")
            email_valid = False

        # Validação do Telefone
        phone_valid = True
        phone_validation_result = validate_brazilian_phone(new_phone)
        if new_phone and not phone_validation_result[0]:
            st.error(f"Erro no Telefone: {phone_validation_result[1]}")
            phone_valid = False

        if st.button("Salvar Alterações") and cod_valid and email_valid and phone_valid:
            try:
                self.db.update_customer(
                    customer.id, new_cod, new_name, new_cell, new_email, new_phone)
                st.success("Cliente atualizado com sucesso!")
                return new_cod, new_name, new_cell, new_email, new_phone
            except Exception as e:
                st.error(f"Erro ao atualizar cliente: {e}")
        return None


def show():
    """Função principal para exibir a tela de edição de clientes."""
    css_path = Path("src/app/css/customer_update.css")
    editor = CustomerEditor(Database())
    editor.load_css(css_path)

    st.subheader("Clientes - Editar")

    try:
        all_customers = editor.db.get_all_customers()
        df_customers = pd.DataFrame(
            all_customers).drop(columns=["id"])
        df_customers.rename(columns={
            "cod_customer": "Código",
            "name_customer": "Nome",
            "cell_customer": "Célula",
            "email_customer": "Email",
            "phone_customer": "Telefone"
        }, inplace=True)
    except Exception as e:
        st.error(f"Erro ao buscar clientes: {e}")
        return

    filter_option = st.selectbox(
        "Escolha a forma de filtragem:", ("por Código", "por Nome"))

    if 'filtered_customers' not in st.session_state:
        st.session_state['filtered_customers'] = df_customers

    filtered_customers = st.session_state['filtered_customers']

    if filter_option == "por Código":
        cod_customer = st_keyup(
            "Digite o código do cliente:", key="filter_cod")
        if cod_customer:
            filtered_customers = df_customers[df_customers['Código'].str.contains(
                cod_customer, na=False)]
            if filtered_customers.empty:
                st.warning("Nenhum cliente encontrado com esse código.")
        st.session_state['filtered_customers'] = filtered_customers

    elif filter_option == "por Nome":
        name_customer = st_keyup(
            "Digite o nome do cliente:", key="filter_name")
        if name_customer:
            filtered_customers = df_customers[df_customers['Nome'].str.contains(
                name_customer, case=False, na=False)]
            if filtered_customers.empty:
                st.warning("Nenhum cliente encontrado com esse nome.")
        st.session_state['filtered_customers'] = filtered_customers

    # Exibe a tabela e a opção de edição
    if not filtered_customers.empty:
        editor.show_customer_table(filtered_customers)

        # Seleciona o primeiro cliente automaticamente
        selected_customer_data = filtered_customers.iloc[0]
        selected_customer = editor.db.get_customer_by_cod(
            selected_customer_data['Código'])

        customer = Customer(selected_customer['cod_customer'],
                            selected_customer['cell_customer'],
                            selected_customer['name_customer'],
                            selected_customer['email_customer'],
                            selected_customer['phone_customer'],
                            selected_customer['id'])

        updated_values = editor.edit_customer(customer)

        if updated_values:
            # Atualiza a linha da tabela diretamente com os novos dados
            filtered_customers.loc[filtered_customers['Código'] == selected_customer_data['Código'], [
                'Nome', 'Célula', 'Email', 'Telefone']] = updated_values[1], updated_values[2], updated_values[3], updated_values[4]
            # Atualiza o estado com os dados modificados
            st.session_state['filtered_customers'] = filtered_customers
            # Reexibe a tabela com os dados atualizados
            editor.show_customer_table(filtered_customers)


if __name__ == "__main__":
    show()
