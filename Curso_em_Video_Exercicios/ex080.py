numeros = list()
numeros_organizados = list()
escopo = 0
i = 0
resposta = 'S'

while resposta != 'N':
    escopo = float(input('Digite um número: '))
    if escopo in numeros:
        print('Número ja adicionado')
    else:
        posicao = 0
        for i in range(len(numeros)):
            if escopo > numeros[i]:
                posicao += 1
        numeros.insert(posicao, escopo)
        print(f'{escopo} foi colocado na posição {posicao}')
    resposta = str(input('Quer continuar?[S/N]: ')).upper()

print(numeros)

#for i in range(len(numeros)):
#    numeros_organizados.append(min(numeros))
#    numeros.pop(numeros.index(min(numeros)))
#print(numeros_organizados)

