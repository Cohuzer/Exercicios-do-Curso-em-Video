def ficha(nome=None, gols=None):
    dicionario = dict()
    if nome == None:
        nome = '<Não catalogado>'
    if gols == None:
        gols = '<Não catalogado>'
    dicionario[nome] = gols
    return dicionario

nome = str(input('Nome do jogador: '))
gols = int(input('Gols do jogador: '))
dicionario = ficha(nome, gols)

for i in dicionario.keys():
    for j in dicionario.values():
        print(f'O jogador {i} fez {j} gols')
