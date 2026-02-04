import sqlite3

conn = sqlite3.connect("data/app.db", check_same_thread=False)
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
