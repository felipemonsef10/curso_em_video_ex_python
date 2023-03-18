from random import choice
print('=' * 20)
print('Vamos jogar jokenpô!')
print('=' * 20)
from time import sleep
print('3, 2, 1 e...')
sleep(3)
jogador = str(input('(ESCREVA COM O CAPSLOK DESLIGADO) Pedra, papel ou tesoura? '))
ped = 'pedra'
pa = 'papel'
te = 'tesoura'
jokenpo = [ped, pa, te]
maq = choice(jokenpo)
if jogador == 'pedra' and maq == pa or jogador == 'papel' and maq == te or jogador == 'tesoura' and maq == ped:
    print('Eu escolho {}. Haha, eu venci!!'.format(maq))
elif jogador == maq:
    print('Eu escolho {}. Deu empate, vamos para outra rodada.'.format(maq))
elif jogador == ped and maq == te or jogador == pa and maq == ped or jogador == te and maq == pa:
    print('Eu escolho {}. Você venceu!'.format(maq))
else:
    print('Essa opção não existe, tente novamente!')
