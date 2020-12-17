#Tupla com o top 20 da tabela do campeonato brasileiro-- a) Top 5 b) Last 4 c) lista em ordem alfabteica
#d) em q posição esta a chapecoense
lista = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza-CE', 'Goiás-GO', 'Bahia-BA', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará-CE', 'Cruzeiro-MG', 'Csa-AL', 'Chapecoense', 'Avái-SC')
print('\033[1;34m-=' * 20)
print(f'Os times escalados são {lista}')
print('-=' * 20)
print(f'Os cinco melhores times são {lista[0:6]}')
print('-=' * 20)
print(f'Os quatro piores time são {lista[-4:]}')
print('-=' * 20)
print(sorted(lista))
print('-=' * 20)
print(f'A Chapecoense esta na {lista.index("Chapecoense") + 1}° posição')
