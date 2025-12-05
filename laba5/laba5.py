# Імпорт 10 бібліотек (5 вбудованих + 5 зовнішніх)
import math
import random
import datetime
import json
import os

import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

print("=== Лабораторна робота №5 ===")

# 1. requests
try:
    response = requests.get("https://api.github.com")
    print("Запит до GitHub API — статус:", response.status_code)
except Exception as e:
    print("Помилка з requests:", e)

# 2. numpy
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("Сума елементів через NumPy:", np.sum(arr))
except Exception as e:
    print("Помилка з numpy:", e)

# 3. pandas
try:
    data = {"name": ["David", "Tom"], "age": [16, 17]}
    df = pd.DataFrame(data)
    print("Таблиця через Pandas:\n", df)
except Exception as e:
    print("Помилка з pandas:", e)

# 4. matplotlib
try:
    plt.plot([1, 2, 3], [2, 4, 6])
    plt.title("Графік від matplotlib")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
except Exception as e:
    print("Помилка з matplotlib:", e)

# 5. faker
try:
    fake = Faker()
    print("Випадкове ім'я через Faker:", fake.name())
except Exception as e:
    print("Помилка з faker:", e)

print("\nРобота завершена успішно ✅")
