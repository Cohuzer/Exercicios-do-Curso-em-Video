dic = dict()
dic['Gols em cada jogo'] = []
dic['Partidas jogadas'] = []
dic['Nomes'] = []
dic['Total dos Gols'] = []
total = qnt = int()

print('-='*30)
print(f'{"CADASTRO DOS JOGAODRES": ^60}')
print('-='*30)
while True:
    escopo = str(input('Nome do Jogador: '))
    qnt = int(input('Quantas partidas foram jogadas por ele: '))
    dic['Nomes'].append(escopo)
    dic['Partidas jogadas'].append(qnt)

    for i in range(qnt):

        total += dic['Gols em cada jogo'][i]
    dic['Total de Gols'] = total
    resp = str(input('Quer continuar[S/N]? '))

    if resp in 'Nn':
        break
print('-='*30)

for i in dic.keys():
    print(f'O campo {i} tem o valor {dic[i]}')
print('-='*30)

for i in range(len(dic['Gols em cada jogo'])):
    print(f'     => Na partida {i + 1} o jogador fez {dic["Gols em cada jogo"][i]} Gols')
