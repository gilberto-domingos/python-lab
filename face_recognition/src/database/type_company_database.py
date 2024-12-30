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

    def insert_employee(self, cod_employee, name_employee, email_employee, phone_employee):
        """Insere um novo funcionário no banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO employees (cod_employee, name_employee, email_employee, phone_employee)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
                """,
                (cod_employee, name_employee, email_employee, phone_employee)
            )
            self.conn.commit()
            return cur.fetchone()[0]  # Retorna o ID do funcionário inserido
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(f"Erro ao salvar no banco de dados: {e}")

    # Método para inserir tipo de empresa
    def insert_type_company(self, cod_company, descr_company):
        """Insere um novo tipo de empresa no banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO type_companies (cod_company, descr_company)
                VALUES (%s, %s)
                RETURNING id;
                """,
                (cod_company, descr_company)
            )
            self.conn.commit()
            # Retorna o ID do tipo de empresa inserido
            return cur.fetchone()[0]
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(f"Erro ao salvar no banco de dados: {e}")

    def get_employee(self, id):
        """Obtém um funcionário pelo ID."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM employees WHERE id = %s",
                (id,)
            )
            return cur.fetchone()  # Retorna os dados do funcionário ou None
        except psycopg2.Error as e:
            raise Exception(
                f"Erro ao buscar funcionário no banco de dados: {e}")

    def update_employee(self, id, cod_employee, name_employee, email_employee, phone_employee):
        """Atualiza os dados de um funcionário."""
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                UPDATE employees
                SET cod_employee = %s, name_employee = %s, email_employee = %s, phone_employee = %s
                WHERE id = %s;
                """,
                (cod_employee, name_employee,
                 email_employee, phone_employee, id)
            )
            self.conn.commit()
            return cur.rowcount  # Retorna o número de linhas afetadas
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(
                f"Erro ao atualizar funcionário no banco de dados: {e}")

    def delete_employee(self, id):
        """Exclui um funcionário pelo ID."""
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                "DELETE FROM employees WHERE id = %s",
                (id,)
            )
            self.conn.commit()
            return cur.rowcount  # Retorna o número de linhas afetadas
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(
                f"Erro ao excluir funcionário no banco de dados: {e}")

    def get_all_employees(self):
        """Obtém todos os funcionários do banco de dados."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("SELECT * FROM employees")
            return cur.fetchall()  # Retorna todos os funcionários
        except psycopg2.Error as e:
            raise Exception(
                f"Erro ao buscar todos os funcionários no banco de dados: {e}")

    def get_employee_by_cod(self, cod_employee):
        """Obtém um funcionário pelo código."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM employees WHERE cod_employee = %s",
                (cod_employee,)
            )
            return cur.fetchone()  # Retorna os dados do funcionário ou None
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar funcionário pelo código: {e}")

    def get_employee_by_name(self, name_employee):
        """Obtém funcionários pelo nome (parcial)."""
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM employees WHERE name_employee ILIKE %s",
                (f"%{name_employee}%",)
            )
            return cur.fetchall()  # Retorna todos os funcionários encontrados
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar funcionários pelo nome: {e}")
