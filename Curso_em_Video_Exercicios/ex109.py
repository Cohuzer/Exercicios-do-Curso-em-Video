import moeda

num = 100
por = 40

print(f'Aumentar = {moeda.aumentar(num, por, sit=True)};\n'
      f'Diminuir = {moeda.diminuir(num, por)};\n'
      f'Dobro = {moeda.dobro(num)};\n'
      f'Metade = {moeda.metade(num, sit=True)}.')
