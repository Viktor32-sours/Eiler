"""
Задача 10
Сложение простых чисел
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов

Ответ: 142913828922

"""
from math import sqrt




def primes(N):
    sieve = set(range(2, N))
    for i in range(2, int(sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))
    return sieve


    
def main():
    # n = 2000000
    n = 100
    print(sum(primes(n)))
    
if __name__ == "__main__":
    main() 

