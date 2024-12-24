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
                    host="186.250.185.87",
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
