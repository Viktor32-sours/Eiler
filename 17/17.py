"""
Задача 17
Счет букв в числительных
Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?


Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.
Ответ: 21124
"""
txt = 'num1.txt'

def read_txt(txt):
    with open(txt, 'r', ) as f:
        for st in f:
            text = f.readlines()
    return text

text = read_txt(txt)
numbers = []

for t in text:
    tt = t.split('\t')
    numbers.append(tt[1].strip())

len_num = 0

for n in numbers:
    nn = n.strip().replace(' ', '').replace('-','')
    ln = list(nn)
    len_num += len(ln)
print(len_num)