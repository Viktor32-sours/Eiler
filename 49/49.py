"""
Задача 49
Перестановки простых чисел
Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330, необычна в двух отношениях: (1) каждый из трех членов является простым числом, (2) все три четырехзначные числа являются перестановками друг друга.

Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных простых чисел, демонстрирующих это свойство. Однако, существует еще одна четырехзначная возрастающая арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена этой прогрессии?
"""
from math import sqrt
import itertools as i

def is_prime(s):
    n = int(s)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return n > 1

# def isPrime(n):
    # n = int(n)
    # if n % 2 == 0:
    #     return n == 2
    # d = 3
    # while d * d <= n and n % d != 0:
    #     d += 2
    # return d * d > n
def permut_num(num):
    list_n = [i for i in i.permutations(str(num), 4)]
    list_permut = []
    for n in list_n:
        # print(''.join(n))
        list_permut.append(int(''.join(n)))

    return list_permut
    

def main():
    
    list_num = []
    for i in range(1000,10000):
        if is_prime(i):
            list_num.append(i)

    list_num.sort()
    # list_num.remove(list_num[-1])
    dic = {}
    for num in list_num:
        list_perm = permut_num(num)
        # list_perm.sort()
        temp_list = []
        for pm in list_perm:
            if pm in list_num:
                temp_list.append(pm)
            # temp_list = set(temp_list)
        if len(temp_list) < 4:
            continue
        dic[pm] = set(temp_list)
    print(len(dic))
    
    new_dic = {}
    for key in dic:
        if len(dic[key]) > 2  and is_prime(key):
            new_dic[key] = dic[key]
    print(len(new_dic))
    list_keys = list(new_dic.keys())
    list_keys.sort()
    i = 0
    for key in list_keys:
        k, v ,l = key, new_dic[key], len(new_dic[key])
        if l > 1:
            i += 1
            print(f'{i} - {k} : {v} : {l}')
            
    # print(len(dic))

    # permut_num(1487)
if __name__ == "__main__":
    main()