def count_pairs(filename, pairs):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:

                pairs_list = {}

                for pair in pairs:
                    pairs_list[pair] = 0

                words = line.lower().split()

                for word in words:
                    for i in range(len(word) - 1):
                        current_pair = word[i:i+2]
                        if current_pair in pairs_list:
                            pairs_list[current_pair] += 1

                yield pairs_list
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return
def main():
    FILE = "text.txt"
    PAIRS = ['su', 'on', 'ps']
    result = count_pairs(FILE, PAIRS)
    i = 1
    for res in result:
        print(f"Рядок №{i}: {res}")
        i += 1

if __name__ == "__main__":
    main()
