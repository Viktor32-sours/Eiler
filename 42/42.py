"""
Задача 42
Закодированные треугольные числа
n-ый член последовательности треугольных чисел задается как tn = ½n(n+1). Таким образом, первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Преобразовывая каждую букву в число, соответствующее ее порядковому номеру в алфавите, и складывая эти значения, мы получим числовое значение слова. Для примера, числовое значение слова SKY равно 19 + 11 + 25 = 55 = t10. Если числовое значение слова является треугольным числом, то мы назовем это слово треугольным словом.

Используя words.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), 16 КБ текстовый файл, содержащий около двух тысяч часто используемых английских слов, определите, сколько в нем треугольных слов.
Ответ: 162
"""


def read(txt):
    with open(txt, 'r') as f:
        words = f.read()
        # print(len(words))
        return words

def is_triangl(word, triangl_list):
    word = word.replace('"', '')
    summ = 0
    for char in word:
        summ += int(ord(char)-64)
    if summ in triangl_list:
        # print(word, summ)
        return True
    # print(word, summ)
    return False


def main():
    triangl_list = [int((i+1)*i/2) for i in range(1,30)]
    txt = 'p042_words.txt'
    words = read(txt).split(',')
    
    s = 0
    for word in words:
        Flag = is_triangl(word, triangl_list)
        if Flag:
            s += 1
    print(s)
    
if __name__ == "__main__":
    main()
    