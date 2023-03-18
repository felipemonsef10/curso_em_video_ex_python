from time import sleep


def linha():
    print('=' * 40)


def menu():
    linha()
    print('MENU PRINCIPAL'.center(40))
    linha()
    print('1 -> Ver pessoas cadastradas'
          '\n2 -> Cadastrar nova pessoa'
          '\n3 -> Encerrar programa')


def saida():
    linha()
    print('FINALIZANDO PROGRAMA...')
    linha()
    sleep(2)
    print('PROGRAMA FINALIZADO!')
    linha()
