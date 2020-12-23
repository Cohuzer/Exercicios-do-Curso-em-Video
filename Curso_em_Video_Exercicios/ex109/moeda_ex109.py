def moeda (n):
    return (f'R${n:.2f}').replace('.', ',')

def aumentar(*n, show=False):
    soma = 0
    for i in n:
        soma += i
        if show:
            soma = moeda(soma)
    return soma

def diminuir(n1, *n, show=False):
    for i in n:
        n1 -= i
        if show:
            n1 = moeda(n1)
    return n1

def dobro(n, show=False):
    dobro = n*2
    if show:
        dobro = moeda(dobro)
    return dobro

def metade(n, show=False):
    metade = n/2
    if show:
        metade = moeda(metade)
    return metade
