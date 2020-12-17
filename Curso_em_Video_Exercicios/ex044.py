#Valor a ser pago em um produto: preço normal ou condição de pagamento: A vista dinheiro/cheque -10%
#A vista no cartão-5%; até 2x no cartão preço normal; 3x ou mais no cartão + 20%
print('\033[1;33m-=' * 20)
v = float(input('VALOR DO PRODUTO: R$ '))
print('\033[1;33m-=' * 20)
f = int(input('Forma de pagamento:\n[1] A vista no dinheiro\n[2] A vista no cheque\n[3] A vista no cartão\n[4] 2x no cartão\n[5] 3x ou mais no cartão '))
print('\033[1;33m-=' * 20)
if f == 1 or f == 2:
    print('O valor do produto tera desconto de 10%, ele custará R${:.2f}'.format(v - (v * 0.1)))
elif f == 3:
    print('O valor do produto tera desconto de 5%, ele custara R${:.2f}'.format(v - (v * 0.05)))
elif f == 4:
    print('O valor do produto é mantido normalmente, R${:.2f}, sendo duas parcelas de R${:.2f}'.format(v, v/2))
elif f == 5:
    print('O valor do produto tera acrescimo de 20%, ele custaria R${:.2f}'.formar(v + (v * 0.2)))
else:
    print('\033[1;31mALGO DE ERRADO ACONTECEU')
