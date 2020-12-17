#tupla com numeros por extenso de 0 a20-- teclado digita um número e a vc o mostra escrito por extenso
lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    i = int(input('\033[1;33mDigite um número entre 0 e 20: '))
    if i >= 0 and i <= 20:
        print(f'\033[1;34mVocê digitou o número {lista[i]}')
        break
    else:
        print('\033[1;31mOpção inválida, tente novamente.', end=' ')
