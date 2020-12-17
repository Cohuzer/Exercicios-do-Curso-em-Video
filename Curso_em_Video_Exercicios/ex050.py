#Ler 6 numeros inteiros e mostre a soma dqls q são par
s = 0
for c in range(0, 6):
    n = int(input('\033[1;34mNÚMERO A SER ANALISADO: '))
    if n % 2 == 0:
        s += n
print('A soma dos valores pares é {}'.format(s))
