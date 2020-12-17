#tupla com nome e preço (na sequencia) de produtos -- mostrar uma lista tabular
lista = ('Lápis', 1.50, 'Borracha', 2.00, 'Caneta', 2.50, 'Caderno', 50.00, 'Bolsa', 126.00, 'Apostila', 70.00, 'Tesoura', 4.00)
print('-=' * 20)
print(f'{"LISTA DE PREÇOS": ^40}')
print('-=' * 20)
while True:
    for c in range(0, len(lista), 2):
        c1 = c + 1
        print(f'{lista[c]:.<30} R${lista[c1]:.2f}')
    break
print('-=' * 20)