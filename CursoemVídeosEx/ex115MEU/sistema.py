from ex115MEU.lib.arquivo1 import *
from ex115MEU.lib.interface1 import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararq(arq)

while True:
    menu()
    try:
        opcao = int(input('\033[1;31mSUA OPÇÃO: \033[m'))
    except (ValueError, TypeError):
        print('\033[1;4;31mERRO\033[m\033[1;31m! DIGITE UMA OPÇÃO VÁLIDA.\033[m')
    else:
        if opcao == 1:
            lerarq(arq)
        elif opcao == 2:
            cadastro(arq)
        elif opcao == 3:
            finalizar()
            break
        else:
            print('\033[1;4;31mERRO\033[m\033[1;31m!DIGITE UMA OPÇÃO VÁLIDA.\033[m')
