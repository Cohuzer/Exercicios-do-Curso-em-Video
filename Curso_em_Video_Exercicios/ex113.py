def leiaInt(entrada):
    while True:
        try:
            n = int(input(entrada))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mERRO! Digite um valor valido\033[m')
        else:
            break

    return int(n)

def leiaFloat(entrada):
    while True:
        try:
            n2 = float(input(entrada))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mERRO! Digite um valor valido\033[m')
        else:
            break
    
    return float(n2)

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
n2 = leiaFloat('Digite um número: ')
print(f'Você digitou o número flutuante {n2}')
