# Task Слишком древний шифр


import random
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stone_insert1 = random.choice(numbers)
print('Число в первой вставке: ' + str(stone_insert1))

code = []
n = len(numbers)
for i in range(1, stone_insert1):
    k = i + 1
    for j in range(k, stone_insert1):
        if  stone_insert1 % (i + j) == 0:
            code.extend([i])
            code.extend([j])


print('Пароль для числа ' + str(stone_insert1) + ' - '),
print(* code)
