def leiaInt(entrada):
    """
    => A função valida a tipagem, apenas aceitando um inteiro como saida
    :param entrada: frase que ira aparecer na tela
    :return: número inteiro indicado pelo usuario
    """
    n = str(input(entrada)).strip()

    while not n.isnumeric():
        print('\033[1;31mERRO! Digite um número inteiro valido!\033[m')
        n = str(input(entrada)).strip()

    n = int(n)
    return n

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
