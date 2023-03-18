num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('O número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2 or tot == 1:
    print('Por isso, {} é um número primo.'.format(num))
else:
    print('Por isso, {} não é um número primo.'.format(num))
