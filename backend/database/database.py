import sqlite3
from pathlib import Path

# Path to memory.db (same folder as this file)
DB_PATH = Path(__file__).parent / "memory.db"


def get_connection():
    """
    Create and return a connection to the SQLite database.
    If the database doesn't exist, SQLite creates it automatically.
    """
    conn = sqlite3.connect(DB_PATH)
    return conn