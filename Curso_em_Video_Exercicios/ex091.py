from random import randint
posi = 1
dicionario = dict()
escopo = list()
for i in range(4):
    player = randint(1, 7)
    dicionario[f'Player{i+1}'] = [player]

for i in dicionario.keys():
    print(f'{i} tirou {dicionario[i][0]}')
    escopo.append(dicionario[i][0])
escopo.sort()

print('-='*30)
print(f'{"Ranking": ^60}')
print('-='*30)

while True:
    for i in dicionario.keys():
        try:
            if dicionario[i][0] == escopo[-1]:
                print(f'{posi}° -> {i} com {dicionario[i][0]} pontos!')
                escopo.pop()
                posi += 1
        except IndexError:
            break
