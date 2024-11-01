import streamlit as st
import pandas as pd 
from src.database import fetch_all_clients, insert_client, update_client, delete_client

def show():
    # Streamlit app title
    st.title("Cadastro")
    
    # select
    options = ["Adicionar", "Consultar", "Editar", "Deletar"]
    choice = st.selectbox("Selecione a opção", options)

    # Add Client
    if choice == "Adicionar":
        st.subheader("Adicione um novo cliente:")
        name = st.text_input("Nome")
        email = st.text_input("Email")
        phone = st.text_input("Telefone")

        if st.button("Adicionar"):
            if name and email and phone:
                insert_client(name, email, phone)
                st.success("Cliente adicionado com sucesso!")
            else:
                st.error("Por favor preencha todos os campos.")

    # View Clients
    elif choice == "Consultar":
        st.subheader("Lista dos clientes")
        clients = fetch_all_clients()
        
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
            st.write("Cliente não encontrado.")

    # Edit Client
    elif choice == "Editar":
        st.subheader("Editar dados do cliente:")
        clients = fetch_all_clients()
        client_ids = [client["id"] for client in clients]
        selected_client = st.selectbox("Selecione o cliente", client_ids)

        if selected_client:
            client_data = next(client for client in clients if client["id"] == selected_client)
            name = st.text_input("Nome", client_data["name"])
            email = st.text_input("Email", client_data["email"])
            phone = st.text_input("Telefone", client_data["phone"])

            if st.button("Atualizar"):
                update_client(selected_client, name, email, phone)
                st.success("Cliente atualizado com sucesso!")

    # Delete Client
    elif choice == "Deletar":
        st.subheader("Deletar cliente")
        clients = fetch_all_clients()
        client_ids = [client["id"] for client in clients]
        selected_client = st.selectbox("Selecione o cliente", client_ids)

        if selected_client:
            if st.button("Deletar"):
                delete_client(selected_client)
                st.success("Cliente deletado com sucesso!")

        # Mostrar lista dos clientes atualizada
        st.subheader("Lista dos clientes")
        clients = fetch_all_clients()
        
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
            st.write("Cliente não encontrado.")
