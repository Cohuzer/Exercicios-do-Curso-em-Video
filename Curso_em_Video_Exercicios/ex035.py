#leia o comprimento de três retas e diga se elas podem formar um triângulo
print('\033[1;31m-=' * 20)
a = float(input('\033[1;34mQual o valor da primeira reta? '))
b = float(input('\033[1;34mQual o valor da segunda reta? '))
c = float(input('\033[1;34mQual o valor da terceira reta? '))
if (b - c) < a < b + c or (a - c) < b < a + c or (a - b) < c < a + b:
    print('\033[1;32mÉ possivel fazer um triangulo com estas retas!')
else:
    print('\033[1;32mNão é possivel fazer um triangulo com essas retas!')
