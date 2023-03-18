nomenota = []
nome = []
nota = []
medias = []
while True:
    nome.append(str(input('\033[1;31mNOME: \033[m')))
    nota.append(float(input('\033[1;35mNOTA 1: \033[m')))
    nota.append(float(input('\033[1;35mNOTA 2: \033[m')))
    medias.append((nota[0] + nota[1]) / 2)
    nome.append(nota[:])
    nomenota.append(nome[:])
    nome.clear()
    nota.clear()
    while True:
        contiua = str(input('\033[1mContinuar? \033[m')).upper().strip()[0]
        if contiua in 'SN':
            break
    if contiua == 'N':
        break
print('\033[1;30m=\033[m' * 30)
print(f'\033[1;35m{"No":<5}{"ALUNO":<15} {"MÉDIA"}\033[m')
print('-' * 30)
for c in range(len(nomenota)):
    print(f'\033[1;32m{c:<5}{nomenota[c][0]:<16}{medias[c]:.1f}\033[m')
print('-' * 30)
while True:
    mostrar = int(input('MOSTRAR NOTA DE QUAL ALUNO?(999 INTERROMPE) -> '))
    if mostrar != 999:
        print('-' * 30)
        print(f'NOTAS {nomenota[mostrar][0]}: {nomenota[mostrar][1]}')
        print('-' * 30)
    if mostrar == 999:
        break
print('=' * 30)
print(f'{"PROGRAMA FINALIZADO":^30}')
print('=' * 30)
# OUTRO JEITO
ficha = list()
while True:
    nome = str(input('NOME: '))
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
