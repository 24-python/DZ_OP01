# Написать программу, которая будет запрашивать у пользователя его имя и возраст,
# а затем выводить приветствие “Привет [имя]! Тебе [возраст]”.

while True:
  name = input("Введите свое имя: ")
  age = int(input("Сколько Вам лет: "))

  months_lived = age * 12
  days_lived = int(age * 365.25)  # учитываем високосные года
  hours_lived = days_lived * 24
  minutes_lived = hours_lived * 60
  seconds_lived = minutes_lived * 60

  print(f"Привет, {name}! Тебе {age} лет.")
  print(f"Ты живешь уже {months_lived} месяцев.")
  print(f"Ты живешь уже {days_lived} дней.")
  print(f"Ты живешь уже {hours_lived} часов.")
  print(f"Ты живешь уже {minutes_lived} минут.")
  print(f"Ты живешь уже {seconds_lived} секунд.")

  choice = input("Хотите продолжить? (да/нет): ").strip().lower()
  if choice != "да":
      break  # Выход из цикла, если пользователь выбрал не продолжать