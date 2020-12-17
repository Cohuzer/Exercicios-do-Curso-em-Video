#Ler o ano de nascimento de 7 pessoas e diga q no final mostre qnts são maiores de idade
import datetime
a = datetime.date.today().year
s = 0
m = 0
for c in range(1, 8):
    n = int(input('ANO DE NASCIMENTO DA {}° PESSOA: '.format(c)))
    if a - n >= 21:
        s += 1
    else:
        m += 1
print('{} pessoas são maiores de idade\n{} pessoas são menores de idade'.format(s, m))
