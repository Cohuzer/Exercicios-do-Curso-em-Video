numeros = list()
escopo = 0
resposta = 'S'

while resposta == 'S':
    escopo = float(input('Insira um número: '))
    if escopo in numeros:
        print('Número já adicionado')
    else:
        numeros.append(escopo)
    resposta = str(input('Deseja continuar [S/N]: ')).upper()

numeros.sort()
print(numeros)
