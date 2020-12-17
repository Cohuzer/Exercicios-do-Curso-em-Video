#Par ou Impar- para qnd o jogador perder e mostra o tanto de vitoria consecutivas
from random import randint
c = 0
while True:
    print('\033[1;33m-' * 30)
    n = int(input('ESCOLHA UM NÚMERO: '))
    e = str(input('PAR OU IMPAR? ')).strip().upper()[0]
    print('-' * 30)
    j = randint(0, 10)
    if e == 'P':
        if (n + j) % 2 == 0:
            c += 1
            print(f'VOCÊ GANHOU!\nEU ESCOLHI {j} E VOCÊ {n}')
        elif (n + j) % 2 != 0:
            break
    elif e == 'I':
        if (n + j) % 2 == 0:
            break
        elif (n + j) % 2 != 0:
            c += 1
            print(f'VOCÊ GANHOU!\nEU ESCOLHI {j} E VOCÊ {n}')
    elif e not in 'PI':
        print('\033[1;31mOPÇÃO INVALIDA, TENTE DENOVO!')
print(f'\033[1;31mGAME OVER!\nEU ESCOLHI {j} E VOCÊ {n}\nVOCÊ FEZ UMA SEQUENCIA DE {c} PONTOS!')
