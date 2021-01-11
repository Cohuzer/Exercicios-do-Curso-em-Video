from typing import Type


def leiaInt(entrada):
    while True:
        try:
            n = int(input(entrada))
        except (ValueError):
            print('\033[31mVALOR INVALIDO! Digite um valor valido\033[m')
        except(TypeError):
            print(f'\033[31mVALOR INVALIDO! Informe um número valido!\033[m')
        except(KeyboardInterrupt):
            print(f'O usuario preferiu não informar esse número!')
            return 0
        else:
            break

    return int(n)

def leiaFloat(entrada):
    while True:
        try:
            n2 = float(input(entrada))
        except (ValueError):
            print('\033[31mVALOR INVALIDO! Digite um valor valido\033[m')
        except(TypeError):
            print(f'\033[31mVALOR INVALIDO! Informe um número valido!\033[m')
        except(KeyboardInterrupt):
            print(f'O usuario preferiu não informar esse número!')
            return 0
        else:
            break
    
    return float(n2)

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
n2 = leiaFloat('Digite um número: ')
print(f'Você digitou o número flutuante {n2}')
