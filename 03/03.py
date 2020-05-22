"""
Задача 3
Наибольший простой делитель
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
Ответ: 6857
"""
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: 
            return False
    return n > 1


def main():
    n = 600851475143
    max_div = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            max_div = i

    print(max_div)


if __name__ == "__main__":
    main()