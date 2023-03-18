from random import randint
from time import sleep
print('ESTOU PENSANDO EM UM NÚMERO...')
s = 0
num = 0
sort = randint(0, 10)
sleep(2)
while num != sort:
    num = int(input('Tente adivinhar, digite um número: '))
    s += 1
print('Número pensado: {}'.format(sort))
print('Você gastou {} tentativas até acertar.'.format(s))
