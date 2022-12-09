# ЗАДАЙТЕ СПИСОК ИЗ N последовательности (1+1/n)**n

from functools import reduce

n = int(input())
numbers = [round((1+1/n)**n, 2) for n in range(1, n + 1)]
print(f'Полученный список: {numbers}')

sum = reduce(lambda x, y: int(x) + int(y), numbers)
print(f'Сумма чисел списка: {sum}')