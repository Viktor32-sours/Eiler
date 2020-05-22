"""
Круговые простые числа
Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?

Ответ: 55
"""

from math import sqrt
from time import time

def iter(n):
    list_char = []
    s = str(n)
    for i in range(len(s)):
        var = s[i:] + s[:i]
        list_char.append(var)
    return list_char

def isPrime(n):
    n = int(n)
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
       
def is_prime(s):
    n = int(s)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return n > 1


def is_crug(set_):
    res = 1
    for elem in set_:
        if isPrime(elem):
            continue
        res *= 0
    return res

def main():
    # n = int(input('Введите границу (1000000): '))
    n = 1000000

    
    list_crug = set()
    list_crug.add(2)
    list_crug.add(3)
    list_crug.add(5)

    for i in range(5, n, 2):
        if  "2" in str(i) or "4" in str(i) or "6" in str(i) or "8" in str(i) or "0" in str(i) or "5" in str(i):
            continue

        if is_prime(i):
            if i not in list_crug:
                list_char = iter(i)
                if is_crug(list_char):
                    list_crug.add(i)

    print(sorted(list_crug), len(list_crug))

if __name__ == "__main__":
    main()