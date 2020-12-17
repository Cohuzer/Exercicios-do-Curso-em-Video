#tupla com palavras (sem acento) -- mostrar para cada palavra suas vogais
lista = ('Zattana', 'Flash Azul', 'Sentinela', 'Hope Summers', 'Saiki Kusuo')
while True:
    for c in lista:
        print(f'Na palavra {c.upper()} temos', end = ' ')
        for letras in c:
            if letras.lower() in 'aeiou':
                print(letras, end=' ')
        print('\n')
    break
