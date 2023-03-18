from CADASTRO.testesarq import *
from CADASTRO.ler import *
from time import sleep


def linhas(tam):
    print('\033[1;36m=\033[m' * tam)


arq = 'testando.txt'
criararq(arq)

while True:
    cabecalho()
    linhas(35)
    opcao = leiaint('Sua opção: ', 'opção')
    linhas(35)

    if opcao == 1:
        lerarq(arq)

    if opcao == 2:
        print('CADASTRANDO NOVA PESSOA'.center(35))
        linhas(35)
        while True:
            nome = leianome('NOME: ')
            if not ''.join(nome.split()).isalpha():
                print('ERRO! Digite um nome válido.')
                linhas(35)
            else:
                break
        idade = leiaint('IDADE: ', 'idade')
        linhas(35)
        cadastrar(arq, nome, idade)

    if opcao == 3:
        print('FINALIZANDO SISTEMA...')
        sleep(2)
        print('SISTEMA FINALIZADO.')
        break

    elif opcao not in [1, 2, 3]:
        print('ERRO!Digite uma opção válida.')
