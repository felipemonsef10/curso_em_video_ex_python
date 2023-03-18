from ex115RESOLUÇÃO.lib.interface import *


def leiaint(msg='Digite um valor: '):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: O VALOR DIGITADO  NÃO É UM NÚMERO INTEIRO.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            n = 0
            return n
        else:
            return num


def arquivoexiste(nome):    # VERIFICA SE O ARQUIVO EXISTE
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):     # CRIA O ARQUIVO CASO NÃO EXISTA
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):       # LÊ O ARQUIVO
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:3>} anos')


def cadastrar(arq, nome='desconhecido', idade=0):   # ADICIONA DADOS AO ARQUIVO
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} add.')
            a.close()
