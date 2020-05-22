# coding: utf-8
# zadacha 11 РќР°РёР±РѕР»СЊС€РµРµ РїСЂРѕРёР·РІРµРґРµРЅРёРµ РІ С‚Р°Р±Р»РёС†Рµ
# 
"""
Произведение этих чисел 26 × 63 × 78 × 14 = 1788696.

Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20, 
расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 '26' 38 40 67 59 54 70 66 18 38 64 70 !
67 26 20 68 02 62 12 20 95 '63' 94 39 63 08 40 91 66 49 94 21 !
24 55 58 05 66 73 99 26 97 17 '78' 78 96 83 14 88 34 89 63 72 !
21 36 23 09 75 00 76 44 20 45 35 '14' 00 61 33 97 34 31 33 95 !
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

Произведение этих чисел 26 × 63 × 78 × 14 = 1788696.

Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20, 
расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?

Максимальное произведение 4-х последовательных чисел: 70600674 Сама последовательность: ['89', '94', '97', '87']
"""
# 1. РѕС‚РєСЂС‹С‚СЊ С‚РµРєСЃС‚РѕРІС‹Р№ С„Р°Р№Р» СЃ С‚Р°Р±Р»РёС†РµР№ 20С…20
# 2. РїСЂРѕС‡РёС‚Р°С‚СЊ С‚Р°Р±Р»РёС†Сѓ Рё Р·Р°РїРёСЃР°С‚СЊ РµС‘ РІ РјР°СЃСЃРёРІ
# 3. Р·Р°РїСѓСЃС‚РёС‚СЊ Р°Р»РіРѕСЂРёС‚Рј РЅР°Р¶РѕР¶РґРµРЅРёСЏ РїСЂРѕРёР·РІРµРґРµРЅРёСЏ
#    4-С… С‡РёСЃРµР», СЂРµР·СѓР»СЊС‚Р°С‚ Р·Р°РїРёСЃР°С‚СЊ РІ РґРІР° СЃРїРёСЃРєР°: СЌР»РµРјРµРЅС‚С‹, СЂРµР·СѓР»СЊС‚Р°С‚
# 4. РёР· РґРІСѓС… СЃРїРёСЃРєРѕРІ СЃРѕР·РґР°С‚СЊ СЃР»РѕРІР°СЂСЊ Рё СЃ РїРѕРјРѕС‰СЊСЋ max РЅР°Р№С‚Рё Рё СЂР°СЃРїРµС‡Р°С‚Р°С‚СЊ 
#    РјР°РєСЃРёРјР°Р»СЊРЅРѕРµ Р·РЅР°С‡РµРЅРёРµ

import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '11.txt')           # добавляем к этому пути имя файла 


def open_read(txt):
    matr = []
    with open(txt, 'r') as f:
        
        for line in f:
            st = line.replace('\n', '').split(' ')
            matr.append(st)
        return matr     
                
        
def goriz(matr):
    
    vol_g = []
    key_g = []
    max_pr = 1
    
    for i in range(len(matr)):
        #print(len(matr))
        
        for j in range(len(matr[i]) - 3):
            proizv = 1
            # Р±РµСЂРµРј СЃСЂРµР· i-РѕР№ СЃС‚СЂРѕРєРё РёР· 4-С… СЌР»-РѕРІ Рё РґРІРёРіР°РµРј РµРіРѕ РІРїСЂР°РІРѕ СЃ С€Р°РіРѕРј 1
            
            for k in matr[i][j:j + 4]:
                proizv *= int(k)
                #print(k, proizv)
            if proizv != 0:             # исключаем последовательности с 0
                #print(k, proizv))
                if proizv > max_pr:
                    max_pr = proizv
                    # РїСЂРё РѕР±РЅРѕРІР»РµРЅРёРё РјР°РєСЃРёРјСѓРјР° РґРѕР±Р°РІР»СЏРµРј РІ СЃРїРёСЃРєРё 
                    # РїСЂРѕРёР·РІРµРґРµРЅРёРµ Рё СЃРѕРѕС‚РІРµС‚СЃС‚РІСѓСЋС‰РёР№ СЃСЂРµР·
                    vol_g.append(max_pr)
                    key_g.append(matr[i][j:j + 3])
                                                                                                                                                                                                                                                                                                                                                                 
    return vol_g[-1], key_g[-1]
    
def vert(matr):
    
    vol_v = []
    key_v = []
    max_pr = 1
    for i in range(len(matr) - 3):
        for j in range(len(matr[i])):
            v = []
            k = 0 
            # СЃРѕР±РёСЂР°РµРј РІ СЃРїРёСЃРѕРє v Р·РЅР°С‡РµРЅРёСЏ i РїРѕ РІРµСЂС‚РёРєР°Р»Рё j РёР· 4-С… СЌР»-РѕРІ
            for k in range(4):
                proizv = 1
                v.append(matr[i+k][j])
            for l in v:
                proizv *= int(l)
                
                if proizv != 0:
                    #print(v,proizv)  # исключаем последовательности с 0
                    if proizv > max_pr:
                        max_pr = proizv
                        vol_v.append(max_pr)
                        key_v.append(v)

    return vol_v[-1], key_v[-1]     
            
def diag_se(matr):
    # последовательность по диагонали(se)
    vol_se = []
    key_se = []
    max_pr = 1
    for i in range(len(matr) - 3):
        for j in range(len(matr[i]) - 3):
            v = []
            k = 0 
            # СЃРѕР±РёСЂР°РµРј РІ СЃРїРёСЃРѕРє v Р·РЅР°С‡РµРЅРёСЏ i РїРѕ РІРµСЂС‚РёРєР°Р»Рё j РёР· 4-С… СЌР»-РѕРІ
            for k in range(4):
                proizv = 1
                v.append(matr[i + k][j + k])
            for l in v:
                proizv *= int(l)
                #print(v, proizv)
                if proizv != 0:            # исключаем последовательности с 0
                    if proizv > max_pr:
                        max_pr = proizv
                        vol_se.append(max_pr)
                        key_se.append(v)
                        
    return vol_se[-1], key_se[-1]   

    
def diag_sw(matr):
    # последовательность по диагонали(sw)
    vol_sw = []
    key_sw = []
    max_pr = 1
    for i in range(len(matr) - 3):
        #print(i)
        for j in range(3, len(matr[i])):
            #print(j)
            v = []
            k = 0
            # СЃРѕР±РёСЂР°РµРј РІ СЃРїРёСЃРѕРє v Р·РЅР°С‡РµРЅРёСЏ i РїРѕ РІРµСЂС‚РёРєР°Р»Рё j РёР· 4-С… СЌР»-РѕРІ
            for k in range(4):
                proizv = 1
                v.append(matr[i + k][j - k])
            for l in v:
                proizv *= int(l)
                #print(v, proizv)
                if proizv != 0:            # исключаем последовательности с 0
                    if proizv > max_pr:
                        max_pr = proizv
                        vol_sw.append(max_pr)
                        key_sw.append(v)

    return vol_sw[-1], key_sw[-1]   


def main():
    
    matr = open_read(file_path)
    dic = dict([(goriz(matr)), (vert(matr)), (diag_se(matr)), (diag_sw(matr))])
    #diag_sw(matr)
    # ~ print(dict.keys(dic))
    # ~ print(dict.values(dic))
    print(f'Максимальное произведение 4-х последовательных чисел: {max(dic)} Сама последовательность: {dic[max(dic)]}' )
    #print(dic)

if __name__ == '__main__':
    main()
