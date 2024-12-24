import psycopg2
from psycopg2.extras import RealDictCursor
from src.app.models.client_model import Client
from src.config.config_database import Database


class Database:
    def __init__(self):
        self.conn = None

    def ensure_connection(self):
        """Garante que a conexão está ativa, tentando reconectar se necessário."""
        if self.conn is None or self.conn.closed:
            self.connect()
        if self.conn is None or self.conn.closed:
            raise Exception(
                "Falha ao estabelecer conexão com o banco de dados.")

    def fetch_all_clients(self):
        """Busca todos os clientes no banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM clients")
        clients_data = cur.fetchall()
        clients = []
        for client_data in clients_data:
            client = Client(
                id_client=client_data['id'],
                cod_client=client_data['cod_client'],
                name_client=client_data['name'],
                cell_client=client_data['cell'],
                email_client=client_data['email'],
                phone_client=client_data['phone']
            )
            clients.append(client)
        return clients

    def insert_client(self, Client: Client):
        """Insere um novo cliente no banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO clients (cod_client, name, email, phone, cell) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (Client.cod_client, Client.name_client, Client.email_client,
             Client.phone_client, Client.cell_client)
        )
        self.conn.commit()
        # Atribui o ID retornado ao cliente
        Client.id_client = cur.fetchone()[0]
        return Client.id_client

    def update_client(self, Client: Client):
        """Atualiza as informações de um cliente."""
        self.ensure_connection()
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE clients SET cod_client=%s, name=%s, email=%s, phone=%s, cell=%s WHERE id=%s",
            (Client.cod_client, Client.name_client, Client.email_client,
             Client.phone_client, Client.cell_client, Client.id_client)
        )
        self.conn.commit()

    def delete_client(self, client_id):
        """Exclui um cliente do banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor()
        cur.execute("DELETE FROM clients WHERE id=%s", (client_id,))
        self.conn.commit()


if __name__ == "__main__":
    db = Database()
    try:
        db.ensure_connection()
        print("O banco está conectado e operacional.")
    except Exception as e:
        print(f"Erro: {e}")
