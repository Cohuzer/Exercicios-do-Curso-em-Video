#Tabuada
import random
n = int(input('\033[1;3{}mNÚMERO DA TABUADA DESEJADA: '.format(random.randint(0, 7))))
print('-' * 20)
for c in range(0, 11):
    print('{} X {} = {}'.format(n, c, n * c))
