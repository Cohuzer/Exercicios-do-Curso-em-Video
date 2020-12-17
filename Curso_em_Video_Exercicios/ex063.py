#Fibonacci
n = int(input('\033[1;34mDIGITOS DA SEQUÊNCIA QUE IRÃO APARECER: '))
v3 = 0
v1 = 1
v2 = 0
c = 0
while c != n:
    print(v3, end = ' -> ')
    v3 = v1 + v2
    v1 = v2
    v2 = v3
    c += 1
print('FIM')