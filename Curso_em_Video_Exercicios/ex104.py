def leiaInt(entrada):
    n = str(input(entrada)).strip()

    while not n.isnumeric():
        print('\033[1;31mERRO! Digite um número inteiro valido!\033[m')
        n = str(input(entrada)).strip()

    n = int(n)
    return n

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
