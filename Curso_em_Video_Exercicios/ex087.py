matriz = [[], [], []]
pares = soma_3 = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Insira o valor da coordenada ({i}, {j}): ')))
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5}]', end=' ')
    print()
print('-=' * 20)

for i in range(3):
    for j in range(3):
        if matriz[i][j]%2 == 0:
            pares += matriz[i][j]
for i in range(3):
    soma_3 += matriz[i][2]
print(f'A soma dos números pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma_3}')
print(f'O maior número da segunda linha é {max(matriz[1])}')
