dic = dict()
dic['Nome'] = str(input('Nome do Jogador: '))
qnt = int(input('Quantas partidas foram jogadas por ele: '))
dic['Gols em cada jogo'] = []
total = int()
for i in range(qnt):
    dic['Gols em cada jogo'].append(int(input(f'Quantos jogos foram marcados na {i + 1}° partida? ')))
    total += dic['Gols em cada jogo'][i]
dic['Total de Gols'] = total
print('-='*30)

for i in dic.keys():
    print(f'O campo {i} tem o valor {dic[i]}')
print('-='*30)

for i in range(len(dic['Gols em cada jogo'])):
    print(f'     => Na partida {i + 1} o jogador fez {dic["Gols em cada jogo"][i]} Gols')
