"""
Задача 56
Макисмальная сумма цифр
Гугол (10100) - гигантское число: один со ста нулями; 100100 почти невообразимо велико: один с двумястами нулями. Несмотря на их размер, сумма цифр каждого числа равна всего лишь 1.

Рассматривая натуральные числа вида a^b, где a, b < 100, какая встретится максимальная сумма цифр числа?
ответ: 972
"""
def sum_chis(i):
    l_chis = list(str(i))
    return sum(map(int, l_chis))

def main():
    max_sum = 0
    gran = 100
    for a in range(1,gran):
        for b in range(1,gran):
            n = pow(a,b)
            s = sum_chis(n)
            if s > max_sum:
                max_sum = s

    print(max_sum)


if __name__ == "__main__":
    main()