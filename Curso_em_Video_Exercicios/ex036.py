#Aprovar um emrpesimo bancario para compra de uma casa
#O programa pergunta o valor da casa, o salario do comprador e em qnts anos ele qr pagar
#Calcule a prestação mensal sabendo q ela n pode execeder 30% do salário, se não é negada
meses = float
prestacao = float
valor = float(input('\033[1;31mQual o valor do emprestimo? '))
salario = float(input('\033[1;31mQual o valor do seu salário? '))
anos = int(input('\033[1;31mEm quantos anos você pretende pagar? '))
meses = anos * 12
prestacao = valor / meses
if prestacao < salario * 0.3:
    print('\033[1;34mSeu imprestimo foi aprovado! Cada prestação será de {:.2f}'.format(prestacao))
else:
    print('\033[4;31mSeu imprestimo foi negado! Você teria que pagar {:.2f} mensalmente, que é maior que 30% do seu salário'.format(prestacao))
