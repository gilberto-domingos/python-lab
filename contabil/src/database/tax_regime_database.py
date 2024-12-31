import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
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
        if self.conn is None or self.conn.closed:
            self.connect()
        if self.conn is None or self.conn.closed:
            raise Exception(
                "Falha ao estabelecer conexão com o banco de dados.")

    def insert_tax_regime(self, cod_tax_regime, descr_tax_regime):
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO tax_regimes (cod_tax_regime, descr_tax_regime)
                VALUES (%s, %s)
                RETURNING id;
                """,
                (cod_tax_regime, descr_tax_regime)
            )
            self.conn.commit()
            return cur.fetchone()[0]
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(f"Erro ao salvar no banco de dados: {e}")

    def get_tax_regime(self, id):
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM tax_regimes WHERE id = %s",
                (id,)
            )
            return cur.fetchone()
        except psycopg2.Error as e:
            raise Exception(
                f"Erro ao buscar regime tributário no banco de dados: {e}")

    def update_tax_regime(self, id, cod_tax_regime, descr_tax_regime):
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                UPDATE tax_regimes
                SET cod_tax_regime = %s, descr_tax_regime = %s
                WHERE id = %s;
                """,
                (cod_tax_regime, descr_tax_regime, id)
            )
            self.conn.commit()
            return cur.rowcount
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(
                f"Erro ao atualizar regime tributário no banco de dados: {e}")

    def delete_tax_regime(self, id):
        self.ensure_connection()
        cur = self.conn.cursor()
        try:
            cur.execute(
                "DELETE FROM tax_regimes WHERE id = %s",
                (id,)
            )
            self.conn.commit()
            return cur.rowcount
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(
                f"Erro ao excluir regime tributário no banco de dados: {e}")

    def get_all_tax_regimes(self):
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("SELECT * FROM tax_regimes")
            return cur.fetchall()
        except psycopg2.Error as e:
            raise Exception(
                f"Erro ao buscar todos os regimes tributários no banco de dados: {e}")

    def get_tax_regime_by_cod(self, cod_tax_regime):
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM tax_regimes WHERE cod_tax_regime = %s",
                (cod_tax_regime,)
            )
            return cur.fetchone()
        except psycopg2.Error as e:
            raise Exception(
                f"Erro ao buscar regime tributário pelo código: {e}")

    def get_tax_regime_by_descr(self, descr_tax_regime):
        self.ensure_connection()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                "SELECT * FROM tax_regimes WHERE descr_tax_regime ILIKE %s",
                (f"%{descr_tax_regime}%",)
            )
            return cur.fetchall()
        except psycopg2.Error as e:
            raise Exception(
                f"Erro ao buscar regimes tributários pela descrição: {e}")
