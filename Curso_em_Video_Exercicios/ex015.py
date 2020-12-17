Km = float(input('Quantos Km foram rodados pelo carro? '))
D = int(input('Por quantos dias o carro foi alugado? '))
P = (D * 60) + (Km * 0.15)
print('Andando {:.2f}Km em {} dias, quem alugou o carro devera pagar R${:.2f}'.format(Km, D, P))
