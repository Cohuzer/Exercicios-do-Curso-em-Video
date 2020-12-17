#Leia o sexo de uma pessoa [M/F], se o valor estiver errado pessa pra digitar dnv
sx = str(input('\033[1;34mINFORME SEU SEXO: ')).strip().upper()[0]
while sx not in 'MF':
    sx = str(input('Informação invalidada. Infrome seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sx))
