print('Digite 4 valores:')
valores = int(input('VALOR 1: ')), int(input('VALOR 2: ')), int(input('VALOR 3: ')), int(input('VALOR 4: '))
if valores.count(9) > 1:
    print(f'O valor 9 apareceu {valores.count(9)} vezes.')
elif valores.count(9) == 1:
    print(f'O valor 9 apareceu {valores.count(9)} vez.')
else:
    print(f'O valor 9 não foi digitado.')
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posição {valores.index(3) + 1}.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares foram: ', end='')
for par in valores:
    if par % 2 == 0:
        print(par, end=' ')
