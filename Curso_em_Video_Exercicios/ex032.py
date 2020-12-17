#Faça um progarma que leia um ano qualquer e diga se ele é Bissexto
from datetime import date
a = str(input('\033[1;41mQual ano você quer analisar? Se quiser o ano atual digite 0: \033[m')).strip()
a = int(a)
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('\033[1;31mEsse ano é Bissexto!\033[m')
else:
    ('\033[1;31mEsse ano não é Bissexto!\033[m')
