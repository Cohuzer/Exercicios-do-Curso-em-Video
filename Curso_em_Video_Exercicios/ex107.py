import moeda

num = float(input('Digite um preço R$'))
por = 40

print(f'Aumentar = {moeda.aumentar(num, por)};\n'
      f'Diminuir = {moeda.diminuir(num, por)};\n'
      f'Dobro = {moeda.dobro(num)};\n'
      f'Metade = {moeda.metade(num)}.')
