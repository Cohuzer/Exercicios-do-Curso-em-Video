#Programa que lê números reais e indica a parte inteira deles (math)
from math import trunc
n = float(input('Me diga um número real: '))
print('A parte inteira de {} corresponde a {}'.format(n, trunc(n)))
