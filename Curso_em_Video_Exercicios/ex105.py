def notas(*n, sit=False):
    """
    => A função analisa as notas de um número não fixo de notas
    :param n: notas dos alunos (Tupla);
    :param sit: Booleano para definir aparição ou não da situação de cada aluno;
    :return: retorna a quantidade de notas cadastradas, maior e menor nota, média, situação e a situação geral.
    """
    lista = [n]
    condicao = []
    respostas = dict()
    soma = 0
    for i in lista[0]:
        soma += i
    quantidade = len(lista[0])
    maior = max(lista[0])
    menor = min(lista[0])
    media = soma / quantidade
    condicaogeral = 'ERRO'

    if sit:
        c = 0
        for i in lista[0]:
            if i < 50:
                condicao.append(f'Aluno {c + 1}-REPROVADO')
            elif i < 70:
                condicao.append(f'Aluno {c + 1}-RECUPERAÇÃO')
            elif i <= 100:
                condicao.append(f'Aluno {c + 1}-APROVADO')
            else:
                condicao.append('<nota fora do range>')
            c += 1
        if -1 < media < 50:
            condicaogeral = f'PÉSSIMA - {media:.2f}'
        elif media < 70:
            condicaogeral = f'RUIM - {media:.2f}'
        elif media < 90:
            condicaogeral = f'ACEITAVEL - {media:.2f}'
        elif media < 100:
            condicaogeral = f'BOA - {media:.2f}'
        else:
            condicaogeral = 'ERRO'

    respostas['Quantidade'] = quantidade
    respostas['Maior Nota'] = maior
    respostas['Menor Nota'] = menor
    respostas['Media das Notas'] = f'{media:.2f}'
    if sit:
        respostas['Condição'] = condicao
        respostas['Condição Geral'] = condicaogeral

    return respostas


print(notas(23, 85, 65, 25, 98, 2.1, 32.1, 90.4, 75, 65, 42, 32, 13, 2, 23, 56, 67, 89, 57, 87, 87, 99, 100, sit=True))
