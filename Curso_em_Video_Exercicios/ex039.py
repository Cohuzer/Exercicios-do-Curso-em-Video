#Faça um programa q leia o ano de nascimento de um jovem e diga: 1-Se ele ainda deve se alistar 2- Se esta na hr certa de se alistar
# Ou se ja passou da hr de se alistar, além de mostrar o tempo que falta pro prazo
from datetime import date
s = str(input('\033[1;35mQUAL SEU SEXO [M/F]: ')).upper().strip()
if s == 'M':
    a = int(input('\033[1;36mEm que ano você nasceu? '))
    b = date.today().year
    i = (a - b) * -1
    if i == 18:
        print('Esta na hora certa de se alistar, você tem {} anos hoje!')
    elif i < 18:
        print('Você ainda vai se alistar em {} anos, você tem {} anos hoje, seu alistamento será em {}!'.format((i - 18) * -1, b - a, a + 18))
    else:
        print('Você já passou do tempo de se alistar em {} anos, você tem {} anos hoje, seu alistamento foi em {}!'.format((i - 18), b - a , a + 18))
else:
    print('Você não é obrigada a se alistar!')
