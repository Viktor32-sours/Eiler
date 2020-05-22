"""
Собственные степени
Сумма 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.
Ответ: 9110846700
"""



def main():
    n = 1000
    summ = 0
    for i in range(1, n + 1):
        a = pow(i,i)
        summ += a

    print(summ)
    print(str(summ)[-10:])



if __name__ == "__main__":
    main()