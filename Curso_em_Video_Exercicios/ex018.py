#Programa que lê um ângulo e indica seu seno, cosseno e tangente (math)
from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Para um ângulo de {}°\nTem o SENO: {:.2f}°\nTem o COSSENO: {:.2f}°\nTem a TANGENTE: {:.2f}°,'.format(a, s, c, t))
