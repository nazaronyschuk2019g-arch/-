def count_pairs(filename, pairs):
    try:
        with open(filename, 'r', encoding='utf-8') as f:   # відкриваємо файл
            for line in f:                                # читаємо файл построчно

                pairs_list = {}                           # створюємо словник для підрахунку

                for pair in pairs:                        # проходимо кожну пару з заданих
                    pairs_list[pair] = 0                  # ініціалізуємо лічильник нулем

                words = line.lower().split()              # робимо весь рядок маленькими буквами і ділимо на слова

                for word in words:                        # перебираємо кожне слово
                    for i in range(len(word) - 1):        # перебираємо індекси для пар
                        current_pair = word[i:i+2]        # беремо пару символів
                        if current_pair in pairs_list:    # якщо ця пара є у списку
                            pairs_list[current_pair] += 1 # збільшуємо лічильник

                yield pairs_list                          # повертаємо результат для цього рядка
    except Exception as e:                                # ловимо помилки (файл не знайдено тощо)
        print(f"Помилка при читанні файлу: {e}")
        return                                             # завершуємо функцію


def main():
    FILE = "text.txt"                                     # назва файлу
    PAIRS = ['su', 'on', 'ps']                            # пари для підрахунку
    result = count_pairs(FILE, PAIRS)                     # отримуємо генератор
    i = 1                                                 # лічильник рядків
    for res in result:                                    # проходимо кожен результат
        print(f"Рядок №{i}: {res}")                       # виводимо
        i += 1                                            # збільшуємо номер рядка


if __name__ == "__main__":                                # точка входу
    main()
