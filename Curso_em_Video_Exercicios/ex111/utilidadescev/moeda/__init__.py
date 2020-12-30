def aumentar(numero, porcentagem, sit=False):
    resultado = numero + ((porcentagem / 100) * numero)
    if sit:
        resultadoFormatado = moeda(resultado)
        return resultadoFormatado
    else:
        return resultado


def diminuir(numero, porcentagem, sit=False):
    resultado = numero - ((porcentagem / 100) * numero)
    if sit:
        resultadoFormatado = moeda(resultado)
        return resultadoFormatado
    else:
        return resultado


def dobro(numero, sit=False):
    resultado = numero * 2
    if sit:
        resultadoFormatado = moeda(resultado)
        return resultadoFormatado
    else:
        return resultado


def metade(numero, sit=False):
    resultado = numero / 2
    if sit:
        resultadoFormatado = moeda(resultado)
        return resultadoFormatado
    else:
        return resultado


def moeda(numero):
    textoFormatado = f'R${numero:.2f}'.replace('.', ',')
    return textoFormatado


def resumo(numero, porcentagemAumento, porcentagemDiminuir, sit=False):
    print(f'-=' * 15)
    print(f"{'RESUMO': ^30}")
    print(f'-=' * 15)
    print(f'  >>> Aumentar = {aumentar(numero, porcentagemAumento, sit)};\n'
          f'  >>> Diminuir = {diminuir(numero, porcentagemDiminuir, sit)};\n'
          f'  >>> Dobro = {dobro(numero, sit)};\n'
          f'  >>> Metade = {metade(numero, sit)}')

