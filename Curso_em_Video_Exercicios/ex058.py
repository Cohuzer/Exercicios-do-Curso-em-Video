import random
n = int(random.randint(0, 100))
print('\033[1;33m{: ^60}'.format(' QUAL O NÚMERO? '))
print('\033[1;34m{:=^60}'.format('INSTRUÇÕES DO JOGO'))
print('Eu tenho um número entre 1 e 100 e você tenta adivinhar qual é\nVocê começa com 100 pontos, mas para cada erro você perde 10\nSe você chegar a zero, eu ganho, se você acertar antes disso, você ganha!')
print('{:=^60}'.format('='))
while True:
    p = int(100)
    print('\033[1;33m-=' * 30)
    r = int(input('{:_^60}'.format('QUAL SEU PALPITE?')))
    print('=' * 60)
    if n == r:
        print('\033[7;47m{: ^60}'.format('VOCÊ ACERTOU DE PRIMEIRA, GANHOU COM 100 PONTOS!'))
    else:
        p -= 10
    while r != n or p > 0:
         if r > n:
            print('\033[1;31m{: ^60}'.format('Você esta com {} pontos'.format(p)))
            p = p - 10
            r = int(input('\033[1;31m{: ^60}'.format('MUITO ALTO, TENTE NOVAMENTE: ')))
         elif r < n:
            print('\033[1;31m{: ^60}'.format('Você esta com {} pontos'.format(p)))
            p = p - 10
            r = int(input('\033[1;31m{: ^60}'.format('MUITO BAIXO, TENTE NOVAMENTE: ')))
         if r == n:
            break
         if p <= 0 or p == 0:
            break
    if r == n:
        print('\033[1;32m{: ^60}'.format('VOCÊ GANHOU COM {} PONTOS!'.format(p)))
    elif p <= 0 or p ==0:
        print('\033[1;35m{: ^60}'.format('VOCÊ PERDEU, SEUS PONTOS CHEGARAM A ZERO!'))
        print(f"         O NÚMERO ERA {n}, MAIS SORTE NA PRÓXIMA VEZ!")
    resp = str(input('\033[1;34mDESEJA JOGAR DENOVO? [S/N]'))
    if resp in 'Nn':
        print('END GAME')
        break
    else:
        print('Lets Bora')