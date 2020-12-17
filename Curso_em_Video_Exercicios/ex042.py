#Desafio 35 + colocar se o triangulo é Isoceles, Equilatero ou Escaleno
print('\033[1;34m-=' * 20)
a = float(input('\033[1;34mQual o valor da primeira reta? '))
b = float(input('\033[1;34mQual o valor da segunda reta? '))
c = float(input('\033[1;34mQual o valor da terceira reta? '))
print('\033[1;34m-='*20)
if (b - c) < a < b + c or (a - c) < b < a + c or (a - b) < c < a + b:
    print('\033[1;32mÉ possivel fazer um triangulo com estas retas!')
    if a == b == c:
        print('\033[1;32mO triangulo feito com essas retas é EQUILATERO')
    elif a == b or b == c or c == a:
        print('\033[1;32mO triangulo feito com essas retas é ISOCELES')
    elif a != b and b != c and c != a:
        print('\033[1;32mO triangulo feito com essas retas é ESCALENO')
else:
    print('\033[1;31mNão é possivel fazer um triangulo com essas retas!')
