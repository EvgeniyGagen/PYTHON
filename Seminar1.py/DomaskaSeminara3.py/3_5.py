# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# fi1 = 1
# fi2 = 1
 
# n = input("Номер элемента Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fi_sum = fi1 + fi2
#     fi1 = fi2
#     fi2 = fi_sum
#     i = i + 1
#     print( fi2)
# # print("Значение этого элемента:", fi2)
# print(fi2 )

n = input("Номер эл-та Фибоначчи: ")
n = int(n)

def fi(n):
    if n in [1, 2]:
        return 1
    else:
        return fi(n - 1) + fi(n - 2)
list = []
for e in range (1,n):
    list.append(fi(e))
print(list)