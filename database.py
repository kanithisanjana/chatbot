import sqlite3

DB_NAME = "chatbot.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_chat(user_msg, bot_reply):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_logs(user_message, bot_response)
    VALUES (?,?)
    """, (user_msg, bot_reply))

    conn.commit()
    conn.close()


def get_all_chats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM chat_logs
    ORDER BY id DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data