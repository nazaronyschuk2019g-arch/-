# handlers/command_handlers.py
from telebot import types
from core.db import add_user, has_user_received_today, save_word_progress
from core.vocabulary_api import get_daily_word_for_user
from core.scheduler import format_word_message


def handle_start(message, bot):
    """Обробник команди /start."""
    user_id = message.chat.id
    add_user(user_id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_word = types.KeyboardButton("🔍 Отримати слово зараз")
    markup.add(btn_word)

    welcome_message = (
        f"Вітаю, {message.from_user.first_name}! 👋\n"
        "Я ваш Тренер Словникового Запасу.\n"
        "Правило просте: Одне нове слово на день.\n"
        "Натисніть кнопку, щоб отримати своє слово на сьогодні!"
    )
    bot.send_message(user_id, welcome_message, reply_markup=markup)


def handle_send_word_now(message, bot):
    """Обробник кнопки 'Отримати слово зараз'."""
    user_id = message.chat.id

    # 1. ПЕРЕВІРКА: Чи отримував вже сьогодні?
    if has_user_received_today(user_id):
        bot.send_message(user_id, "🛑 Ви вже вивчили слово на сьогодні! Повертайтеся завтра за новою порцією знань. 🕒")
        return

    try:
        # Отримуємо дані слова
        word_data = get_daily_word_for_user(user_id)

        if word_data:
            # Відправляємо текст
            msg = format_word_message(word_data)
            bot.send_message(user_id, msg, parse_mode='Markdown')

            # Відправляємо аудіо (якщо є)
            if word_data.get('audio_link'):
                bot.send_chat_action(user_id, 'upload_voice')
                bot.send_audio(user_id, word_data['audio_link'], title=f"Pronunciation of {word_data['word']}")

            # Зберігаємо прогрес (щоб заблокувати повторне отримання)
            save_word_progress(user_id, word_data.get('id', 1))
        else:
            bot.send_message(user_id, "Вибачте, сталася помилка при пошуку слова.")

    except Exception as e:
        print(f"Помилка: {e}")
        bot.send_message(user_id, "Виникла технічна помилка.")