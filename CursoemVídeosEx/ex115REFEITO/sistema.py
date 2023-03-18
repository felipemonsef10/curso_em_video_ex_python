from ex115REFEITO.lib.sistema import *


arq = 'listapessoas.txt'
verificar = verifarq(arq)
if not verificar:
    criararq(arq)

while True:
    menu()
    linha()
    a = leiaint('SUA OPÇÃO: ')
    if a == 1:
        lerarq(arq)
    if a == 2:
        nome = leianome('NOME: ')
        idade = leiaint('IDADE: ')
        cadastrar(arq, nome, idade)
    if a == 3:
        saida()
        break
    if a not in (1, 2, 3):
        print('DIGITE UM VALOR VÁLIDO!')
