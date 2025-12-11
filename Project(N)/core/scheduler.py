# --- 1. Імпорти: планувальник, налаштування і функції роботи з БД/API ---
from apscheduler.schedulers.background import BackgroundScheduler         # для розкладу
from config import DAILY_SEND_HOUR, DAILY_SEND_MINUTE                    # час надсилання
from core.db import get_all_active_users, save_word_progress             # робота з БД
from core.vocabulary_api import get_daily_word_for_user                  # логіка слова дня


# --- 2. Формування повідомлення для користувача ---
def format_word_message(data):
    """Форматує дані слова в красиве повідомлення Markdown."""
    message = (
        f"🌟 **Слово Дня: {data['word']}** 🌟\n\n"
        f"🇺🇦 **Переклад:** _{data['translation']}_\n"
        f"🗣️ **Транскрипція:** `{data['transcription']}`\n\n"
        f"✍️ **Визначення (EN):** {data['definition']}\n\n"
        f"📝 **Приклад вживання:** \n>{data['example']}"
    )
    return message


# --- 3. Головне завдання, яке виконується щодня ---
def send_daily_word_job(bot):
    """Функція, що виконується за розкладом."""
    active_users = get_all_active_users()                               # отримуємо активних юзерів

    for user_id in active_users:
        try:
            word_data = get_daily_word_for_user(user_id)                # отримуємо слово
            if word_data:
                message = format_word_message(word_data)                # формуємо текст
                bot.send_message(user_id, message, parse_mode='Markdown')

                save_word_progress(user_id, word_data['id'])            # зберігаємо прогрес

        except Exception as e:
            print(f"Помилка при відправці слова користувачу {user_id}: {e}")
            # помилки типу: користувач заблокував бота


# --- 4. Налаштування та запуск планувальника ---
def setup_scheduler(bot):
    """Ініціалізує та запускає планувальник."""
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        send_daily_word_job,       # яку функцію запускати
        'cron',                    # тип розкладу
        hour=DAILY_SEND_HOUR,      # година
        minute=DAILY_SEND_MINUTE,  # хвилина
        args=[bot]                 # передаємо бота у функцію
    )

    scheduler.start()

    print("Планувальник запущено.")
