#ПРОДВИНУТЫЙ КОНВЕРТЕР ДОЛЛАР РУБЛЬ рубль доллар

import requests

def get_usd_rate():
    # URL API Центрального банка России для получения курсов валют
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    try:
        response = requests.get(url).json()
        # Получаем курс доллара США
        return response['Valute']['USD']['Value']
    except Exception as e:
        print(f"Произошла ошибка при получении данных: {e}")
        # Возвращаем None, если произошла ошибка
        return None

current_rate = get_usd_rate()
if current_rate is not None:
    print(f"Текущий курс доллара США: {current_rate} руб.")
else:
    print("Не удалось получить актуальный курс валюты. Попробуйте позже.")
    exit() # Выход из программы, если не удалось получить курс

while True:
    conversion_type = input("Выберите конвертацию: 1. Рубль в доллар 2. Доллар в рубль (введите 1 или 2): ").strip()
    if conversion_type not in ["1", "2"]:
        print("Пожалуйста, выберите корректный вариант конвертации.")
        continue

    try:
        if conversion_type == "1":
            rur = float(input("Введите сумму в рублях: "))
            result = rur / current_rate
            print(f"Вы получите {result:.2f} долларов США")
        elif conversion_type == "2":
            usd = float(input("Введите сумму в долларах: "))
            result = usd * current_rate
            print(f"Вы получите {result:.2f} рублей")
    except ValueError:
        print("Пожалуйста, введите корректную сумму.")
        continue

    choice = input("Хотите продолжить конвертацию? (да/нет): ").strip().lower()
    if choice != "да":
        break  # Выход из цикла, если пользователь выбрал не продолжать