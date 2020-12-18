def formatar(frase):
    from random import randint
    tamanho = len(frase) + 4
    print(f'\033[01;{randint(41,47)}m='*tamanho)
    print(f'  {frase}')
    print('='*tamanho)

def AHP():
    from time import sleep
    while True:
        formatar('A.H.P. <-> Assistente HELPY-ME Please')
        funcao = str(input(f'\033[m -> Insira o nome da função/biblioteca: '))
        if funcao.lower() == 'fim':
            formatar('Volte sempre!')
            break
        formatar('Analisando os dados')
        sleep(0.2)
        print(f'{help(funcao)}')

AHP()
