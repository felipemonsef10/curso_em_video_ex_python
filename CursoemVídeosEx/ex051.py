print('=-=' * 8)
print('PROGRESSÃO ARITIMÉTRICA')
print('=-=' * 8)
num = int(input('Primeiro número: '))
raz = int(input('Razão: '))
dt = num + (10 - 1) * raz
print('Os dez primeiros termos dessa PA são:')
for c in range(num, dt + raz, raz):
    print(c, end=' ')
