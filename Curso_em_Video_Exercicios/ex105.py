def notas(*n, sit=False):
    lista = [n]
    condicao = []
    respostas = dict()
    soma = 0
    for i in lista[0]:
        soma += i
    quantidade = len(lista[0])
    maior = max(lista[0])
    menor = min(lista[0])
    media = soma/quantidade

    if sit:
        c = 0
        for i in lista[0]:
            if i < 50:
                condicao.append(f'Aluno {c+1}-REPROVADO')
            elif i < 70:
                condicao.append(f'Aluno {c+1}-RECUPERAÇÃO')
            elif i <= 100:
                condicao.append(f'Aluno {c+1}-APROVADO')
            else:
                condicao.append('<nota fora do range>')
            c += 1

    respostas['Quantidade'] = quantidade
    respostas['Maior Nota'] = maior
    respostas['Menor Nota'] = menor
    respostas['Media das Notas'] = media
    if sit:
        respostas['Condição'] = condicao

    return respostas

print(notas(23,85,65,25,98,75,65,42,32,13,2,23,56,67,89,57,87,87,99,100, sit=True))
