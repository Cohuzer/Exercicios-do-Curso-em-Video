def aumentar(numero, porcentagem):
    resultado = numero + ((porcentagem / 100) * numero)
    return resultado


def diminuir(numero, porcentagem):
    resultado = numero - ((porcentagem / 100) * numero)
    return resultado


def dobro(numero):
    resultado = numero * 2
    return resultado


def metade(numero):
    resultado = numero / 2
    return resultado

def moeda(funcao):
    textoFormatado = f'R${funcao:.2f}'.replace('.', ',')
    return textoFormatado
