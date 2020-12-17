escopo = 0
i = 0
valores = [[], []]

while i != 7:
    escopo = int(input(f'Digite o {i + 1}° valor: '))
    i += 1
    if escopo%2 == 0:
        valores[0].append(escopo)
    else:
        valores[1].append(escopo)

valores[0].sort()
valores[1].sort()
print(f'Números pares: {valores[0]}\nNúmeros impares: {valores[1]}')
