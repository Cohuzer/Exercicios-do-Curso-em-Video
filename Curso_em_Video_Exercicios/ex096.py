def area(lar, com):
    return lar * com
print('''
>----------------------------------------------------------<
                  ~CONTROLE DE TERRENO~
>----------------------------------------------------------<
''')
while True:
    lar = float(input('Largura (m): '))
    com = float(input('Comprimento (m): '))
    print(f'A área do retangulo é {area(lar, com)} m^2')
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break
