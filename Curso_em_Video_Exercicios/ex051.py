#ler o primeiro termo e a razão de um progressão aritimética. No final mostre os primeiros 10 termos na msm
print('\033[1;32m{:=^20}'.format('PA'))
v = int(input('VALOR BASE DA PROGRESSÃO: '))
r = int(input('VALOR DA RAZÃO DA PROGRESSÃO: '))
s = v
decimo = v + (10 - 1) * r
for c in range(v, decimo + r, r):
    print('{}'.format(c), end = ' -> ')
print('END')
