#Jokenpo
import random
import time
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(0, 2)
print('\033[1;34m-=' * 20)
p = int(input('''QUAL SUA JOGADA?
[ 0 ] PARA PEDRA
[ 1 ] PARA PAPEL
[ 2 ]PARA TESOURA'''))
print('-=' * 20)
time.sleep(1)
print('JÔ')
time.sleep(1)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.5)
if p == pc:
    print('\033[1;33mVOCÊ JOGOU {}'.format(itens[p]))
    print('EU JOGUEI {}'.format(itens[pc]))
    print('NÓS EMPATAMOS!')
elif p == 0 and pc == 2 or p == 1 and pc == 0 or p == 2 and pc == 1:
    print('\033[1;32mVOCÊ JOGOU {}'.format(itens[p]))
    print('EU JOGUEI {}'.format(itens[pc]))
    print('VOCÊ VENCEU!')
elif pc == 0 and p == 2 or pc == 1 and p == 0 or pc == 2 and p == 1:
    print('\033[1;31mVOCÊ JOGOU {}'.format(itens[p]))
    print('EU JOGUEI {}'.format(itens[pc]))
    print('EU VENCI!')
else:
    print('\033[1;31mOPÇÃO NÃO CATALOGADA')
print('\033[1;34mEND GAME')
