#Programa pra ler sexo e idade de varias pessoas, o programa prgt se o usuario qr continuar, mostre ao fim:
#a) qnd tem + de 18, b)qnts homens foram cadastrados, c)Mulheres com - de 20
c = h = m = 0
while True:
    print('\033[1;33m-' * 30)
    s = str(input('QUAL SEU SEXO? ')).strip().upper()[0]
    if s not in 'MF':
        s = str(input('\033[1;31mSEXO INVALIDO, TENTE DENOVO: '))
        print('-' * 30)
    i = int(input('\033[1;33mQUAL SUA IDADE? '))
    print('-' * 30)
    if s == 'M':
        h += 1
    elif s == 'F' and i < 20:
        m += 1
    if i > 18:
        c += 1
    if i < 0:
        i = int(input('\033[1;31mIDADE INVALIDA, TENTE DENOVO: '))
        print('-' * 30)
    r = str(input('\033[1;33mQUER CONTINUAR [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
    if r not in 'SN':
        r = str(input('\033[1;31mRESPOSTA INAVLIDA, TENTE DENOVO: ')).strip().upper()[0]
print(f'\033[1;33mFORAM CADASTRADOS {c} PESSOAS COM MAIS DE 18 ANOS\n{h} HOMENS FORAM CADASTRADOS\n{m} MULHERES COM MENOS DE 20 ANOS')
