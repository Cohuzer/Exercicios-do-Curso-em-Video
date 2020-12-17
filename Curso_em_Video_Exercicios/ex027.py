#Ler o nome de uma pessoa e em seguida dizer qual o primeiro e qual o ultimo nome dela separadamente
n = str(input('Diga um nome completo: '))
n1 = n.split()
print('O primeiro nome dessa pessoa é {}\nO último nome é {}'.format(n1[0], n1[len(n1) - 1]))
