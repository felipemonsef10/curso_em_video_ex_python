while True:
    n = int(input('Digite um número: '))
    s = 0
    if n < 0:
        break
    print(f'A tabuada de {n} é:')
    print('-=' * 8)
    for c in range(10):
        s += 1
        print(f'{n} * {s} = {n * s}')
    print('-=' * 8)
print('Fim')
