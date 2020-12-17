# A confederação Nacional de Natação precisa ler uma idade e dizer a sua categoria:
# até 9: mirim; até 14: Infantil; até 19: Junior; Até 20: Senior; + q 20: Master
from datetime import date
print('\033[1;34m-='*20)
a = int(input('\033[1;34mQual seu ano de nascimento? '))
a1 = date.today().year
i = a1 - a
print('\033[1;34m-='*20)
if i <= 9 and i > 0:
    print('\033[33mVocê é da categoria Mirim')
elif i > 9 and i <=14:
    print('\033[33mVocê é da categoria Infantil')
elif i > 14 and i <= 19:
    print('\033[32mVocê é da categoria Junior')
elif i == 20:
    print('\033[32mVocê é da categoria Senior')
elif i > 20:
    print('\033[1;31mVocê é da categoria Master')
else:
    print('\033[1;31mALGO DE ERRADO ACONTECEU')
