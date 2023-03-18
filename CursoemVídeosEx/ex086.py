# MEU JEITO
total = []
linha1 = []
linha2 = []
linha3 = []
s = 0
while True:
    for c in range(0, 3):
        linha1.append(int(input(f'Digite um valor para [0, {c}]: ')))
    for c in range(0, 3):
        linha2.append(int(input(f'Digite um valor para [1, {c}]: ')))
    for c in range(0, 3):
        linha3.append(int(input(f'Digite um valor para [2, {c}]: ')))
    total.append(linha1)
    total.append(linha2)
    total.append(linha3)
    contador = 0
    print('-=' * 35)
    for c in range(0, 3):
        print(f'[ {total[contador][c]:^4}]', end='')
    contador += 1
    print()
    for c in range(0, 3):
        print(f'[ {total[contador][c]:^4}]', end='')
    contador += 1
    print()
    for c in range(0, 3):
        print(f'[ {total[contador][c]:^4}]', end='')
    print()
    s += 9
    print('-=' * 35)
    if s == 9:
        break
print()
# OUTRO JEITO
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}', end='')
    print()
