nota1 = nota2 = request = 0
aluno = list()
boletim = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('Insira a Primeira nota: '))
    nota2 = float(input('Insira a Segunda nota: '))
    aluno = [nome, nota1, nota2]
    boletim.append(aluno[:])
    resposta = input('Quer continuar? [S/N]: ')
    if resposta in 'Nn':
        break
    aluno.clear()
print('-='*20)
print(f'Num.-   Aluno -             Média: ')
print('=-'*20)
for i in range(len(boletim)):
    print(f'{i + 1: <10}{boletim[i][0]: <10}{round(((boletim[i][1] + boletim[i][2])/2), 2): >10}')
print('--'*20)

while True:
    request = int(input('Você deseja ver a nota individual de qual aluno? [Negativos para parada]: '))
    if request < 0:
        break
    else:
        print(f'Individualidade: {[boletim[request - 1]]}')
