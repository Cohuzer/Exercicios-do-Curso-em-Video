#Professor quer sortear a ordem de apresentação de um trabalho, 4 alunos (random?)
import random
a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto aluno? '))
list = [a1, a2, a3, a4]
random.shuffle(list)
print('A ordem de alunos a apresentar o trabalho será\n {}'.format(list))
