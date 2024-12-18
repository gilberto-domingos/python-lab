# database.py

import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        """Estabelece conexão com o banco de dados se não estiver conectado."""
        if self.conn is None or self.conn.closed:
            try:
                self.conn = psycopg2.connect(
                    dbname="contabil",
                    user="mmss",
                    password="mmssmmnn",
                    host="application-database",
                    port=5432
                )
                print("Conexão com o banco de dados estabelecida.")
            except psycopg2.Error as e:
                self.conn = None
                print(f"Erro ao conectar ao banco de dados: {e}")

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
        return cur.fetchall()

    def insert_client(self, name, email, phone):
        """Insere um novo cliente no banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO clients (name, email, phone) VALUES (%s, %s, %s) RETURNING id",
            (name, email, phone)
        )
        self.conn.commit()
        return cur.fetchone()[0]

    def update_client(self, client_id, name, email, phone):
        """Atualiza as informações de um cliente."""
        self.ensure_connection()
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE clients SET name=%s, email=%s, phone=%s WHERE id=%s",
            (name, email, phone, client_id)
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
