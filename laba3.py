def main():
    students = {}  

    while True:
        name = input("Введіть ім'я студента (або 'stop' для завершення): ")
        if name.lower() == "stop":
            break
        try:
            grade = int(input(f"Введіть оцінку для {name}: "))
            if 1 <= grade <= 12:
                students[name] = grade
            else:
                print("Оцінка має бути від 1 до 12.")
        except ValueError:
            print("Будь ласка, введіть число!")

    if not students:
        print("Дані не введено.")
        return

    print("\nСписок студентів та їх оцінок:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    average = sum(students.values()) / len(students)
    vidminnyky = [name for name, grade in students.items() if 10 <= grade <= 12]
    khoroshysty = [name for name, grade in students.items() if 7 <= grade <= 9]
    vidstayuchi = [name for name, grade in students.items() if 4 <= grade <= 6]
    nezdaly = [name for name, grade in students.items() if 1 <= grade <= 3]

    print("\nСтатистика:")
    print(f"Середній бал групи: {average:.2f}")
    print(f"Відмінники ({len(vidminnyky)}): {', '.join(vidminnyky) if vidminnyky else 'немає'}")
    print(f"Хорошисти ({len(khoroshysty)})")
    print(f"Відстаючі ({len(vidstayuchi)})")
    print(f"Не здали ({len(nezdaly)})")

if __name__ == "__main__":
    main()
