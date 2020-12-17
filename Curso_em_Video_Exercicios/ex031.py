#Pergunte ao usuario a distancia de uma viagem em km. calcule o preço da passagem, cobrando 0,50 reais por km para viagens até 200 km
# mais do que isso cobre 45 centavos por km
d = str(input('\033[0;36mQual a distância de sua viagem [km/h]? \033[m')).strip()
d = int(d)
if d < 200:
    v = d * 0.5
    print('\033[1;31mO valor da viagem será R${:.2f}\033[m'.format(v))
else:
    v = d * 0.45
    print('\033[1;31mO valor da sua viagem será R${:.2f}\033[m'.format(v))
