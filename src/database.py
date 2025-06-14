import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"

def create_tables():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS water_intake (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            intake_ml INTEGER,
            date TEXT
        )
        """
    )
    
    connection.commit()
    connection.close()
    
def log_intake(user_id, intake_ml):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    date_today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO water_intake (user_id, intake_ml, date) VALUES(?,?,?)", (user_id, intake_ml, date_today))
    connection.commit()
    connection.close()

def get_intake_history(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT intake_ml, date FROM water_inatke WHERE user_id = ?", (user_id,))
    records = cursor.fetchall()
    connection.close()
    return records

create_tables()

