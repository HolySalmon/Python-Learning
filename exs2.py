# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

input_num = input("Введите число n >>> ")
num = int(input_num)
double_num = int(input_num + input_num)
tripple_num = int(input_num + input_num + input_num)
summ = num + double_num + tripple_num
print(f"Введенное число =", input_num, "\nОдинарное число =", num, "\nДвойное число =", double_num, "\nТройное число =",
      tripple_num, "\nСумма всех трех чисел =", summ)
