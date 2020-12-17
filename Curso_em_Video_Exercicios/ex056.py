#leia nome idade e sexo de 4 pessoas e mostre: 1- a média de idade 2- o homem mais velho 3-qnts tem menos de 20 anos
from random import randint
m = 0
si = 0
mi = 0
for c in range(1, 5):
    print('\033[1;3{}m-'.format(randint(0, 7)) * 35)
    n = str(input('NOME DA {}° PESSOA A SER ANALIZADA: '.format(c))).strip().upper()
    s = str(input('SEXO [M/F]: ')).strip().upper()
    i = int(input('IDADE: '))
    si += i
    if s == 'M' and i > m:
        hm = n
    if i < 20:
        mi += 1
print('\033[1;3{}mA media de idade entre essas pessoas é {}\nO homem mais velho é {}\n{} pessoas tem menos de 20 anos'.format(randint(0, 7), si/4, hm, mi))
