import sqlite3

DATABASE = "amber.db"

def init_database():
    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS context_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS persistent_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            importance INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS system_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def remember_persistent(content, importance=5):
    connection = sqlite3.connect(DATABASE)

    connection.execute(
        """
        INSERT INTO persistent_memory (content, importance)
        VALUES (?, ?)
        """,
        (content, importance)
    )

    connection.commit()
    connection.close()

def recall_persistent():
    connection = sqlite3.connect(DATABASE)

    memories = connection.execute(
        """
        SELECT id, content, importance, created_at, updated_at
        FROM persistent_memory
        ORDER BY importance DESC
        """
    ).fetchall()

    connection.close()

    return memories

def set_preference(key, value):
    connection = sqlite3.connect(DATABASE)

    connection.execute(
        """
        INSERT INTO preferences (key, value)
        VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET
            value = excluded.value,
            updated_at = CURRENT_TIMESTAMP
        """,
        (key, value)
    )

    connection.commit()
    connection.close()

def get_preference(key):
    connection = sqlite3.connect(DATABASE)

    preference = connection.execute(
        """
        SELECT value
        FROM preferences
        WHERE key = ?
        """,
        (key,)
    ).fetchone()

    connection.close()

    if preference:
        return preference[0]

    return None