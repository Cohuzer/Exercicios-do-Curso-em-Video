#Soma entre os números impares multiplo de 3 q estão entre 1 e 500
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} valores é {}'.format(cont, s))
