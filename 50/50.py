"""
Сумма последовательных простых чисел
Простое число 41 можно записать в виде суммы шести последовательных простых чисел:

41 = 2 + 3 + 5 + 7 + 11 + 13
Это - самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной сотни.

Самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной тысячи, содержит 21 слагаемое и равна 953.

Какое из простых чисел меньше одного миллиона можно записать в виде суммы наибольшего количества последовательных простых чисел?
Ответ: 
"""
# from math import sqrt


# def is_prime(s):
#     n = int(s)
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0: 
#             return False
#     return n > 1

# def isPrime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#         d += 2
#     return d * d > n

# def list_prime(n):
#     l_p = set()
#     l_p.add(2)
#     for i in range(3,n,2):
#         if isPrime(i):
#             l_p.add(i)
#     return l_p

# def primes(N):
#     sieve = set(range(2, N))
#     for i in range(2, int(sqrt(N))):
#         if i in sieve:
#             sieve -= set(range(2*i, N, i))
#     return list(sorted(sieve))


# def posled(list_prime):
#     # len_m = []
#     max_len = 0
#     for i in range(len(list_prime)):
#         for e in range(i + 1, len(list_prime)+1):
#         # print(i,e)
#             posl = list_prime[i:e]
#             # print(i,e, posl)
#             if sum(posl) in list_prime and len(posl) > max_len:
#                 max_len = len(posl)
#                 len_m = posl
#     print(max_len, len_m, sum(len_m))

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0 or n % int(n/i) == 0:return False
    return True



def main():
    primes= [i for i in range(2,int(10**3.6),1) if is_prime(i)]
    # print(primes, sum(primes))
    max_sqnc,max_num = 0,0
    i,j = 0,len(primes)
    while len(primes[i:]) > max_sqnc:
        j = len(primes)+1
        while j > 0:
            n = primes[i:j]
            if is_prime(sum(n)) and sum(n) < 10**6 and max_sqnc < len(n):
                max_sqnc, max_num = len(n), sum(n)
                break
            j -= 1
        i += 1
    print(max_num, max_sqnc)


if __name__ == "__main__":
    main()