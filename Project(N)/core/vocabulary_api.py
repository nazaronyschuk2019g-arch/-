# core/vocabulary_api.py
import requests
import random

# Цей API повністю безкоштовний і не вимагає ключів
FREE_DICT_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def translate_word(word):
    """
    Тимчасова заглушка для перекладу, щоб не використовувати складні API.
    """
    # Маленький словничок для тесту
    dictionary = {
        "serendipity": "інтуїтивна прозорливість",
        "example": "приклад",
        "python": "пітон (мова програмування)",
        "developer": "розробник",
        "bot": "бот"
    }
    return dictionary.get(word.lower(), "Переклад відсутній (потрібен Google API)")


def fetch_and_get_word_data(word_text):
    """
    Отримує дані з безкоштовного API.
    """
    url = f"{FREE_DICT_API_URL}{word_text.lower()}"

    try:
        response = requests.get(url)

        # Якщо слова немає або помилка - повертаємо None
        if response.status_code != 200:
            print(f"API Error: {response.status_code}")
            return None

        data = response.json()[0]  # API повертає список, беремо перший елемент

        # Парсимо дані (витягуємо значення безпечно)
        definition = "Немає визначення"
        if "meanings" in data and data["meanings"]:
            definition = data["meanings"][0]["definitions"][0].get("definition", "Немає визначення")

        transcription = ""
        if "phonetic" in data:
            transcription = data["phonetic"]

        audio_link = None
        # Шукаємо аудіо
        if "phonetics" in data:
            for item in data["phonetics"]:
                if item.get("audio"):
                    audio_link = item["audio"]
                    break

        return {
            "id": 1,  # <--- ФІКТИВНИЙ ID, ЩОБ ВИПРАВИТИ ПОМИЛКУ 'id'
            "word": data.get("word", word_text),
            "definition": definition,
            "translation": translate_word(word_text),
            "transcription": transcription,
            "example": f"Example sentence for {word_text}",
            "audio_link": audio_link
        }

    except Exception as e:
        print(f"Критична помилка API: {e}")
        return None


def get_daily_word_for_user(telegram_id):
    """
    Вибирає слово для користувача.
    """
    # Список слів для ротації, щоб бот не видавав одне й те саме
    words = ["serendipity", "developer", "example", "python", "bot"]
    random_word = random.choice(words)

    return fetch_and_get_word_data(random_word)