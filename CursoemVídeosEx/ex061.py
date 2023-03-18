print('-=' * 8)
print('CALCULANDO UMA PA:')
print('-=' * 8)
a1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
s = 0
print('Os 10 primeiros termos dessa PA são: ', end='')
while s < 10:
    s += 1
    n = a1 + raz
    a1 = n
    print(a1 - raz, end=' ')
