main_list = [12, 5, 8, 33, 2, 19, 40, 27, 14, 1,
             "стіл", "стілець", "ручка", "книга", "зошит",
             "дошка", "школа", "дзвоник", "учень", "клас"]

int_list = sorted([x for x in main_list if isinstance(x, int)])
str_list = sorted([x for x in main_list if isinstance(x, str)])

sorted_list = int_list + str_list

even_list = [x for x in int_list if x % 2 == 0]

caps_list = [s.upper() for s in str_list]

print("Головний список:", main_list)
print("Відсортований список (int ↑ + str a→я):", sorted_list)
print("Список парних чисел:", even_list)
print("Список рядків у CAPS:", caps_list)
