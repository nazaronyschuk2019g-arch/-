from timer_logger import timer_logger   # імпортуємо декоратор з іншого файлу
import time                             # для імітації довгої роботи


# --- Функція, яку будемо декорувати ---
@timer_logger                        # застосовуємо наш декоратор
def slow_function():                 # звичайна функція
    time.sleep(1.5)                  # затримка 1.5 секунди
    return "Готово!"                 # повертаємо результат


# --- Виклик функції ---
print(slow_function())      
