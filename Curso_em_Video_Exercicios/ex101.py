from datetime import datetime


def voto(idade):
    if 16 < idade < 70:
        return "Obrigatorio"
    elif idade > 70:
        return "Opicional"
    else:
        return "Negado"


hoje = datetime().today().year
nasc = int(input('Insira seu ano de nascimento: '))
idade = hoje - nasc

print(f'A situação do seu voto é {voto(idade)}')
