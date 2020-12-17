from time import sleep

def contador(inicio, fim, passo):
    print('< Contando >')
    escopo = inicio
    if passo < 0:
        while True:
            print(f'{escopo}', end=' ')
            sleep(0.5)
            escopo += passo
            if escopo <= fim:
                print(f'Fim')
                break
    elif inicio < fim:
        while True:
            print(f'{escopo}', end=' ')
            sleep(0.5)
            escopo += passo
            if escopo >= fim:
                print(f'Fim')
                break
    elif inicio > fim:
        while True:
            print(f'{escopo}', end=' ')
            sleep(0.5)
            escopo -= passo
            if escopo <= fim:
                print(f'Fim')
                break
    print('-=' * 10)

contador(10, 0, 1)
contador(0, 10, 2)

print('-=' * 30)
entrada1 = int(input('Inicio: '))
entrada2 = int(input('Fim: '))
entrada3 = int(input('Passo: '))
print('-=' * 30)

contador(entrada1, entrada2, entrada3)
