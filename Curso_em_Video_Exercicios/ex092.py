from datetime import datetime
dic = dict()
dic['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dic['Idade'] = datetime.today().year - nasc
dic['CPTS'] = int(input('Carteira de Trabalho [0 para inexistente]: '))
if dic['CPTS'] != 0:
    dic['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dic['Salário'] = float(input('Salário: R$'))
    dic['Aposentadoria'] = dic['Idade'] + ((dic['Ano de Contratação'] + 35) - datetime.today().year)
print()

for i in dic.keys():
    print(f'O seu {i} é {dic[i]}')
