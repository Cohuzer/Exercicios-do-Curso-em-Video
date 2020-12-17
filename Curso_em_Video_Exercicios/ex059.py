#Ler dois valores: [1] para somalos, [2] para multiplicar, [3] maior, [4] para novos números, [5] sair
n1 = float(input('\033[1;33mDIGA UM NÚMERO: '))
n2 = float(input('DIGA OUTRO NÚMERO: '))
n = 0
print('-=' * 20)
while n != 5:
    n = int(input('''   \033[1;35m [ 1 ] Somar
    \033[1;34m[ 2 ] Multiplicar
    \033[1;33m[ 3 ] Qual o maior
    \033[1;32m[ 4 ] Novos números
    \033[1;31m[ 5 ] Sair
    \033[1;30mQual sua escolha: '''))
    print('-=' * 20)
    if n == 1:
        print('\033[1;35m{} + {} = {}'.format(n1, n2, n1 + n2))
        print('-=' * 20)
    elif n == 2:
        print('\033[1;34m{} X {} = {}'.format(n1, n2, n1 * n2))
        print('-=' * 20)
    elif n == 3:
        if n1 > n2:
            print('\033[1;33m{} é maior que {}'.format(n1, n2))
            print('-=' * 20)
        elif n2 > n1:
            print('\033[1;33m{} é maior que {}'.format(n2, n1))
            print('-=' * 20)
        else:
            print('\033[1;33m{} e {} são iguais'.format(n1, n2))
            print('-=' * 20)
    elif n == 4:
        n1 = float(input('\033[1;32mDIGA UM NÚMERO: '))
        n2 = float(input('\033[1;32mDIGA OUTRO NÚMERO: '))
        print('-=' * 20)
    elif n == 5:
        print('\033[1;31m{:=^2}'.format('FIM DO PROCESSO'))
    else:
        print('\033[1;31m{:=^2}'.format('ERROR!'))
        print('-=' * 20)
