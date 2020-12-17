#Crie um programa que diga se o nome de uma cidade começa ou n com 'SANTO'
n = str(input('Em que cidade você nasceu: ')).strip()
print('Santo' == n[:5].capitalize())
#d = n.split()
#print('{} começa com Santo? {}'.format(n, 'Santo' in d[0].capitalize()))
