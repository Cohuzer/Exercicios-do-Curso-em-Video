#61 pedindo se o usuario qr continuar, zero para
r = 'k'
while r not in 'N':
    print('\033[1;32m{:=^20}'.format('PA'))
    v = int(input('VALOR BASE DA PROGRESSÃO: '))
    r = int(input('VALOR DA RAZÃO DA PROGRESSÃO: '))
    s = v
    decimo = v + (10 - 1) * r
    while v != decimo + r:
        print('{}'.format(v), end = ' -> ')
        v += r
    print('END')
    r = str(input('VOCÊ DESEJA CONTINUAR [S/N]: ')).strip().upper()
print('{:=^20}'.format('THIS IS THE END'))
