# MEU JEITO
from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()
for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}.')               # ATÉ ONDE EU CONSEGUI(SEM COLOCAR EM ORDEM)
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{" RANKING ":=^30}')
for i, v in enumerate(ranking):
    print(f"{f'{i + 1}° lugar: {v[0]} com {v[1]}.':^30}")
    sleep(1)
print()
print()
# JEITO FEITO PELO CURSO
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 15)
print(f'{"< RANKING >":-^30}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{f'{i + 1}° lugar: {v[0]} com {v[1]}.':^30}")
    sleep(1)
