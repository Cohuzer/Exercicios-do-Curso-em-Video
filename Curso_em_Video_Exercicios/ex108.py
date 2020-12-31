import moeda

num = float(input('Digite um preço R$'))
por = 40

print(f'Aumentar = {moeda.moeda(moeda.aumentar(num, por))};\n'
      f'Diminuir = {moeda.moeda(moeda.diminuir(num, por))};\n'
      f'Dobro = {moeda.moeda(moeda.dobro(num))};\n'
      f'Metade = {moeda.moeda(moeda.metade(num))}.')
