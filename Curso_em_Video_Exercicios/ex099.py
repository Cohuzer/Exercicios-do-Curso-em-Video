from random import randint as rdt
def maior(*num):
    lista = list()
    for n in num:
        lista.append(n)
    return max(lista)

print(f'O maior número é {maior(rdt(0, 100), 12, 213, 31, 312, 3, 5, rdt(0, 1000), rdt(0, 1000))}')
