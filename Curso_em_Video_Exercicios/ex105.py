def notas(*n):
    lista = [n]
    condicao = []
    soma = 0
    for i in lista[0]:
        soma += i
    quantidade = len(lista)
    maior = max(lista)
    menor = min(lista)
    media = soma/quantidade
    for i in lista[0]:
        if i < 50:
            condicao.append(f'Aluno {i+1}-REPROVADO')
        elif i < 70:
            condicao.append(f'Aluno {i+1}-RECUPERAÇÃO')
        elif i <= 100:
            condicao.append(f'Aluno {i+1}-APROVADO')
        else:
            condicao.append('<nota fora do range>')
    respostas = [f'Foram catalogadas {quantidade} notas',
                 f'A maior nota foi {maior}',
                 f'A menor nota foi {menor}',
                 f'A média foi {media}',
                 condicao]
    return respostas

print(notas(23,85,65,25,98,75,65,42,32,13,2,23,56,67,89,57,87,87,99,100))
