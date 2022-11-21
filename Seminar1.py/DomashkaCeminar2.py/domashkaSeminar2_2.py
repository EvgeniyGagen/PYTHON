# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


print("Введите число  n = ")
n = int(input())
proizv = 1
while n > 0:
    
    proizv = proizv*n%10
    n = n//10

print(proizv)