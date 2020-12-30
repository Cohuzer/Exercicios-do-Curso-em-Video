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
