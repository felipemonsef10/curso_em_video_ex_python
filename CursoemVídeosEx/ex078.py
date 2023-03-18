# MEU JEITO
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print('-=' * 21)
print(f'VALORES DIGITADOS: {valores}')
for f in range(1):
    print(f'O menor número da lista é o {min(valores)} nas posições ', end='')
    for posi, num in enumerate(valores):
        if sorted(valores)[0] == num:
            print(posi, end='... ')
    print(f'\nO maior número da lista é o {max(valores)} nas posições ', end='')
    for posi, num in enumerate(valores):
        if sorted(valores)[-1] == num:
            print(posi, end='... ')
print()
print()
# OUTRO JEITO
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < mai:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
