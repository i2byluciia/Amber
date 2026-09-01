import sqlite3

DATABASE = "amber.db"

def init_database():
    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def remember(content):
    connection = sqlite3.connect(DATABASE)

    connection.execute(
        "INSERT INTO memories (content) VALUES (?)",
        (content,)
    )

    connection.commit()
    connection.close()

def recall():
    connection = sqlite3.connect(DATABASE)

    memories = connection.execute(
        "SELECT id, content, created_at FROM memories"
    ).fetchall()

    connection.close()

    return memories