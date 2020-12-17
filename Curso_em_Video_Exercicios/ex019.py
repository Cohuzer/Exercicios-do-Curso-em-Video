#Sortear um nome dentre 4, ajude o professor (random?)
import random
a1 = str(input('PRIMEIRO ALUNO: '))
a2 = str(input('SEGUNDO ALUNO: '))
a3 = str(input('TERCEIRO ALUNO: '))
a4 = str(input('QUARTO ALUNO: '))
list = [a1, a2, a3, a4]
r = random.choice(list)
print('Quem vai apagar o quadro é ... {}'.format(r))
