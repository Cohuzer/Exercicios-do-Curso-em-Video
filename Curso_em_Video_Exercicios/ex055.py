#Ler o peso de 5 pessoas e diga o maior e o menor
m = 0
n = 1000000
for c in range(1, 6):
    p = float(input('PESO DA {}° PESSOA: '.format(c)))
    if p > m:
        m = p
    if p < n:
        n = p
print('O maior peso foi {}Kg e o menor peso foi {}Kg'.format(m, n))
