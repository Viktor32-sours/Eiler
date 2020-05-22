"""
 Задача 28
Диагонали числовой спирали
Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

Можно убедиться, что сумма чисел в диагоналях равна 101.

Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?
Ответ: 669171001
"""
from itertools import cycle

n = 1001 # размер матрицы
 
# directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
# directions = ((1, 0),(0, 1), (-1, 0), (0, -1))
# directions = ((0, -1),(1, 0),(0, 1),(-1, 0))
directions = ((0, 1),(1, 0), (0, -1), (-1, 0)) # направление заполнения 
nums = range(2, n*n+1) # генератор значений

# генератор длинны шага спирали
def length_producer(_max):
    curr_l = _max
    while curr_l > 0:
        yield curr_l
        curr_l -=1
        yield curr_l

l_p = list(length_producer(n))[:-1] # отбрасываем 0
l_p[0] = l_p[0] - 1 # уменьшаем на 1 последний шаг, иначе выходим за грань
l_p.reverse() #  разворачиваем список

buffer = []
for i in range(n):
    buffer.append([None]*n)
 
curr_i, curr_j = n//2, n//2

buffer[curr_i][curr_j] = 1 # вставляем 1 в центр матрицы

values_iterator = iter(nums)
 
for l, d in zip(l_p, cycle(directions)):
    # print(l, d)
    
    for i in range(l):
        num = next(values_iterator)
        curr_i += d[0]
        curr_j += d[1]
        buffer[curr_i][curr_j] = num
        # print(f'curr_i = {curr_i}, curr_j = {curr_j}, num = {num}')

# for line in buffer:
#     print(line)

sum_diag = 0

for x in range(n):
    sum_diag += buffer[x][x]
    sum_diag += buffer[x][n-1-x]



print(sum_diag - 1) # единица входит в сумму 2 раза