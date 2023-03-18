from random import randint
from time import sleep
nmr = randint(0, 5) #Computador pensa em um número
print('=' * 60)
print('Tente adivinhar o número que estou pensando...')
print('=' * 60)
jogador = int(input('Digite um número de 0 à 5: ')) #Jogador tenta adivinhar
print('O número pensando foi...')
sleep(2)
print('{}'.format(nmr))
if jogador == nmr:
    print('Parabéns, você acertou!')
else:
    print('Tente novamente')

