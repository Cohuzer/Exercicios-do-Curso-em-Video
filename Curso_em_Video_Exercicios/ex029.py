#Programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado e
# que a multa vai custar 7 reais por Km acima do limite
v = str(input('\033[1;31mVelocidade do carro:\033[m ')).strip()
v = float(v)
m = int
if v >= 80:
    print('\033[1;34mVocê será multado!\033[m')
    m = (v - 80) * 7
    print('\033[1;34mO valor da multa será R${:.2f}\033[m'.format(m))
else:
    print('\033[1;33mTenha um bom dia, dirija com segurança!\033[m')
print('\033[1;36;41mTHIS IS THE END\033[m')
