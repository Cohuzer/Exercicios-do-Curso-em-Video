def leiaDinheiro(prompt):
    num = str(input(prompt))
    if ',' in num:
        num = num.replace(',', '.')

    while not num.isdecimal() and num.isnumeric():
        num = str(input(f'\033[31mO VALOR "{num}" NÃO É UM NÚMERO, INSIRA UM NÚMERO: \033[m'))
        if ',' in num:
            num = num.replace(',', '.')

    numConvertido = float(num)
    return numConvertido
