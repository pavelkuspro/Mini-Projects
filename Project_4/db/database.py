import sqlite3

# cesta k databázi (je ve stejné složce jako tento soubor)
DB_PATH = "db/game.db"

def init_db():
    """Vytvoří databázi a tabulku users, pokud neexistují."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            highscore INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def get_user(username):
    """Vrátí uživatele podle jména, nebo None pokud neexistuje."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user


def create_user(username):
    """Vytvoří nového uživatele."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

def update_score(username, new_score):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Získáme původní skóre
    cursor.execute("SELECT highscore FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    old_score = result[0] if result else 0

    # Pokud nové skóre je lepší → aktualizujeme
    if new_score > old_score:
        cursor.execute("UPDATE users SET highscore = ? WHERE username = ?", (new_score, username))

    conn.commit()
    conn.close()

def get_top_players(limit=3):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username, highscore
        FROM users
        ORDER BY highscore DESC
        LIMIT ?
    """, (limit,))

    results = cursor.fetchall()
    conn.close()
    return results
