# database.py

import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",    # Use "localhost" if the PostgreSQL container is on your machine
        port="5432",
        database="contabil",
        user="mmss",
        password="mmssmmnn"
    )
    return conn

def fetch_all_clients():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    conn.close()
    return clients

def insert_client(name, email, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO clients (name, email, phone) VALUES (%s, %s, %s) RETURNING id", (name, email, phone))
    conn.commit()
    client_id = cur.fetchone()[0]
    conn.close()
    return client_id

def update_client(client_id, name, email, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE clients SET name=%s, email=%s, phone=%s WHERE id=%s", (name, email, phone, client_id))
    conn.commit()
    conn.close()

def delete_client(client_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM clients WHERE id=%s", (client_id,))
    conn.commit()
    conn.close()
