#ler varios números; mostre a média; diga o maior e o menor; programa pergunta se o usuario qr continuar
resp = 'batata'
n = int(input('\033[1;32mDIGA UM NÚMERO: '))
maior = n
menor = n
while resp not in 'N':
    n = int(input('\033[1;32mDIGA UM NÚMERO: '))
    if n < menor:
        menor = n
    if maior < n:
        maior = n
    resp = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
print('\n\033[1;31m{} FOI O MAIOR NÚMERO DIGITADO\n{} FOI O MENOR NÚMERO DIGITADO'.format(maior, menor))
