import sqlite3
import os

DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "app.db")

# تأكد أن المجلد موجود
os.makedirs(DB_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

def create_tables():
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT,
        name TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        buyer_id INTEGER,
        car_model TEXT,
        part_name TEXT,
        description TEXT,
        status TEXT DEFAULT 'open'
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS offers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        request_id INTEGER,
        junkyard_id INTEGER,
        price REAL,
        note TEXT
    )
    """)

    conn.commit()
    
    def add_user(email, password, role, name):
    try:
        c.execute(
            "INSERT INTO users (email, password, role, name) VALUES (?, ?, ?, ?)",
            (email, password, role, name)
        )
        conn.commit()
        return True
    except:
        return False


def get_user(email, password):
    c.execute(
        "SELECT id, role, name FROM users WHERE email=? AND password=?",
        (email, password)
    )
    return c.fetchone()