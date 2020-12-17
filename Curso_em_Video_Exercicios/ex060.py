c = 1
n1 = 1
n = int(input('\033[1;34mINFORME UM NÚMERO A SER FATORIADO: '))
while c != (n + 1):
    n1 = n1 * c
    c += 1
print('A FATORIAL DE {} ({}!) É {}'.format(n, n, n1))

