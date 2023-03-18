num = int(input('Digite um número de 0 à 10: '))
print('A tabuada de {} é:'.format(num))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, c * num))
