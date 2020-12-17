#escala de IMC
from math import pow
print('\033[1;34m-=' * 20)
p = float(input('\033[1;34mQual seu peso? [Em Kg] '))
a = float(input('\033[1;34mQual sua altura? [Em M] '))
print('\033[1;34m-=' * 20)
IMC = p / pow(a, 2)
if IMC <= 18.5:
    print('\033[1;31mVocê está abaixo do seu peso ideal, cuidado! Seu IMC é {:.2f}'.format(IMC))
elif IMC > 18.5 and IMC <= 25:
    print('\033[1;32mVocê está no seu peso ideal, parabéns! Seu IMC é {:.2f}'.format(IMC))
elif IMC > 25 and IMC <= 30:
    print('\033[1;35mVocê está acima do seu peso ideal, cuidado! Seu IMC é {:.2f}'.format(IMC))
elif IMC > 30 and IMC <= 35:
    print('\033[1;35mVocê está com Obesidade Grau I, cuidado! Seu IMC é {:.2f}'.format(IMC))
elif IMC > 35 and IMC <= 40:
    print('\033[1;33mVocê está com Obesidade Grau II, cuidado! Seu IMC é {:.2f}'.format(IMC))
elif IMC > 40:
    print('\033[1;31mVocê está com Obesidade Mórbida, cuidado! Seu IMC é {:.2f}'.format(IMC))
else:
    print('\033[1;41mALGO DE ERRADO ACONTECEU\033[m')
