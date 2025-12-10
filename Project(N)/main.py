import telebot
from config import BOT_TOKEN
from core.scheduler import setup_scheduler
from handlers.command_handlers import handle_start, handle_send_word_now
import time

# Ініціалізація бота
bot = telebot.TeleBot(BOT_TOKEN)


# --- Обробники Команд ---

@bot.message_handler(commands=['start'])
def start_message(message):
    handle_start(message, bot)


@bot.message_handler(regexp='^🔍 Отримати слово зараз$')
def send_word_now_message(message):
    handle_send_word_now(message, bot)


# --- Запуск ---

if __name__ == '__main__':

    # 1. Запуск Планувальника для щоденної розсилки
    setup_scheduler(bot)

    # 2. Запуск Бота
    print("Бот запущено. Початок опитування Telegram...")

    # Цикл polling для обробки вхідних повідомлень
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Помилка під час опитування бота: {e}")
        time.sleep(5)