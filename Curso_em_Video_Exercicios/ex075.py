#Leia 4 valores |input| e guarde numa tupla-- a) qnts 9 tem b)qnd aparece o 1° 3 c) quais foram os pares
a = int(input('Digite um valor: '))
b = int(input('Digite mais um valor:'))
c = int(input('Digite outro valor: '))
d = int(input('Digite um último valor: '))
par = 0
lista = (a, b, c, d)
for count in range(0, 4):
    if lista[count] % 2 == 0:
        par += 1
print(f'Nestes números temos {lista.count(9)} noves')
print(f'Nestes números o 1° três esta na {lista.index(3) + 1}° posição')
print(f'Nestes números temos {par} números pares')
