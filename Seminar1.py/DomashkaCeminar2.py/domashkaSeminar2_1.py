# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


print("Введите число  n = ")
n = int(input())
sum = 0
while n > 0:
    
    sum = sum + n%10
    n = (n - n%10)/10
print(sum)