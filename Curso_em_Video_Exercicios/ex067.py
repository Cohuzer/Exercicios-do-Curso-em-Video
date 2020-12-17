#Tabauada dos números digitados pelo úsuario- para qnd o valor for negativo
while True:
    print('-' * 30)
    n = int(input('QUAL TABUADA VOCÊ DESEJA VER? '))
    print('-' * 30)
    c = 0
    if n < 0:
        break
    while c != 11:
        print(f'{n} X {c} = {n * c}')
        c += 1
print('FIM DO PROCESSO')
