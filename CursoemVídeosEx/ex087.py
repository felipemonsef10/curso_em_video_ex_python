# EXERCÍCIO APRIMORADO
# MEU JEITO
total = []
linha1 = []
linha2 = []
linha3 = []
s = 0
c1 = 0
maior = 0
par = 0
while True:
    for c in range(0, 3):
        linha1.append(int(input(f'Digite um valor para [0, {c}]: ')))
    for c in range(0, 3):
        linha2.append(int(input(f'Digite um valor para [1, {c}]: ')))
        if c == 0:
            maior = linha2[c]
        elif linha2[c] > maior:
            maior = linha2[c]
    for c in range(0, 3):
        linha3.append(int(input(f'Digite um valor para [2, {c}]: ')))
    total.append(linha1)
    total.append(linha2)
    total.append(linha3)
    contador = 0
    print('-=' * 35)
    for c in range(0, 3):
        print(f'[{total[contador][c]:^5}]', end='')
        if total[contador][c] % 2 == 0:
            par += total[contador][c]
        if c == 2:
            c1 += total[contador][2]
    contador += 1
    print()
    for c in range(0, 3):
        print(f'[{total[contador][c]:^5}]', end='')
        if total[contador][c] % 2 == 0:
            par += total[contador][c]
        if c == 2:
            c1 += total[contador][2]
    contador += 1
    print()
    for c in range(0, 3):
        print(f'[{total[contador][c]:^5}]', end='')
        if total[contador][c] % 2 == 0:
            par += total[contador][c]
        if c == 2:
            c1 += total[contador][2]
    print()
    s += 9
    print('-=' * 35)
    if s == 9:
        break
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {c1}')
print(f'O maior valor da linha 2 é: {maior}')
print()

# OUTRO JEITO
spar = mai = scol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
