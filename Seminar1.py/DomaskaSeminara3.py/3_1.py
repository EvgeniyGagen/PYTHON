# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# list = [2, 3, 5, 9, 3]


# sum = 0
# for i in range(len(list)):
#     if list[i]%2 == 1:
#         sum += list[i]
#         print(sum)
#     else:
#         print('no')

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '2 3 4 5 9 3'.split()

res = select(int, data)
res = where(lambda x: x%2 !=0, res)
res = select(lambda x: (x, x + x), res)

print(res)