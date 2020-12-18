def voto(nasc):
    from datetime import date
    hoje = date.today().year
    idade = hoje - nasc
    if 18 <= idade < 65:
        situacao = "Obrigatorio"
    elif idade > 65 or 16 <= idade < 18:
        situacao = "Opicional"
    else:
        situacao = "Negado"
    return [idade, situacao]


nasc = int(input('Insira seu ano de nascimento: '))
votos = voto(nasc)
print(f'Com {votos[0]} anos a situação do seu voto é {votos[1]}')
