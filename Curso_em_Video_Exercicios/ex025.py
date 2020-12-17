#Ler o nome de uma pessoa e dizer se tem 'SILVA' no nome
n = str(input('Escreva um nome: ')).strip()
print('Este nome tem Silva? {}'.format('Silva' in n.capitalize()))
