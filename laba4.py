# Словник, що імітує базу даних товарів та їх цін
store = {
    'apple': 15.85,
    'banana': 202,
    'cheese': 320,
    'milk': 35.25,
    'carrot': 89.9,
    'tomato': 18,
    'meat': 250,
    'juice': 61
}

# Функція для гарного форматування ціни (2 знаки після коми)
def format_price(price):
    return f"price: {price:.2f} UAH"  # Повертає f-рядок з форматованою ціною

# Функція, що перевіряє наявність списку товарів у 'store'
def check(products):
    result = {}  # Створюємо порожній словник для результатів
    for product in products:  # Перебираємо кожен товар у списку
        # Записуємо True/False у 'result' залежно від наявності товару в 'store'
        result[product] = product in store
    return result  # Повертаємо словник з результатами перевірки

# Функція для обробки замовлення
def order(products):
    availability = check(products)  # Отримуємо словник наявності товарів

    # Перевіряємо, чи ВСІ значення у словнику 'availability' є True
    if all(availability.values()):
        total = 0  # Початкова загальна сума
        for product in products:  # Перебираємо товари для підрахунку суми
            total += store[product]  # Додаємо ціну товару до загальної суми
        # Повертаємо повідомлення про успіх та загальну вартість
        return f"Усі товари є! Загальна {format_price(total)}"
    else:
        # Створюємо список 'miss' з товарів, яких немає (де available == False)
        miss = [product for product, available in availability.items()
                if not available]
        # Повертаємо повідомлення з переліком відсутніх товарів
        return f"Немає в наявності: {' '.join(miss)}"

# Головна функція програми (точка входу)
def main():
    while True:  # Створюємо нескінченний цикл (меню)
        print("1 - Переглянути ціну\n2 - Купити")  # Друкуємо опції меню
        choice = input("Your choice: ")  # Отримуємо вибір користувача

        user_input = input("Введи товари через пробіл: ")  # Отримуємо список товарів
        products = user_input.split()  # Розбиваємо рядок на список товарів по пробілу

        if choice == "1":  # Якщо користувач обрав '1' (Перегляд)
            availability = check(products)  # Перевіряємо наявність
            for product, is_available in availability.items():  # Перебираємо результати
                if is_available:  # Якщо товар є
                    # Друкуємо назву та форматовану ціну
                    print(f"{product} – {format_price(store[product])}")
                else:  # Якщо товару немає
                    print(f"{product} – нема в наявності")

        elif choice == "2":  # Якщо користувач обрав '2' (Купівля)
            print(order(products))  # Викликаємо функцію 'order' і друкуємо результат
        else:  # Якщо введено будь-що інше
            print("Невірний вибір, спробуй ще раз.")

# Ця конструкція гарантує, що 'main()' запуститься тільки тоді, 
# коли файл запускається напряму (а не імпортується)
if __name__ == "__main__":
    main()  # Запускаємо головну функцію
