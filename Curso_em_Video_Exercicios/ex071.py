#Simule um caixa eletronico- Cédulas de 50, 20, 10, 1
n = int(input('\033[1;33mQUAL O VALOR A SER SACADO? R$ '))
total = n
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            ced = 0
        totalced = 0
        if total == 0:
            break
