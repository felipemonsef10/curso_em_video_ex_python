dados = dict()
gols = []
s = 0
dados['jogador'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Partidas jogadas por {dados["jogador"]}: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantidade de gols da partida {c + 1}: ')))
    dados['gols'] = gols
    s += dados['gols'][c]
    dados['totalgols'] = s
gol = ''
print('=' * 30)
for k, v in dados.items():
    if k == 'jogador':
        print(f'Nome do jogador: {v}')
    if k == 'gols':
        for i, g in enumerate(gols):
            if g == 1:
                gol = 'gol'
                print(f'Jogo {i + 1}: {g} {gol}')
            else:
                gol = 'gols'
                print(f'Jogo {i + 1}: {g} {gol}')
    if k == 'totalgols':
        print(f'Total de gols feito em {len(gols)} partida(s): {v} gols')
        print(f'Média de gols por partida: {v / len(gols):.2f} G/P')
print('=' * 30)
