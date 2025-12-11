import telebot                              # імпорт бібліотеки для телеграм-бота
from config import BOT_TOKEN                # токен бота з конфіга
from core.scheduler import setup_scheduler  # функція підключення планувальника
from handlers.command_handlers import (handle_start, handle_send_word_now) # імпорт обробників команд
import time                                 # для паузи при помилках


bot = telebot.TeleBot(BOT_TOKEN)            # створення екземпляра бота


@bot.message_handler(commands=['start'])    # обробник команди /start
def start_message(message):
    handle_start(message, bot)              # виклик функції старту


@bot.message_handler(regexp='^🔍 Отримати слово зараз$')  # обробка кнопки
def send_word_now_message(message):
    handle_send_word_now(message, bot)      # відправка слова "зараз"


if __name__ == '__main__':                  # запуск скрипта напряму

    setup_scheduler(bot)                    # запуск щоденного розкладу

    print("Бот запущено. Початок опитування Telegram...")  # лог

    try:
        bot.polling(none_stop=True,         # без зупинки при помилках
                     interval=0)            # без затримки між отриманням апдейтів
    except Exception as e:
        print(f"Помилка під час опитування бота: {e}")  # лог помилки
        time.sleep(5)                       # пауза 5 сек і повтор

