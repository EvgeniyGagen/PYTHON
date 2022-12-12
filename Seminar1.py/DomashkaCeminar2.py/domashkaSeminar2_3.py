# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.


print('Введите число n')
n = int(input())
lst = [round((1+1/i)**i, 4) for i in range(1, n+1)]
print(f'последовательность: {lst}\nСумма: {round(sum(lst))}')

# n = int(input())
# sum = 0
# i = 1
# for i in range(1, n+1):
#     result = (1+1/n)**n
#     sum = sum+result
#     i += 1
# print(sum)

# ===========================================
# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += (1 + 1 / i) ** i
# print(summ)


# Задача 4

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)

