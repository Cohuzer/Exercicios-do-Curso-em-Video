from random import randint
senha = []
senhas = []

print('-=' * 20)
print('                MEGA SENA')
print('-=' * 20)

quantidade = int(input('Quantos jogos você deseja? '))

for h in range(quantidade):
    for i in range(6):
        senha.append(randint(0, 60))
    for i in senha:
        if senha.count(i) > 1:
            senha[senha.index(i)] = randint(0, 60)
    senhas.append(senha[:])
    senha.clear()

print('-=' * 5, F'CRIANDO {quantidade} JOGOS', '=-' * 5)
for i in range(len(senhas)):
    print(senhas[i])
