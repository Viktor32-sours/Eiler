#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?
Ответ: 1366
"""
while 1:
	
	n = int(input('Введите степень числа 2: '))
	
	a = str(2**n)
	print ('2 в степени ',n, 'равно ', a)
	
	a = list(a)
	b = sum(map(int, a))
	print('Сумма цифр числа 2 в степени', n, ' равна ',b)
	
