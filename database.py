import sqlite3

DATABASE_FILE = 'mining_bot.db'

def create_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                    )''')

    # Create mining_records table
    cursor.execute('''CREATE TABLE IF NOT EXISTS mining_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        amount REAL NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')

    conn.commit()
    conn.close()

def add_user(username, password, role='user'):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                   (username, password, role))
    conn.commit()
    conn.close()

def get_user(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_mining_record(username, amount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mining_records (username, amount) VALUES (?, ?)",
                   (username, amount))
    conn.commit()
    conn.close()

def get_mining_records(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mining_records WHERE username = ?", (username,))
    records = cursor.fetchall()
    conn.close()
    return records
  
