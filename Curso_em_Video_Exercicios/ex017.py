#Programa que lê os catetos e indica a hipotenusa (math)
from math import hypot
n1 = float(input('Me diga o comprimento do cateto oposto: '))
n2 = float(input('Me diga o comprimento do cateto adjascente: '))
h = hypot(n1, n2)
print('A Hipotenusa deste triângulo é {:.2f}°'.format(h))
