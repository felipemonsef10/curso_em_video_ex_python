def dados(msg):
    cadastradas = {'Ana Paula Vieira': 32,
                   'Cláudio Mendonça': 18,
                   'Gustavo Guanabara': 41,
                   'Felipe Gabriel': 17}
    print('\033[1;32m-=\033[m' * 20)
    print('MENU PRICIPAL'.center(40))
    print('\033[1;32m-=\033[m' * 20)
    print('1 -> ver pessoas cadastradas'
          '\n2 -> cadastrar novas pessoas'
          '\n3 -> encerrar programa')
    print('\033[1;32m-=\033[m' * 20)
    while True:
        opcao = int(input(msg))
        if opcao == 1:
            print('\033[1;32m-=\033[m' * 20)
            print('\033[1;4;31mPESSOAS CADASTRADAS\033[m'.center(52))
            print('\033[1;32m-=\033[m' * 20)
            for k, v in cadastradas.items():
                print(f'{k:<20}', f'\t\t\t{v} anos')
            print('\033[1;32m-=\033[m' * 20)
        elif opcao == 2:
            print('\033[1;32m-=\033[m' * 20)
            print('\033[1;4;31mCADASTRANDO NOVA PESSOA\033[m'.center(52))
            print('\033[1;32m-=\033[m' * 20)
            nova = str(input('NOME: '))
            while True:
                try:
                    idade = int(input('IDADE: '))
                except:
                    print('\033[1;31mERRO: DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
                else:
                    break
            cadastradas[nova] = idade
            print(f'Novo registro de {nova} adicionado.')
        elif opcao == 3:
            print('\033[1;32m-=\033[m' * 20)
            print('\033[1;31mSAINDO DO SISTEMA...\033[m')
            print('\033[1;32m-=\033[m' * 20)
            break
        else:
            print('\033[1;31mERRO! DIGITE UMA OPÇÃO VÁLIDA.')
