def ficha(nome=None, gols=None):
    dicionario = dict()
    if nome != None and gols != None:
        dicionario[f'{nome}'] = gols
    elif nome == None and gols != None:
        dicionario['<Não catalogado>'] = gols
    elif nome != None and gols == None:
        dicionario[f'{nome}'] = '<Não catalogado>'
    return dicionario

nome = str(input('Nome do jogador: '))
gols = int(input('Gols do jogador: '))
dicionario = ficha(nome, gols)
for i in dicionario.keys():
    for j in dicionario.values():
        print(f'O jogador {i} fez {j} gols')
