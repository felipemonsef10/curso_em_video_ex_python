print('=-' * 10)
print('TABELA DO BRASILEIRÃO')
print('=-' * 10)
times = 'Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', \
        'Athletico-PR', 'Atlético-MG', 'América-MG', 'Fortaleza', 'São Paulo',  \
        'Botafogo', 'Santos', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará', 'Cuiabá', \
        'Atlético-GO', 'Avaí', 'Juventude'
s = 0
for c in times:
    s += 1
    print(f'{s}º - {c}')
print('')
print(f'Os 5 primeiros colocados são respectivamente: {times[0]}, {times[1]}, {times[2]}, {times[3]} e {times[4]}.')
print(f'Os últimos 4 colocados são respectivamente: {times[-4]}, {times[-3]}, {times[-2]} e {times[-1]}.')
print('Os times organizados em ordem alfabéfica são: ')
print('')
s = 0
for ordem in sorted(times):
    s += 1
    print(f'{s}º - {ordem}')
print('')

# Jeito 1
for posi, time in enumerate(times):
    if time == 'São Paulo':
        print(f'O {time} está em {posi + 1}ª colocação na tabela.')

# Jeito 2
print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição.')
