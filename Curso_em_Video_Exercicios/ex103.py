def ficha(nome=None, gols=None):
    dicionario = dict()
    if nome == None:
        nome = '<Não catalogado>'
    if gols == None:
        gols = '<Não catalogado>'
    dicionario[nome] = gols
    return dicionario


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Gols do jogador: ')).strip()

if gols.isnumeric():
    gols = int(gols)
else:
    gols = None

if nome == '':
    nome = None

dicionario = ficha(nome, gols)

for i in dicionario.keys():
    for j in dicionario.values():
        print(f'O jogador {i} fez {j} gol(s) no campeonato')
