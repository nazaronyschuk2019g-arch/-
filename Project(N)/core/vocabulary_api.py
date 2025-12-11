# --- 1. Імпорти та базові налаштування ---
# Робота з HTTP-запитами + random для вибору слова
import requests
import random

# Безкоштовне API (не потребує ключів)
FREE_DICT_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


# --- 2. Тимчасовий перекладач (заглушка) ---
def translate_word(word):
    """
    Тимчасова заглушка для перекладу, щоб не використовувати складні API.
    """
    # Мини-словник для тестів
    dictionary = {
        "serendipity": "інтуїтивна прозорливість",
        "example": "приклад",
        "python": "пітон (мова програмування)",
        "developer": "розробник",
        "bot": "бот"
    }
    return dictionary.get(word.lower(), "Переклад відсутній (потрібен Google API)")


# --- 3. Робота з DictionaryAPI: отримання визначення, транскрипції, аудіо ---
def fetch_and_get_word_data(word_text):
    """
    Отримує дані з безкоштовного API.
    """
    url = f"{FREE_DICT_API_URL}{word_text.lower()}"

    try:
        response = requests.get(url)

        # Якщо слова немає або API повернуло помилку
        if response.status_code != 200:
            print(f"API Error: {response.status_code}")
            return None

        data = response.json()[0]  # API повертає список → беремо перший елемент

        # --- Безпечне витягування визначення ---
        definition = "Немає визначення"
        if "meanings" in data and data["meanings"]:
            definition = data["meanings"][0]["definitions"][0].get("definition", "Немає визначення")

        # --- Транскрипція ---
        transcription = ""
        if "phonetic" in data:
            transcription = data["phonetic"]

        # --- Пошук аудіо ---
        audio_link = None
        if "phonetics" in data:
            for item in data["phonetics"]:
                if item.get("audio"):
                    audio_link = item["audio"]
                    break

        return {
            "id": 1,  # фіктивний ID (щоб не падали інші частини коду)
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


# --- 4. Вибір слова дня для користувача ---
def get_daily_word_for_user(telegram_id):
    """
    Вибирає слово для користувача.
    """
    # Список слів, які бот може давати в ротації
    words = ["serendipity", "developer", "example", "python", "bot"]

    random_word = random.choice(words)  # випадковий вибір

    return fetch_and_get_word_data(random_word)
