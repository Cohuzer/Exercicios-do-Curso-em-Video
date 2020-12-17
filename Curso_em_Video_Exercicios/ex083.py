equacao = str(input('Digite uma equação: '))
equacao_split = list()
for i in range(len(equacao)):
    equacao_split.append(equacao[i])
parenteses = equacao_split.count('(') + equacao_split.count(')')
count_parentese = 0
ultimo_parenteses = 0

for c, i in enumerate(equacao_split):
    if i == '(':
        count_parentese += 1
        ultimo_parenteses = c
    elif i == ')':
        count_parentese -= 1
        if count_parentese < 0:
            print(f'Houve um erro de construção da formula (parenteses) na {c + 1}° posição, parentese ) a mais')
if count_parentese != 0:
    print(f'Houve um erro na formula, um parentese extra aberto na {ultimo_parenteses + 1}° posição')
else:
    print('A formula esta correta!')
