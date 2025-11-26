from decorator import timer_logger

@timer_logger
def my_function():
    for _ in range(2_000_000):
        pass
    return "Готово!"

print(my_function())
