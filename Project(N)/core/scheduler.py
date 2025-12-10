from apscheduler.schedulers.background import BackgroundScheduler
from config import DAILY_SEND_HOUR, DAILY_SEND_MINUTE
from core.db import get_all_active_users, save_word_progress
from core.vocabulary_api import get_daily_word_for_user


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


def send_daily_word_job(bot):
    """Функція, що виконується за розкладом."""
    active_users = get_all_active_users()

    for user_id in active_users:
        try:
            word_data = get_daily_word_for_user(user_id)
            if word_data:
                message = format_word_message(word_data)
                bot.send_message(user_id, message, parse_mode='Markdown')

                # Зберігаємо прогрес (яке слово відправлено)
                save_word_progress(user_id, word_data['id'])

        except Exception as e:
            # Обробка помилок Telegram API, якщо користувач заблокував бота
            print(f"Помилка при відправці слова користувачу {user_id}: {e}")


def setup_scheduler(bot):
    """Ініціалізує та запускає планувальник."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        send_daily_word_job,
        'cron',
        hour=DAILY_SEND_HOUR,
        minute=DAILY_SEND_MINUTE,
        args=[bot]
    )
    scheduler.start()
    print("Планувальник запущено.")