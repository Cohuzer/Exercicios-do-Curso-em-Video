from random import randint
while True:
    print('\033[01;43m=-'*30)
    print(f'{"A.H.P.- Assistente HELP() em Python": ^60}')
    print('=-'*30)
    funcao = str(input(f'\033[m -> Insira o nome da função/biblioteca: \033[01;{randint(41,47)}m'))
    if funcao.lower() == 'fim':
        break
    print(f'{help(funcao)}')
