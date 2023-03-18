def linha(tam, cor):
    print(f'{cor}=\033[m' * tam)


def cabecalho():
    linha(35, '\033[1;36m')
    print('\033[1;33m1\033[m -> \033[1;34mMostrar pessoas cadastradas\033[m\n'
          '\033[1;33m2\033[m -> \033[1;34mCadastrar novas pessoas\033[m\n'
          '\033[1;33m3\033[m -> \033[1;34mEncerrar programa\033[m')


def criararq(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        try:
            a = open(arq, 'wt+')
            a.close()
        except:
            print('Não foi possível criar o arquivo.')
            return False
        else:
            print(f'Arquivo "{arq}" criado com sucesso.')
    else:
        print(f'Arquivo "{arq}" já existente.')


def cadastrar(arq, nome='Desconhecida', idade='Desconhecida'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao cadastrar os dados.')
        else:
            print(f'{nome} foi cadastrado com sucesso.')
            a.close()


def lerarq(arq):
    print('PESSOAS CADASTRADAS'.center(35))
    linha(35, '\033[1;36m')
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]}')
