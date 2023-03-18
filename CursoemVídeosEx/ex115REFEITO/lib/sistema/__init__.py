from ex115REFEITO.lib.interface import *


def leianome(txt):
    while True:
        try:
            nome = str(input(txt))
        except (TypeError, ValueError):
            linha()
            print('DIGITE UM NOME VÁLIDO!')
            linha()
        else:
            return nome


def leiaint(txt):
    while True:
        try:
            idade = int(input(txt))
        except (ValueError, TypeError):
            linha()
            print('DIGITE UM VALOR VÁLIDO!')
            linha()
        else:
            return idade


def verifarq(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except :
        print('Houve um erro na criação do arquivo.')


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ocorreu um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ocorreu um ERRO no cadastro dos dados.')
        else:
            a.close()


def lerarq(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Não foi possível abrir o arquivo.')
    else:
        linha()
        print('PESSOAS CADASTRADAS'.center(40))
        linha()
        for valores in a:
            dado = valores.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<37}{dado[1]}')
