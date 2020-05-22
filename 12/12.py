# coding: utf-8
# Треугольное число с большим количеством делителей
"""
Последовательность треугольных чисел образуется путем сложения натуральных чисел. 
К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

     1: 1
     3: 1, 3
     6: 1, 2, 3, 6
    10: 1, 2, 5, 10
    15: 1, 3, 5, 15
    21: 1, 3, 7, 21
    28: 1, 2, 4, 7, 14, 28 

Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?
Ответ: 
Максимальная длина списка делителей: 576
Треугольное число: 76576500
Время вычисления: 0:00:25.392255

Максимальная длина списка делителей: 1024
Треугольное число: 842161320
Время вычисления: 0:14:59.544686
"""
from datetime import datetime
# from multiprocessing import Pool
# import os

#  генератор треугольных чисел
def triang_num(end, begin=2, num=1):
    list_num = []
    # ~ num = 1
    for i in range(begin,end+2):
        list_num.append(num)
        num += i
    # ~ print(list_num)
    return list_num, i, num-i
    # return list_num, num-i

# ~ print(triang_num(5))
# нахождение числа делителей
def kol_del(num):
    i = 1
    list_del = []
    while i*i < num:
        if num % i == 0:
            list_del.append(i)
            if num != num // i:
                list_del.append(num//i)
        i += 1
    list_del.append(num)
    list_del.sort()
    return list_del

# 
# нахождение максимальной длины списка 'l' и самого списка 'k'
def max_leng(list_num):
    
    l_max = 1  
    l = []
    k = [] 
    for elem in list_num:
        kol = kol_del(elem)
        leng = len(kol)
        if leng > l_max:
            l_max = leng
            l.append(l_max)
            k.append(kol)

    return l[-1], k[-1] , elem       

def make_all(n, begin=2, num=1):
    
    triang_num(n, begin=2, num=1)
    kol_del(num)
    max_leng(list_num)

def main():
    
    d = int(input('Введите число делителей: '))
    x = int(input('Введите шаг итераций(100, 200, ...): ')) # инкрементный шаг итераций
    start = datetime.now()
    n = d
    list_num , i, num = triang_num(n)
    
    max_l, max_spis, elem = max_leng(list_num)

   
    
    while max_l < d:
        list_num, i, num  = triang_num(n,i, num)
        
             
        max_l, max_spis, elem = max_leng(list_num)
        n += x
        print(f'Продолжаем поиск...кол-во треугольных чисел Т = {n}')

    print(f'Максимальная длина списка делителей: { max_l}')    
    # print(f'Список делителей: \n{ max_spis}')    
    print(f'Треугольное число: { max_spis[-1]}')    
    end = datetime.now()
    total = end - start
    print(f'Время вычисления: {total}')
    
if __name__ == '__main__':
    main()
