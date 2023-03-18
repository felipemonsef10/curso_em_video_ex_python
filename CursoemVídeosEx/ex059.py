sair = 5
escolha = 1
maior = 0
while escolha != 5:
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    print('''   ESCOLHA UMA OPÇÃO ABAIXO:
             [1]somar
             [2]multiplicar
             [3]maior
             [4]novos números
             [5]sair do programa''')

    escolha = int(input('Digite um número referente a tabela acima: '))
    if escolha == 1:
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    if escolha == 2:
        print('{} x {} = {}'.format(v1, v2, v1 * v2))
    if escolha == 3:
        if v1 > maior and v1 != v2:
            maior = v1
            if v2 > maior:
                maior = v2
                print('O número maior entre {} e {} é {}'.format(v1, v2, maior))
            else:
                print(maior)
        else:
            print('{} e {} são iguais.'.format(v1, v2))
print('Voçê saiu do programa!')
