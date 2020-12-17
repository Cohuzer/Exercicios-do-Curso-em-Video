#Leia três números e diga qual é o maior e o menor
menor = int
maior = int
a = int(input('\033[1;33mMe diga um número: \033[m'))
b = int(input('\033[1;33mMe diga mais um número: \033[m'))
c = int(input('\033[1;33mMe diga ainda mais um núemro: \033[m'))
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('\033[4;35m O maior número foi {}\n O menor número foi {}\033[m'.format(maior, menor))
