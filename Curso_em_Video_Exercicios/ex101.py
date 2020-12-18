def voto(nasc):
    from datetime import date
    hoje = date.today().year
    idade = hoje - nasc
    if 16 < idade < 70:
        return [idade, "Obrigatorio"]
    elif idade > 70:
        return [idade, "Opicional"]
    else:
        return [idade, "Negado"]


nasc = int(input('Insira seu ano de nascimento: '))
votos = voto(nasc)
print(f'Com {votos[0]} anos a situação do seu voto é {votos[1]}')
