import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"

def create_tables():
    """Create necessary database tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_intake (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            intake_ml INTEGER,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_intake(user_id, intake_ml):
    """Log user's water intake."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    date_today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO water_intake (user_id, intake_ml, date) VALUES (?, ?, ?)", (user_id, intake_ml, date_today))
    conn.commit()
    conn.close()

def get_intake_history(user_id):
    """Retrieve intake history for a user."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT intake_ml, date FROM water_intake WHERE user_id = ?", (user_id,))
    records = cursor.fetchall()
    conn.close()
    return records

# Initialize database
create_tables()
