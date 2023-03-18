lista = []
s = 0
while True:
    n = int(input('Digite um valor: '))
    if s == 0 or n < lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos <= len(lista):
            if n > lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    s += 1
    while True:
        continuar = str(input('Deseja continuar? ')).upper().strip()[0]
        if continuar in 'NS':
            break
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Foram digitados {s} números.')
print(f'Lista ordenada de forma decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado {lista.count(5)} vez(es).')
else:
    print('O valor 5 não foi digitado.')
print('-=' * 30)
