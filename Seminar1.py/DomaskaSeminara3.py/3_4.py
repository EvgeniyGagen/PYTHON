# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('Введите число n = ')
n = int(input())
 
dvchislo = ''
 
while n > 0:
    dvchislob = str(n % 2) + dvchislo
    n = n // 2
 
print(dvchislo)