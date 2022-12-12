# Перемешивание списка


import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    temp = list[i]
    list[i] = list[index_a]
    list[index_a] = temp
print(list)
# import random 
# y = ['Apple', '2 ', '-5675 ', '0.678 ', 'morning']
# random.shuffle(y)
# print(y)
