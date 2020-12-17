numeros = list()
resposta = 'S'
par = list()
impar = list()
while resposta != 'N':
    numeros.append(float(input('Insira um número: ')))
    resposta = str(input('Quer continuar? [S/N]: ')).upper()

for i in numeros:
    if i%2 == 0:
        par.append(i)
    if i%2 != 0:
        impar.append(i)

print('A lista com todos os números:', numeros)
print('A lista com os números pares:', par)
print('A lista com os números impares:', impar)
