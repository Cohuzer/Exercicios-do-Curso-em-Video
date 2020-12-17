from random import randint
def sorteia():
    for i in range(5):
        numeros.append(randint(0, 100))
    return numeros

def somaPar(lista):
    soma = 0
    for i in lista:
        if i%2 == 0:
            soma += i
    return soma

numeros = list()
print(f'Números sorteados: {sorteia()}')
print(f'A soma dos números pares é {somaPar(numeros)}')
