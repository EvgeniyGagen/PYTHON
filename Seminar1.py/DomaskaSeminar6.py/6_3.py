# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12   CЕРГЕЙ

def sum_odd_index(lst: list) -> int:
    l = enumerate(lst)
    l1 = filter(lambda e: e[0] % 2 == 1, l)
    print(l1)
    l2 = list(zip(*l1))
    print(l2)
    l3 = list(l2[1])
    print(l3)
    return sum(l3)
 

print(sum_odd_index([2, 3, 5, 9, 3]))