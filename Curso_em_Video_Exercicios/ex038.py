#Leia dois números e escreva: 1- O primeiro valor é maior 2- O segundo valor é maior 3- Não existe maior valor, os dois são iguais
n1 = float(input('\033[1;33mDiga um número: '))
n2 = float(input('\033[1;33mDiga outro número: '))
if n1 > n2:
    print('\033[1;31mO primeiro valor, {}, é o maior'.format(n1))
elif n2 > n1:
    print('\033[1;31mO segundo valor, {}, é o maior'.format(n2))
else:
    print('\033[1;34mNão existe valor maior, ambos são iguais')
