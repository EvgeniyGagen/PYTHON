# сумма вещественных чисел
number = float(input("Введите вещественное число: "))
new_sum = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр вещественного числа равна = {new_sum}")
