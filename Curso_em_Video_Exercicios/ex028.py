#Pragrama que faça o computador 'pensar' em um número entre 0 e 5 e peça para o usuario tentar descobrir o número escolhido pelo
#computador o programa deve escrever na tela se o usuario acertou ou errou
import random
import time
n = random.randint(0, 5)
r = str(input('\033[1;30;43mQual número você acha que é?\033[m')).strip()
r = int(r)
time.sleep(2)
if n == r:
    print('\033[1;34mVOCÊ ACERTOU! PARABENS, VOCÊ É QUASE UM VIDENTE!\033[m')
else:
    print('\033[1;31VOCÊ ERROU, EU PENSEI EM {}! TENTE NA PRÓXIMA VEZ!\033[m'.format(n))
print('{:=^20}'.format('\033[1;35mEND GAME\033[m'))
