numeros = list()
index_maior = list()
index_menor = list()
maior = 0
menor = 0
for i in range (0, 5):
    numeros.append(float(input('Digite um número: ')))

maior = max(numeros)
menor = min(numeros)

for v in numeros:
    if v == maior:
        index_maior.append(v)
    elif v == menor:
        index_menor.append(v)

print(f'O maior valor digitado foi {maior}, digitado pela primeira vez nas posições {index_maior}')
print(f'O menor valor digitado foi {menor}, digitado a primeira vez nas posições {index_menor}')
