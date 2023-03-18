# MEU JEITO
nomepeso = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    nomepeso.append(dados[:])
    dados.clear()
    while True:
        continua = str(input('Deseja continuar? ')).upper().strip()[0]
        if continua in 'NS':
            break
    if continua == 'N':
        break
for c in range(0, len(nomepeso)):
    if c == 0:
        maior = menor = nomepeso[c][1]
    else:
        if nomepeso[c][1] > maior:
            maior = nomepeso[c][1]
        elif nomepeso[c][1] < menor:
            menor = nomepeso[c][1]
print(f'O número de pessoas cadastradas é: {len(nomepeso)}')
print(f'As pessoas mais pesadas, pesando {maior}Kg, são: ', end='')
for p in nomepeso:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'As pessoas mais leves, pesando {menor}Kg, são: ', end='')
for p in nomepeso:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
