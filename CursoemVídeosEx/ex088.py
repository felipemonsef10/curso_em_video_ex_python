from random import randint
from time import sleep
tot = []
temp = []
print('=' * 40)
print(f'\033[1;31m{"JOGO DA MEGA SENA":^40}\33[m')
print('=' * 40)
qtd = int(input('\033[1;35mNúmero de jogos à serem sorteados: \033[m'))
print('-' * 40)
print(f'\033[1;31m{f"SORTEANDO {qtd} JOGOS...":^40}\033[m')
print('-' * 40)
for c in range(0, qtd):
    s = 0
    while True:
        numsorteados = (randint(1, 60))
        if numsorteados not in temp:
            temp.append(numsorteados)
            s += 1
        if s == 6:
            break
    tot.append(temp[:])
    temp.clear()
    sleep(2)
    print(f'\033[1;40mJOGO {c + 1}: {sorted(tot[c])}\033[m')

# OUTRO JEITO
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 30)
print('       JOGA NA MEGA SENA      ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
