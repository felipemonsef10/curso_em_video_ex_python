from random import randint
from time import sleep
print('GERANDO 5 NÚMEROS ALEATÓRIOS...')
sleep(3)
n = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
print('Os números gerados foram: ')
print('')
for c in n:
    print(c)
print('')
# Jeito 1
print(f'O menor valor foi: {sorted(n)[0]} e o maior foi: {sorted(n)[-1]}')
# Jeito 2
print(f'O menor valor foi: {min(n)} e o maior foi: {max(n)}')
