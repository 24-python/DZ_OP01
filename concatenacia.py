# Конкатенация строк, введенных через input

while True:
    text_1 = input("Введите первую строку: ")
    text_2 = input("Введите вторую строку: ")

    result = text_1 + text_2

    print(result)
    choice = input("Хотите продолжить? (да/нет): ").strip().lower()
    if choice != "да":
        break  # Выход из цикла, если пользователь выбрал не продолжать