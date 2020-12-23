def aumentar(*n):
    soma = 0
    for i in n:
        soma += i
    return soma

def diminuir(n1, *n):
    for i in n:
        n1 -= i
    return n1

def dobro(n):
    return n*2

def metade(n):
    return n/2

#Funções do exercicio 107

def mostraMoeda (n):
    return (f'R${n:.2f}').replace('.', ',')
#Função do exercicio 108