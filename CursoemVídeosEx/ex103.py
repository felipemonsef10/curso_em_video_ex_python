def ficha(j='', gols=''):
    if not gols.isnumeric():
        if j == '':
            return f'O jogador <desconhecido> fez 0 gol(s) no campeonato.'
        else:
            return f'O jogador {j} fez 0 gol(s) no campeonato.'
    else:
        if j == '':
            return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.'
        else:
            return f'O jogador {j} fez {gols} gol(s) no campeonato.'


player = str(input('Nome do jogador: ').strip())
goals = str(input('Quantidade de gols: ').strip())
print(ficha(player, goals))
