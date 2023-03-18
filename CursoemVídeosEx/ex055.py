maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))
