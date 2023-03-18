# MEU JEITO
valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    for posi, valor in enumerate(valores):
        if valores.count(valor) > 1:
            valores.pop(posi)
            print('Valor já adicionado anteriormente!')
    while True:
        continuar = str(input('Deseja continuar o programa? ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('=' * 40)
valores.sort()
print(f'Valores digitados: {valores}')
print()
print()

# OUTRO JEITO
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    r = str(input('Quer continuar? [S/N]')).strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
