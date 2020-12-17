numeros = list()
conta_5 = list()
resposta = 'S'
while resposta != 'N':
    numeros.append(float(input('Insira um número: ')))
    resposta = str(input('Quer continuar? [S/N]: ')).upper()

print(f'Foram digitados {len(numeros)} números')

numeros2 = numeros[:]
numeros2.sort(reverse=True)
print(f'A lista em formato descrescente: {numeros2}')

if 5 in numeros:
    if numeros.count(5) == 1:
        print(f'O valor 5 foi digitado na posição {numeros.index(5)}')
    else:
        for i in range(len(numeros)):
            if numeros[i] == 5:
                conta_5.append(i)
        print(f'O valor 5 foi digitado nas posições {conta_5} ')
else:
    print('O número 5 não foi digitado')
