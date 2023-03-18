dados = []
jogadores = {}
golstemp = []
while True:
    totalg = 0
    nome = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Partidas jogadas por {nome}: '))
    for c in range(partidas):
        gols = int(input(f'Gols na parida {c + 1}: '))
        totalg += gols
        golstemp.append(gols)
    jogadores[f'{nome}'] = partidas, golstemp[:], totalg
    golstemp.clear()
    dados.append(jogadores.copy())
    jogadores.clear()
    while True:
        continuar = str(input('Continuar: ')).upper().strip()[0]
        if continuar in 'NS':
            break
    if continuar == 'N':
        break
print(f'{"NOME":>15}{"Gols":>15}{"Total":>17}')
print('=' * 50)
for p, i in enumerate(dados):
    for k, v in i.items():
        print(f'Jogador{p + 1:}: {k:<14} {str(v[1]):<15} {v[2]:>4}')
print('=' * 50)
print()
while True:
    ver = int(input('Verificar estatísticas de qual jogador(999 para): '))
    for p, i in enumerate(dados):
        if ver == p + 1:
            c = 0
            for k, v in i.items():
                print('-' * 25)
                print(f'Estatísticas de {k}:')
                for g in v[1]:
                    c += 1
                    print(f'Jogo {c}: {g} gols')
                print('-' * 25)
    if ver == 999:
        break
print()

# OUTRO JEITO
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} fez: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostar dados de qual jogador? (999 para)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
