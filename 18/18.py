"""
Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания составляет 23.

   3
  7 4
 2 4 6
8 5 9 3

То есть, 3 + 7 + 4 + 9 = 23.

Найдите максимальную сумму пути от вершины до основания следующего треугольника:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

Примечание: Так как в данном треугольнике всего 16384 возможных маршрута от вершины до основания,
эту задачу можно решить проверяя каждый из маршрутов. Однако похожая Задача 67 с треугольником, 
состоящим из сотни строк, не решается перебором (brute force) и требует более умного подхода! ;o)
Ответ: 1074
"""

def open_read(txt):
    triangle = []
    with open(txt, 'r') as f:
        for line in f:
            st = line.strip().split(' ')
            triangle.append(st)
        return triangle     

def main():
    txt = '18.txt'
    triangle = open_read(txt)
   
    path = []
    # начинаем снизу пирамиды и движемся вверх
    for i in range(len(triangle)-1,0, -1):

        for y in range(0, len(triangle[i])-1):
            # суммируем каждый элемент следующего ряда с каждым из 
            # соседних нижнего ряда
            sum_l = int(triangle[i-1][y]) + int(triangle[i][y])
            sum_r = int(triangle[i-1][y]) + int(triangle[i][y+1])
            
            # для нахождения максимальной суммы пути
            triangle[i-1][y] = max(sum_l, sum_r) # переписываем значение узла
            # верхнего ряда на максимальную сумму
            
            # для нахождения минимальной суммы пути
            # triangle[i-1][y] = min(sum_l, sum_r)  
                
    
    for line in triangle:
        print(line)
    print(f'Максимальная сумма: {triangle[0][0]}')

if __name__ == "__main__":
    main()