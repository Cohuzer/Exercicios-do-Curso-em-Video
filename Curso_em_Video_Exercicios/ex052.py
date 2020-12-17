#Ler um número inteiro e dizer se é primo ou n é
n = int(input('\033[1;30mDIGITE NÚMERO INTEIRO A SER ANALIZADO: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        s += 1
        print('\033[1;32m{}'.format(c), end = ' ')
    else:
        print('\033[1;31m{}'.format(c), end = ' ')
print(' ')
print('\033[1;30m{} é divisivel por {} números'.format(n, s))
if s == 2:
    print('\033[1;30m{} É primo!'.format(n))
else:
    print('\033[1;30m{} NÃO é primo!'.format(n))
