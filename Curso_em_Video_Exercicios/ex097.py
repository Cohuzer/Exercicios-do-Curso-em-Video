def escreva(strix):
    altair = len(strix) + 4
    print('~'* altair)
    print(f'  {strix}')
    print('~'* altair)

entrada = str(input('Entrada: ')).strip()
escreva(entrada)
