#Leia um número e diga se é par ou impar
n = str(input('\033[1;33mMe diga um número: \033[m'))
n = int(n)
if n % 2 == 0:
    print('\033[1;31mEsse número é par.\033[m')
else:
    print('\033[1;35mEsse número é impar\033[m')
