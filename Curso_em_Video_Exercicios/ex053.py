f = str(input('ESCREVA UMA FRASE: ')).strip().upper().replace(' ', '')
fi = f[::-1]
print(fi)
if f == fi:
    print('ESTA FRASE É UM PALÍNDROMO!')
else:
    print('ESTA FRASE NÃO É UM PALÍNDROMO')
