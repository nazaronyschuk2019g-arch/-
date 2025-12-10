import os
from dotenv import load_dotenv

# ЗМІНА 1: Завантажуємо змінні з файлу .env
load_dotenv()

# --- Конфіденційні дані (завантажуються з .env) ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
# ... інші змінні ...

# ЗМІНА 2: ПЕРЕВІРТЕ НАЯВНІСТЬ ЦЬОГО РЯДКА
DATABASE_URL = os.getenv("DATABASE_URL")

# ... інші статичні налаштування нижче ...
OXFORD_APP_ID = os.getenv("OXFORD_APP_ID")
OXFORD_APP_KEY = os.getenv("OXFORD_APP_KEY")

# --- Статичні налаштування для Oxford ---
# Базовий URL для словникових запитів (наприклад, для entry/definition)
OXFORD_BASE_URL = "https://od-api.oxforddictionaries.com/api/v2"
# Для отримання даних слова (де {word_id} - слово, {language_code} - en-us/en-gb)
OXFORD_ENDPOINT_ENTRIES = f"{OXFORD_BASE_URL}/entries/en-us/"

# Час щоденної розсилки (UTC). Наприклад, 8:00 UTC.
DAILY_SEND_HOUR = 8
DAILY_SEND_MINUTE = 0