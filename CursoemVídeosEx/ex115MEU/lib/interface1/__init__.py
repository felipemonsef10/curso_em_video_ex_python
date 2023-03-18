def menu():
    print('\033[1;32m-=\033[m' * 20)
    print('\033[1;31mMENU PRICIPAL\033[m'.center(47))
    print('\033[1;32m-=\033[m' * 20)
    print('\033[1;33m1\033[m -> \033[1;34mver pessoas cadastradas\033[m'
          '\n\033[1;33m2\033[m -> \033[1;34mcadastrar novas pessoas\033[m'
          '\n\033[1;33m3\033[m -> \033[1;34mencerrar programa\033[m')
    print('\033[1;32m-=\033[m' * 20)


def cadastro(arq):
    from ex115MEU.lib.arquivo1 import cadastrar, leiaint, leiastr
    print('\033[1;32m-=\033[m' * 20)
    print('\033[1;4;31mCADASTRANDO NOVA PESSOA\033[m'.center(52))
    print('\033[1;32m-=\033[m' * 20)
    nome = leiastr('\033[1;33mNOME: \033[m')
    idade = leiaint('\033[1;33mIDADE: \033[m')
    cadastrar(arq, nome, idade)


def finalizar():
    from time import sleep
    print('\033[1;32m-=\033[m' * 20)
    print('\033[1;31mFINALIZANDO SISTEMA...\033[m')
    print('\033[1;32m-=\033[m' * 20)
    sleep(2)
    print('\033[1;31mSISTEMA FINALIZADO COM SUCESSO\033[m')
    print('\033[1;32m-=\033[m' * 20)
