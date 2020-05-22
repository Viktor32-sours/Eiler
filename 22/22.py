"""
Задача 22
Используя names.txt (щелкните правой кнопкой мыши и «Сохранить ссылку / цель как ...»), 
текстовый файл размером 46 КБ, содержащий более пяти тысяч имен, начните с сортировки в 
алфавитном порядке. Затем, вычисляя алфавитное значение для каждого имени, умножьте это 
значение на его алфавитную позицию в списке, чтобы получить оценку имени.
Например, когда список отсортирован в алфавитном порядке, COLIN, который стоит 3 + 15 + 12 + 9 + 14 = 53, 
является 938-м именем в списке. Таким образом, COLIN получил бы оценку 938 × 53 = 49714.

Какова общая сумма всех имен в файле?
Ответ: 871198282
"""
def read_file(txt):
    with open(txt, 'r') as f:
        names_list = f.readline()
        return names_list

def summNames(sort_list):
    summList = []
    base = ord('A') - 1
    for i in range(len(sort_list)):
        summWord = 0
        for elem in sort_list[i]: # AARON
            summWord += ord(elem) - base # ord(A) - 64 = 65 - 64 = 1
        summList.append(summWord * (i+1)) # 
    return sum(summList)
       

def main():
    txt = 'p022_names.txt' # "MARY","PATRICIA","LINDA","BARBARA",...
    names_list = read_file(txt).strip().replace('"','').split(",") # MARY,PATRICIA,LINDA,BARBARA, ...
    sort_list = sorted(names_list) # ['AARON', 'ABBEY', 'ABBIE', 'ABBY', 'ABDUL', ...
    print(summNames(sort_list))
    
if __name__ == "__main__":
    main()
#----------------------------------------------
# print sum((i+1)*sum(ord(c)-64 for c in list(n)) for i,n in enumerate(sorted(eval('['+open('p022_names.txt').read()+']'))))