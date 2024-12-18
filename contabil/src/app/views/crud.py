import streamlit as st
import pandas as pd
import os
import sys


src_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..', 'src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from src.database.database import Database
except ImportError as e:
    print(f"Error importing database module: {e}")
    print(f"sys.path: {sys.path}")
    sys.exit(1)


db = Database()


def show():
    st.title("Cadastro")

    options = ["Adicionar", "Consultar", "Editar", "Deletar"]
    choice = st.selectbox("Escolha a opção:", options)

    if choice == "Adicionar":
        st.subheader("Adicione um novo cliente:")
        name = st.text_input("Nome")
        email = st.text_input("Email")
        phone = st.text_input("Telefone")

        if st.button("Adicionar"):
            if name and email and phone:
                try:
                    db.insert_client(name, email, phone)
                    st.success("Cliente adicionado com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao adicionar cliente: {e}")
            else:
                st.error("Por favor, preencha todos os campos.")

    # Consultar clientes
    elif choice == "Consultar":
        st.subheader("Lista dos clientes")
        try:
            clients = db.fetch_all_clients()
            if clients:
                # Renomear as colunas para português
                clients_df = pd.DataFrame(clients)
                clients_df = clients_df.rename(columns={
                    "id": "ID",
                    "name": "Nome",
                    "email": "Email",
                    "phone": "Telefone"
                })
                st.table(clients_df)
            else:
                st.write("Nenhum cliente encontrado.")
        except Exception as e:
            st.error(f"Erro ao buscar clientes: {e}")

    # Editar cliente
    elif choice == "Editar":
        st.subheader("Editar dados do cliente:")
        try:
            clients = db.fetch_all_clients()
            client_ids = [client["id"] for client in clients]
            selected_client = st.selectbox("Escolha o cliente:", client_ids)

            if selected_client:
                client_data = next(
                    client for client in clients if client["id"] == selected_client)
                name = st.text_input("Nome", client_data["name"])
                email = st.text_input("Email", client_data["email"])
                phone = st.text_input("Telefone", client_data["phone"])

                if st.button("Atualizar"):
                    db.update_client(selected_client, name, email, phone)
                    st.success("Cliente atualizado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao editar cliente: {e}")

    # Deletar cliente
    elif choice == "Deletar":
        st.subheader("Deletar cliente")
        try:
            clients = db.fetch_all_clients()
            client_ids = [client["id"] for client in clients]
            selected_client = st.selectbox("Selecione o cliente:", client_ids)

            if selected_client:
                if st.button("Deletar"):
                    db.delete_client(selected_client)
                    st.success("Cliente deletado com sucesso!")

            # Mostrar lista dos clientes atualizada
            st.subheader("Lista dos clientes")
            clients = db.fetch_all_clients()
            if clients:
                clients_df = pd.DataFrame(clients)
                clients_df = clients_df.rename(columns={
                    "id": "ID",
                    "name": "Nome",
                    "email": "Email",
                    "phone": "Telefone"
                })
                st.table(clients_df)
            else:
                st.write("Nenhum cliente encontrado.")
        except Exception as e:
            st.error(f"Erro ao deletar cliente: {e}")
