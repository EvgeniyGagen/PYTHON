# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# def elements(nums):
#     nums = [int(i) for i in nums.split()]
#     return list(set(nums))

# a= [1,2,2,2,2,3,1,4]

# print(set(a))

lst = list(map(int, input('Введите числа через пробел:\n').split()))
print(f'Исходный список: {lst}')
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f'Список из неповторяющхся элементов: {new_lst}')