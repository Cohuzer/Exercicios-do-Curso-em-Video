#Utilize as funções do Python para tirar/modificar ao menos 7 informações de uma string de entrada

#Entrada
p = input('Digite algo: ')

#Processamento/saida
print('O tipo primitivo de {} é'.format(p), type(p))
print('Só tem espaços? ', p.isspace())
print('É um número? ', p.isnumeric())
print('É alfabético? ', p.isalpha())
print('É alfanumerico? ', p.isalnum())
print('Esta em maiúsculas? ', p.isupper())
print('Esta em minúsculs? ', p.islower())
print('Esta captalizada? ', p.istitle())
