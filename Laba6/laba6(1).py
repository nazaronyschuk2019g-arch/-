import time                # для вимірювання часу
import sqlite3             # для роботи з базою SQLite
from functools import wraps  # дозволяє зберегти назву та метадані функції


# --- Декоратор для вимірювання часу та логування в SQLite ---
def timer_logger(func):             # оголошуємо декоратор, який приймає функцію
    @wraps(func)                    # зберігаємо назву та docstring оригінальної функції
    def wrapper(*args, **kwargs):   # обгортка, яка виконується замість функції
        start = time.time()         # фіксуємо час до виконання
        result = func(*args, **kwargs)  # викликаємо оригінальну функцію
        end = time.time()           # час після виконання
        execution_time = end - start  # різниця — час виконання

        # --- Логування у SQLite ---
        conn = sqlite3.connect("logs.db")  # створюємо / відкриваємо базу logs.db
        cursor = conn.cursor()             # створюємо курсор для виконання SQL команд

        # створюємо таблицю, якщо її немає
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                function_name TEXT,
                exec_time REAL,
                timestamp TEXT
            )
        """)

        # вставляємо запис
        cursor.execute("""
            INSERT INTO logs(function_name, exec_time, timestamp)
            VALUES (?, ?, datetime('now'))
        """, (func.__name__, execution_time))

        conn.commit()    # зберігаємо зміни
        conn.close()     # закриваємо з’єднання

        print(f"Функція {func.__name__} виконана за {execution_time:.6f} сек")  # інфо в консоль

        return result    # повертаємо результат оригінальної функції

    return wrapper       # повертаємо обгортку
