# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


print("Введите число  n = ")
n = int(input())
sum = 0
while n > 0:
    
    sum = sum + n%10
    n = (n - n%10)/10
print(sum)

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))
# # s = '0.56'
# # summ = 0
# # for i in s:
# #     if i.isdigit():
# #         summ += int(i)
# # print(summ)
