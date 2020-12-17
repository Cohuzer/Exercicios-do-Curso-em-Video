#Ler uma frase escrita pelo teclado e dizer: 1- Quantas vezes 'A' aparece 2- Em q posição 'A' apareceu primeiro 3- Em q posição 'A' apareceu pela ultima vez
n = str(input('Escreva uma frase: ')).strip().lower()
a = n.count('a')
a1 = n.find('a')
a2 = n.rfind('a')
print('Em {}, A aparece {} vezes\nPrimeiro na {}° letra\nPor último na {}° letra'.format(n, a, a1 + 1, a2 + 1))
