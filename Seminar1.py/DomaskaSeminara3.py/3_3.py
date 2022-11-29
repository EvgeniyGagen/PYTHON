# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19




list = [1.1, 1.2, 3.1, 5, 10.01]
drmax = list[0]
drmin = list[0]
i = 4
# num = list[i]*100
for i in range(len(list)):
    num = list[i]*100
    if (num%100 > drmax):
        drmax = num
        print(drmax)
    else:
        (num%100 < drmin)
        drmin = num
        print(drmin)
print(drmax - drmin)