tudo = []
temp = dict()
s = 1
while True:
    temp[f'pessoa{s}'] = str(input('Nome: ')).capitalize()
    while True:
        temp['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if temp['sexo'] in 'MF':
            break
    temp['idade'] = int(input('Idade: '))
    tudo.append(temp.copy())
    temp.clear()
    s += 1
    while True:
        continua = str(input('Deseja cadastrar mais pessoas? ')).upper().strip()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print('=' * 65)
print(f'Foram cadastradas {len(tudo)} pessoas.')
i = 0
mulheres = []
for c in range(len(tudo)):
    for k, v in tudo[c].items():
        if k == 'idade':
            i += v
        if k == 'sexo' and v == 'F':
            mulheres.append(tudo[c][f'pessoa{c + 1}'])
print('=' * 65)
print(f'A média de idade do grupo é: {i / len(tudo):.2f} anos')
print('=' * 65)
print('As mulheres cadastradas foram: ', end='')
for p, v in enumerate(mulheres):
    print(f'[{v}]', end='')
print()
print('=' * 65)
print(f'As pessoas com idade acima da média({i / len(tudo):.2f}) são: ', end='')
for c in range(len(tudo)):
    for k, v in tudo[c].items():
        if k == 'idade' and v > i / len(tudo):
            print(f"[{tudo[c][f'pessoa{c + 1}']}]", end=' ')
print()
print('=' * 65)
