#leia o salario de um funcionario e indique seu aumento: acima de 1250 10%, e igual ou inferior 15%
s = float(input('\033[7;30;45mQual o salário? R$ \033[m'))
if s > 1250:
    s = s + (s * 0.10)
    print('\033[1;31mSeu salário com reajuste de 10% será R${:.2f}\033[m'.format(s))
else:
    s = s + (s * 0.15)
    print('\033[1;32mSeu salário com reajuste de 15% será R${:.2f}\033[m'.format(s))
