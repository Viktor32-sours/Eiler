"""
Задача 4
Наибольшее произведение-палиндром
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

Ответ: 993х913=906609
"""
def is_palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    
    

def main():
    start = 100
    stop = 1000
    list_palindrom = []
    for i in range(start, stop):
        for j in range(start, stop):
            proizv = i * j
            #print(proizv)
            if is_palindrom(proizv):
                #print(i, j, proizv)
                list_palindrom.append(proizv)
        #sorted(list_palindrom)
    print(max(list_palindrom))

    
if __name__ == "__main__":
    main()
