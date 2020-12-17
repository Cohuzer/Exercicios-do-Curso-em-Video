# escreva um numero inteiro e escolha uma base de conversão
# 1 para binarios, 2 para octal e 3 para hexadecidecimal
n = int(input('\033[1;34mME DIGA UM NÚMERO INTEIRO A SER CONVERTIDO: '))
o = int(input('''PARA QUAL BASE NUMÉRICA VOCÊ QUER CONVERTER ESSE NÚMERO:
[1] CONVERTER PARA BINÁRIOS
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL
Qual sua Opção: '''))
if o == 1:
    print('{} convertido para BINÁRIOS é {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31MOPÇÃO INVALIDA!')
