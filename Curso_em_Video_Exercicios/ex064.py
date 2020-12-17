#Leia varios int; 999 para o progama; mostre os números digitados e a soma deles
n1 = 0
n = 0
c = 0
n1 = int(input('\033[1;33mESCREVA UM NÚMERO INTEIRO FORA 999: '))
while n1 != 999:
    n += n1
    c += 1
    n1 = int(input('\033[1;33mESCREVA UM NÚMERO INTEIRO FORA 999: '))
print('A SOMA DOS {} NÚMEROS É {}'.format(c, n))
