#criar 5 números aleatorios, jogar numa tupla e listalos do menor para o maior
from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram {lista}')
print(f'O maior número sorteado foi {max(lista)}')
print(f'O menor número sorteado foi {min(lista)}')
