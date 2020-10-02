#  Пользователь вводит время в секундах.
#  Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#  Используйте форматирование строк.

user_seconds = int(input("Input some seconds >>> "))

hour = user_seconds // 3600
minutes = user_seconds // 60 - (hour * 60)
sec = user_seconds % 60

print(f"input seconds =", user_seconds, "\nreformat time in HH:MM:SS =", hour, ":", minutes, ":", sec)
