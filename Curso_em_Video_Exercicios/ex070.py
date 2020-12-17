#ler varios nomes e preços de produtos. programa prgt continuidade.
# mostre: a) total gasto b)qnts custam > 1000 c) qual o mais barato
a = b = c = 0
print('\033[1;33m-' * 40)
n = str(input('QUAL PRODUTO VOCÊ IRA ADIQUIRIR? ')).strip().capitalize()
p = float(input(f'QUAL O PREÇO DO {n}? '))
a += p
if p < 1000:
    b += 1
c = p
nc = n
print('-' * 40)
r = str(input('VOCÊ QUER CONTINUAR [S/N]? ')).strip().upper()[0]
print('-' * 40)
if r not in 'SN':
    r = str(input('\033[1;31mTRY AGAIN, VOCÊ QUER CONTINUAR [S/N]? ')).strip().upper()[0]
    print('-' * 40)
if r == 'S':
    while True:
        n = str(input('\033[1;33mQUAL PRODUTO VOCÊ IRA ADIQUIRIR? ')).strip().capitalize()
        p = float(input(f'QUAL O PREÇO DO {n}? '))
        print('-' * 40)
        a += p
        if p < 1000:
            b += 1
        if p < c:
            c = p
            nc = n
        r = str(input('VOCÊ QUER CONTINUAR [S/N]? ')).strip().upper()[0]
        print('-' * 40)
        if r == 'N':
            break
        elif r not in 'SN':
            r = str(input('\033[1;31mTRY AGAIN, QUER CONTINUAR [S/N]? ')).strip().upper()[0]
            print('-' * 40)
print(f'NO TOTAL FORAM GASTOS R${a}\n{b} PRODUTOS CUSTARAM MENOS DE R$1000,00\n{nc} É O PRODUTO MAIS BARATO, ELE CUSTA R${c}')
