def leiastr(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mDigite um nome válido\033[m')
        else:
            if n.isnumeric():
                print('\033[1;31mDigite um nome válido\033[m')
            else:
                return n


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


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print('\033[1;32m-=\033[m' * 20)
        for linha in a:
            dado = linha.split(';')
            print(f'\033[1;34m{dado[0]:<30}{dado[1]:3>}\033[m'.replace('\n', ''))


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao tentar cadastrar os dados!')
        else:
            a.close()
