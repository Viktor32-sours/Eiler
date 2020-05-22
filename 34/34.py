"""
Задача 34
Факториалы цифр
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
Ответ: 40730
"""
from math import factorial
  

def sum_fact(n):
    str_n = list(str(n))
    sum_f = 0
    for elem in str_n:
        sum_f += factorial(int(elem))
    return sum_f


def main():
    # list_res = set()
    # for k in range(1, 4):
    #     # list_res = set()
    #     for item in combinations_with_replacement('0123456789', k):
    #         ls = list(item)
    #         tmp = "".join(ls)
    #         print(tmp)
        
    #         temp = int(tmp)
    #         if sum_fact(temp) == temp:
    #             list_res.add(temp)
    list_res = set()
    for i in range(1,500000):
        if sum_fact(i) == i:
            list_res.add(i)
    print(sum(list(list_res))- 3)

if __name__ == "__main__":
    main()