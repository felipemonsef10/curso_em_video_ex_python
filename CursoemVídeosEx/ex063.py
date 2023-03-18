print('-=' * 11)
print('SEQUÊNCIA DE FIBONACCI')
print('-='*11)
n = int(input('Quantos termos deseja: '))
s = 0
t1 = 0
t2 = 1
t = 0
while s < n:
    s += 1
    t = t1 + t2
    print(t1, end=' -> ')
    t1 = t2
    t2 = t
print('FIM')
