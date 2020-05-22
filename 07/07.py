"""
Задача 7
10001-ое простое число
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?
Ответ: 104743

"""


#---------------------------------------------------------------
from sys import argv
from time import time

def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i

def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1

def naive(n):
    from itertools import count, islice
    primes = (n for n in count(2) if all(n % d for d in range(2, n)))
    return islice(primes, 0, n)

def isPrime(n):
    import re
    # see http://tinyurl.com/3dbhjv
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None

def regexp(n):
    import sys
    N = int(sys.argv[1]) # number of primes wanted (from command-line)
    M = 100              # upper-bound of search space
    l = list()           # result list

    while len(l) < N:
        l += filter(isPrime, range(M - 100, M)) # append prime element of [M - 100, M] to l
        M += 100                                # increment upper-bound

    return l[:N] # print result list limited to N elements

def dotime(func, n):
    # print(func.__name__)
    start = time()
    print(sorted(list(func(n)))[-1])
    print('Time in seconds: ' + str(time() - start))

# if __name__ == "__main__":
#     for func in naive, historic, regexp:
#         dotime(func, int(argv[1]))

def main():
    n = 10001

    dotime(historic, int(n))
    
if __name__ == "__main__":
    main() 
