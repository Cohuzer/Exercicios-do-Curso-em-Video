# Calculador de Média 5> Reprovado, 5 - 6.9 recuperação, 7< Aprovado
m = float
print('\033[1;34m-=' * 20)
n = str(input('NOME DO ALUNO ANALISADO: ')).strip()
print('-=' * 20)
b1 = int(input('NOTA DO 1° BIMESTRE [0-100]: '))
b2 = int(input('NOTA DO 2° BIMESTRE [0-100]: '))
b3 = int(input('NOTA DO 3° BIMESTRE [0-100]: '))
b4 = int(input('NOTA DO 4° BIMESTRE [0-100]: '))
print('-=' * 19,'-=\033[m')
m = (b1 + b2 + b3 + b4) / 4
if m <= 50:
    print('\033[1;31mA média de {} foi {}, ele esta reprovado! Seu desempenho é F'.format(n, m))
elif m > 50 and m <= 70:
    print('\033[1;31mA média de {} foi {}, ele está de recuperação! Seu desempenho é E'.format(n, m))
elif m > 70 and m <= 80:
    print('\033[1;32mA média de {} foi {}, ele está aprovado! Seu desempenho é D'.format(n, m))
elif m > 80 and m <= 90:
    print('\033[1;32mA média de {} foi {}, ele está aprovado! Seu desempenho é C'.format(n, m))
elif m > 90 and m < 100:
    print('\033[1;33mA média de {} foi {}, ele está aprovadissimo! Seu desempenho foi A!'.format(n, m))
elif m == 100:
    print('\033[1;32mA média de {} foi 100!!! ele está mais do que aprovadissimo! Seu desempenho foi o maior, SS!'.format(n))
else:
    print('\033[1;31m!!HOUVE ALGO DE ERRADO COM AS NOTAS COMPUTADAS!!')
