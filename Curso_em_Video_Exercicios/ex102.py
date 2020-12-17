def fatorial(numero, show=False):
    soma = 1
    numero += 1
    if show:
        for i in range(1, numero):
            print(f'{i} X ', end='')
            if i == numero - 1:
                print(f'{i} = ', end='')
            soma *= i
        print(soma)
        return soma
    else:
        for i in range(1, numero):
            soma *= i
        print(soma)
        return soma

entrada = int(input('Número a ser fatorado: '))
print(f'A fatorial de {entrada} é {fatorial(entrada)}')
print('-*'*20)
print(f'A fatorial de {entrada} é {fatorial(entrada, show=True)}')
