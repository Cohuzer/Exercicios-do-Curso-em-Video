#Exercicio 64 com break
c = n = cont = 0
while True:
    n = int(input('DIGITE UM NÚMERO [999 PARA PARAR]: '))
    if n == 999:
        break
    c += n
    cont += 1
print(f'FORAM DIGITADOS {cont} NÚMEROS E A SOMA DELES É {c}')
