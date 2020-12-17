dicionario = dict()
quantidade = int(input('Quantos alunos serão catalogados? '))
for i in range(quantidade):
    nome = situacao = str
    nota = float
    nome = str(input(f'Insira o nome do {i+1}° aluno: '))
    nota = float(input(f'Insina a média de {nome}: '))
    if nota > 70:
        situacao = 'Aprovado'
    else:
        situacao = 'Não aprovado'
    dicionario[f'{nome}'] = [nota, situacao]
    print('')
for k in dicionario.keys():
    print(f'O nome é {k}\nA média é {dicionario[k][0]}, está {dicionario[k][1]}')
    print('')
