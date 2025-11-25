# --- Імпорти 10 бібліотек ---
import numpy as np        # імпортуємо NumPy та даємо коротке ім'я np для роботи з масивами
import requests           # імпортуємо бібліотеку для виконання HTTP-запитів
import pandas as pd       # імпортуємо Pandas і скорочуємо як pd для роботи з таблицями DataFrame
import matplotlib.pyplot as plt  # імпортуємо модуль побудови графіків з Matplotlib
from PIL import Image     # імпортуємо клас Image з бібліотеки Pillow для роботи із зображеннями
import tqdm               # імпортуємо tqdm для показу прогрес-барів
from bs4 import BeautifulSoup  # імпортуємо парсер HTML-документів
import seaborn as sns     # імпортуємо Seaborn — бібліотеку для красивих графіків
import scipy              # імпортуємо SciPy — наукова бібліотека з великою кількістю алгоритмів
import flask              # імпортуємо Flask — фреймворк для створення веб-додатків

# --- 5 спроб використати бібліотеки ---

try:
    print(np.array([1, 2, 3]) + 1)     # створюємо масив NumPy і додаємо 1 до кожного елемента
except Exception as e:
    print(e)                           # якщо виникне помилка — виводимо її

try:
    r = requests.get("https://example.com")  # надсилаємо GET-запит на сервер example.com
    print(r.status_code)                     # виводимо HTTP-код відповіді (200, 404 тощо)
except Exception as e:
    print(e)                                 # у разі помилки виводимо текст помилки

try:
    print(pd.DataFrame({"a": [1, 2]}))   # створюємо DataFrame з одного стовпця "a" та двох рядків
except Exception as e:
    print(e)                              # виводимо помилку, якщо щось піде не так

try:
    plt.plot([1, 2], [3, 4])             # будуємо простий графік: точки (1,3) і (2,4)
    plt.savefig("plot.png")              # зберігаємо графік у файл plot.png
    print("Графік ок")                   # повідомляємо, що графік створено
except Exception as e:
    print(e)                             # показуємо помилку, якщо вона з'явиться

try:
    Image.new("RGB", (50, 50), "blue").save("img.png")  # створюємо нове зображення 50x50 синього кольору й зберігаємо
    print("Картинка ок")                                 # повідомляємо, що зображення збережене
except Exception as e:
    print(e)                                             # виводимо помилку при невдалій операції
