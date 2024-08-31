# мультикалькулятр

while True:
    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))

    print("Вывод всех арифметических операций:")
    print("Сложение - ", number_1 + number_2)
    print("Вычитание - ", number_1 - number_2)
    print("Умножение - ", number_1 * number_2)

    # Проверка на деление на ноль
    if number_2 != 0:
        print("Деление - ", number_1 / number_2)
        print("Целая часть от деления - ", number_1 // number_2)
        print("Остаток от деления - ", number_1 % number_2)
    else:
        print("Деление на ноль невозможно")

    print("Возведение в степень - ", number_1 ** number_2)

    choice = input("Хотите продолжить? (да/нет): ").strip().lower()
    if choice != "да":
        break  # Выход из цикла, если пользователь выбрал не продолжать
