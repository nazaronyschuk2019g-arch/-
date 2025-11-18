# --- Імпорти 10 бібліотек ---
import numpy as np        # масиви
import requests           # запити
import pandas as pd       # таблиці
import matplotlib.pyplot as plt  # графіки
from PIL import Image     # зображення
import tqdm               # прогрес-бар
from bs4 import BeautifulSoup  # html
import seaborn as sns     # графіки
import scipy              # обчислення
import flask              # веб

# --- 5 спроб використати бібліотеки ---

try:
    print(np.array([1, 2, 3]) + 1)     # NumPy: просте додавання
except Exception as e:
    print(e)

try:
    r = requests.get("https://example.com")  # Requests: запит
    print(r.status_code)
except Exception as e:
    print(e)

try:
    print(pd.DataFrame({"a": [1, 2]}))   # Pandas: маленька таблиця
except Exception as e:
    print(e)

try:
    plt.plot([1, 2], [3, 4])             # Matplotlib: графік
    plt.savefig("plot.png")
    print("Графік ок")
except Exception as e:
    print(e)

try:
    Image.new("RGB", (50, 50), "blue").save("img.png")  # Pillow: створення картинки
    print("Картинка ок")
except Exception as e:
    print(e)
