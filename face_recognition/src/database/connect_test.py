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
                    dbname="contabil",            # Nome do banco de dados
                    user="mmss",                  # Usuário do banco
                    password="mmssmmnn",          # Senha do banco
                    host="186.250.185.87",        # IP público do servidor
                    port=5432                     # Porta do PostgreSQL exposta
                )
                print("Conexão com o banco de dados estabelecida.")
            except psycopg2.Error as e:
                self.conn = None
                print(f"Erro ao conectar ao banco de dados: {e}")


# Adicionando o código para executar a conexão
if __name__ == "__main__":
    db = Database()
    db.connect()
