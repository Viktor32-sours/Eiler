"""
Задача 5
Наименьшее кратное
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
Ответ: 232792560

"""
from functools import reduce

def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

res = reduce(lcm, range(2, 21))
print(res)
# 232792560