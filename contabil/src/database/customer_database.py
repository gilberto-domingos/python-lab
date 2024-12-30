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
                raise Exception(f"Erro ao conectar ao banco de dados: {e}")

    def ensure_connection(self):
        """Garante que a conexão está ativa, tentando reconectar se necessário."""
        if self.conn is None or self.conn.closed:
            self.connect()
        if self.conn is None or self.conn.closed:
            raise Exception(
                "Falha ao estabelecer conexão com o banco de dados.")

    def insert_customer(self, cod_customer, name_customer, cell_customer, email_customer, phone_customer):
        """Insere um novo cliente no banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO customers (cod_customer, name_customer, cell_customer, email_customer, phone_customer)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """,
                (cod_customer, name_customer, cell_customer,
                 email_customer, phone_customer)
            )
            self.conn.commit()
            return cur.fetchone()[0]  # Retorna o ID do cliente inserido
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(f"Erro ao salvar no banco de dados: {e}")

    def get_customer(self, id):
        """Obtém um cliente pelo ID."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM customers WHERE id = %s",
                (id,)
            )
            return cur.fetchone()  # Retorna os dados do cliente ou None
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar cliente no banco de dados: {e}")

    def update_customer(self, id, cod_customer, name_customer, cell_customer, email_customer, phone_customer):
        """Atualiza os dados de um cliente."""
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                UPDATE customers
                SET cod_customer = %s, name_customer = %s, cell_customer = %s, email_customer = %s, phone_customer = %s
                WHERE id = %s;
                """,
                (cod_customer, name_customer, cell_customer,
                 email_customer, phone_customer, id)
            )
            self.conn.commit()
            return cur.rowcount  # Retorna o número de linhas afetadas
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(
                f"Erro ao atualizar cliente no banco de dados: {e}")

    def delete_customer(self, id):
        """Exclui um cliente pelo ID."""
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                "DELETE FROM customers WHERE id = %s",
                (id,)
            )
            self.conn.commit()
            return cur.rowcount  # Retorna o número de linhas afetadas
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(f"Erro ao excluir cliente no banco de dados: {e}")

    def get_all_customers(self):
        """Obtém todos os customers do banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("SELECT * FROM customers")
            return cur.fetchall()  # Retorna todos os customers
        except psycopg2.Error as e:
            raise Exception(
                f"Erro ao buscar todos os customers no banco de dados: {e}")

    def get_customer_by_cod(self, cod_customer):
        """Obtém um cliente pelo código."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM customers WHERE cod_customer = %s",
                (cod_customer,)
            )
            return cur.fetchone()  # Retorna os dados do cliente ou None
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar cliente pelo código: {e}")

    def get_customer_by_name(self, name_customer):
        """Obtém customers pelo nome (parcial)."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM customers WHERE name_customer ILIKE %s",
                (f"%{name_customer}%",)
            )
            return cur.fetchall()  # Retorna todos os customers encontrados
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar customers pelo nome: {e}")
