from time import sleep


# MEU JEITO
def pyHelp(a):
    if a == 'fim':
        return
    print(f'\033[1;34mAcessando o manual do \033[4;33m{a.upper()}\033[m\033[1;34m ...\033[m')
    sleep(3)
    print('\033[1;7;39;45m')
    help(a)
    print('\033[m')


while True:
    print('\033[1;7;38;48m-=\033[m' * 20)
    print('  \033[1;7;38;48m         SISTEMA DE AJUDA PyHelp.   \033[m')
    print('\033[1;7;38;48m-=\033[m' * 20)
    f = str(input('\n\033[1;32;40mFunção ou Biblioteca > \033[m')).strip().lower()
    pyHelp(f)
    if f == 'fim':
        break
print('\033[0;34mFINALIZANDO PROGRAMA... ')
sleep(2)
print('\033[4;35mFIM DE PROGRAMA.\033[m')
print()

# OUTRO JEITO
from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', cor=2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
