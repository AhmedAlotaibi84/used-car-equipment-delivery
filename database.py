import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/app.db", check_same_thread=False)
c = conn.cursor()

def create_tables():
    c.execute("""
        CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car TEXT,
            year TEXT,
            part TEXT,
            price TEXT,
            note TEXT,
            image BLOB
        )
    """)
    conn.commit()

def add_part(car, year, part, price, note, image):
    c.execute("""
        INSERT INTO parts (car, year, part, price, note, image)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (car, year, part, price, note, image))
    conn.commit()

def get_parts():
    c.execute("SELECT * FROM parts ORDER BY id DESC")
    return c.fetchall()
