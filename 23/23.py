"""
Задача 23
Неизбыточные суммы
Идеальным числом называется число, у которого сумма его делителей равна самому числу. 
Например, сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28, что означает, 
что число 28 является идеальным числом.
Число n называется недостаточным, если сумма его делителей меньше n, и называется избыточным, 
если сумма его делителей больше n.

Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16), наименьшее число, 
которое может быть записано как сумма двух избыточных чисел, равно 24. Используя математический 
анализ, можно показать, что все целые числа больше 28123 могут быть записаны как сумма двух 
избыточных чисел. Эта граница не может быть уменьшена дальнейшим анализом, даже несмотря на то, 
что наибольшее число, которое не может быть записано как сумма двух избыточных чисел, меньше этой 
границы.

Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных 
чисел.
Ответ: 4179871
"""

# list_num = [i for i in range(1, 28123+1)]

# def sum_div(n):
#     s = 0
#     for i in range(1, n//2 + 1):
#         if n % i == 0:
#             s += i
#     return s

def main():
    sums = 1
    for i in range(2, 28123):
        boo = True
        for k in lAbundants:
            if k < i:
                if (i-k) in dAbundants:
                    boo = False
                    break
            else : break
        if boo == True: sums += i

    print(sums)
    # max_izb = 24
    
    # list_izb = []
    # for i in range(12, max_izb + 1, 2):
    #     if sum_div(i) > i:
    #         list_izb.append(i)
    # set_izb = set(list_izb)

    # # print(set_izb)
    # sum_izb = []
    # for num in range(1, max_izb + 1):
    #     # print(num)
    #     for izb in set_izb:
    #         print(num, izb)
    #         if izb >= num and (izb - num) in set_izb:
    #             print(num)
    #             sum_izb.append(num)

    # #         #     print('num')
    # set_izb = set(sum_izb)   
    #     # 
            
    # print(set_izb)
    # s = sum(set_izb)
    # print(s)
#------------------------------------------------------------
    # def is_abundant(n):
    #     max_divisor = int(n / 2) + 1
    #     sum = 0
    #     for x in range(1, max_divisor):
    #         if n % x == 0:
    #             sum += x  
    #     return sum > n

    # abundants = list(x for x in range(1, 28123) if is_abundant(x))

    # sums = 0
    # for i in range(12, 28123):
    #     for abundant in abundants:
    #         if abundant >= i and is_abundant(i + abundant):
    #             sums += i
    # print(sums)
#-----------------------------------------------------------------------------
def GetSumOfDivs(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n%i == 0:
            upper = n/i
            total += upper
            if upper != i: total += i
        i += 1
    return total


def isabundant(n): return GetSumOfDivs(n) > n
lAbundants = [x for x in range(12, 28123) if isabundant(x) == True]
dAbundants = {x:x for x in lAbundants}


if __name__ == "__main__":
    main()