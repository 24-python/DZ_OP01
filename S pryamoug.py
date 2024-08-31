# площадь прямоугольника и периметр прямоугольника

while True:
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    area = length * width

    perimeter = 2 * (length + width)

    print(f"Площадь прямоугольника: {area}, периметр прямоугольника: {perimeter}")
    choice = input("Хотите продолжить? (да/нет): ").strip().lower()
    if choice != "да":
        break  # Выход из цикла, если пользователь выбрал не продолжать