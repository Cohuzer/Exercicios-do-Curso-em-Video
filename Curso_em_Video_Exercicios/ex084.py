pessoa = list()
pessoas = list()
maior = manor = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    elif pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor:
        menor = pessoa[1]
    pessoas.append(pessoa[:])
    resposta = input('Quer continuar? [S/N]: ')
    if resposta in 'Nn':
        break
    pessoa.clear()

print(f'No total {len(pessoas)} pessoas foram analisadas')
print(f'O maior peso foi {maior}Kg, de ', end='')
for i in range(len(pessoas)):
    if pessoas[i][1] == maior:
        print(pessoas[i][0], end=' ')
print(f'\nO menor peso foi {menor}Kg, de ', end='')
for i in range(len(pessoas)):
    if pessoas[i][1] == menor:
        print(pessoas[i][0], end=' ')
