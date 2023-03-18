from random import randint
from time import sleep
lista = []


def reflle(lst):
    print('-=' * 20)
    print('Sorteando 5 números...')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lst[c], end=' ')
        sleep(0.4)


def sumeven(lst):
    soma = 0
    print('\nOs números pares dessa lista são:')
    for c in range(0, 5):
        if lst[c] % 2 == 0:
            soma += lst[c]
            print(lst[c], end=' ')
            sleep(0.5)
    print('\nA soma desses números é: ')
    print(f'{soma}')
    print('-=' * 20)


reflle(lista)
sumeven(lista)
