# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def elements(nums):
    nums = [int(i) for i in nums.split()]
    return list(set(nums))

a= [1,2,2,2,2,3,1,4]

print(set(a))