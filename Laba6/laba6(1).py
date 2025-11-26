import time
import sqlite3
from functools import wraps

def timer_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start

        conn = sqlite3.connect("logs.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                function_name TEXT,
                exec_time REAL,
                timestamp TEXT
            )
        """)
        cursor.execute("""
            INSERT INTO logs(function_name, exec_time, timestamp)
            VALUES (?, ?, datetime('now'))
        """, (func.__name__, exec_time))

        conn.commit()
        conn.close()

        print(f"{func.__name__} виконана за {exec_time:.6f} сек")
        return result
    return wrapper
