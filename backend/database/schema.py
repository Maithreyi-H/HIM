from .database import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Memories table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        content TEXT,
        importance REAL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Relationship table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS relationship (
        user_id INTEGER PRIMARY KEY,
        trust REAL DEFAULT 0,
        affection REAL DEFAULT 0,
        comfort REAL DEFAULT 0,
        attachment REAL DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Conversation summaries
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversation_summary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database schema created successfully!")


if __name__ == "__main__":
    create_tables()