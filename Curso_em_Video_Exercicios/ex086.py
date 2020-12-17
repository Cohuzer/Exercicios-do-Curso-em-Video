matriz = [[], [], []]
pares = soma_3 = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Insira o valor da coordenada ({i}, {j}): ')))
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5}]', end=' ')
    print()

