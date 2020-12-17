dic = dict()
dic['Nomes'] = []
dic['Idades'] = []
dic['Sexo'] = []
resp = str()
qnt = 1
med = 0
listaF = list()
lista2 = list()

while True:
    escopo = str(input('Nome: ')).capitalize().strip()
    dic['Nomes'].append(escopo)
    dic['Idades'].append(int(input('Idade: ')))
    escopo = str(input('Sexo: ')).upper().strip()
    dic['Sexo'].append(escopo)
    resp = str(input('Quer continuar[S/N]? '))
    if resp in 'Nn':
        break
    else:
        qnt += 1

for i in dic['Idades']:
    med += i
med /= qnt

for i in range(len(dic['Sexo'])):
    if dic['Sexo'][i][0] in 'Ff':
        listaF.append(dic['Nomes'][i])

for i in range(len(dic['Idades'])):
    if dic['Idades'][i] > med:
        lista2.append(dic['Nomes'][i])

print(f'Foram cadastradas {qnt} pessoas')
print(f'A média de idades é {med:.2f}')
print(f'As mulheres são {listaF}')
print(f'As pessoas com idade acima da média são {lista2}')
